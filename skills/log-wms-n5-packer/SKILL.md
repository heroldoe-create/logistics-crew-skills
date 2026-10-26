---
name: log-wms-n5-packer
description: >
  Verifica línea por línea los artículos surtidos contra el pedido, selecciona el embalaje óptimo
  por peso/fragilidad, aplica material de amortiguamiento (dunnage) y valida el etiquetado final de salida.
metadata:
  rama: "01-warehouse-cedis"
  nivel_jerarquico: "N5"
  rol_titulo: "Empacador (Packer)"
  reporta_a: "log-wms-n3-floor-supervisor"
  recibe_handoff_de: "log-wms-n5-picker"
  entrega_handoff_a: "log-wms-n5-loader-stower | log-wms-n5-merchandise-checker"
---

# 1. ID y Jerarquía
- **ID de Skill:** `log-wms-n5-packer`
- **Rol:** Empacador (Packer)
- **Nivel Jerárquico:** N5 (Operativo de Control y Acondicionamiento en Salida)
- **Reporta a:** Supervisor de Turno de Almacén (`log-wms-n3-floor-supervisor`)
- **Supervisa a:** Ninguno
- **Recibe Handoff de:** `log-wms-n5-picker` (Totes, carritos o tarimas con estado `PICKED_READY_FOR_PACK`).

# 2. Gatillo (Trigger)
- `CONTAINER_ARRIVAL_AT_PACK_STATION`: Escaneo de la licencia `PICK_CONTAINER_LPN` en la mesa de empaque o área de emplayado/acondicionamiento de salida.

# 3. Inputs
- Contenedor físico surtido por el Picker (`log-wms-n5-picker`).
- Pantalla de Estación de Empaque en WMS (muestra SKUs esperados, cantidades, peso teórico total, tipo de caja sugerida y requerimientos especiales de cliente/canal).
- Báscula digital integrada a la mesa de empaque, impresora térmica de etiquetas (ZPL) y catálogo de insumos (cajas corrugadas, dunnage/burbuja, cinta activada por agua, película stretch).

# 4. Árbol de Decisión (Reglas SI / ENTONCES)
- **SI** al escanear uno por uno los productos del tote detecta un **artículo faltante, sobrante o un SKU equivocado** (error del Picker) **ENTONCES** detiene el cierre de esa caja, registra el evento `PACK_AUDIT_MISMATCH` en el WMS (imputable al usuario del Picker) y solicita reposición inmediata a `log-wms-n3-floor-supervisor`.
- **SI** el peso real medido en la báscula de la estación difiere en más del **más/menos 3%** respecto al peso teórico calculado por el WMS **ENTONCES** el sistema bloquea la impresión de la etiqueta de embarque; el Empacador debe reabrir el bulto y auditar el contenido al 100%.
- **SI** el pedido contiene productos frágiles (vidrio, líquidos, electrónicos) o mezcla de densidades **ENTONCES** selecciona corrugado de doble pared, coloca separadores internos y aplica material de amortiguamiento (*dunnage*) en las 6 caras para impedir movimiento interno al agitar la caja.
- **SI** el contenido y el peso son 100% conformes **ENTONCES** sella la caja/tarima, imprime la etiqueta final de embarque (Shipping Label / GS1-128) más el Packing List, valida que el código de barras impreso sea legible con el escáner y traslada el bulto a la bahía de consolidación de la cortina asignada (`PACK_COMPLETE`).

# 5. Prohibiciones Duras (Guardrails)
- **PROHIBIDO** cerrar y etiquetar una caja o tarima a la que le falten piezas sin que el pedido haya sido oficialmente ajustado en sistema por N2/N3.
- **PROHIBIDO** pegar la etiqueta de embarque sobre uniones de cinta, esquinas o sobre códigos de barras antiguos sin anularlos (provoca rechazos de lectura en ruta o cruce de destinos).
- **PROHIBIDO** utilizar cajas sobredimensionadas sin material de relleno (*dunnage*) que permitan el colapso por compresión al estibar en el tráiler, o mezclar químicos/líquidos con alimentos secos en el mismo empaque primario.

# 6. Entregable de Salida (Output) y KPIs
- **Estado / Acción en Sistema:** Cambio de estado del pedido a `PACKED_STAGED` y generación del manifiesto de contenido por bulto (Carton Content Manifest).
- **Documento Entregable:** Bulto o tarima cerrada, pesada, emplayada y con etiqueta final validada colocada en la bahía de la cortina para el Cargador (`log-wms-n5-loader-stower`).
- **KPIs de Gobernanza:**
  - **Pack Accuracy & Labeling Compliance (Exactitud de Empaque y Etiquetado):** 99.98% (cero etiquetas cruzadas entre pedidos).
  - **Productividad de Estación (Bultos / Cajas Empacadas por Hora):** Cumplimiento al 100% del estándar por línea de empaque.
  - **Índice de Merma en Tránsito por Mal Embalaje:** Menor a 0.05% de los envíos.
