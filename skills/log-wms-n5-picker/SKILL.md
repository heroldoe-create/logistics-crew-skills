---
name: log-wms-n5-picker
description: >
  Ejecuta el surtido secuencial de pedidos mediante terminal RF o Voz siguiendo la ruta óptima
  (Snake Pattern), con escaneo obligatorio de ubicación/SKU y reporte inmediato de Short Picks.
metadata:
  rama: "01-warehouse-cedis"
  nivel_jerarquico: "N5"
  rol_titulo: "Surtidor (Picker)"
  reporta_a: "log-wms-n3-floor-supervisor"
  recibe_handoff_de: "log-wms-n2-ops-chief | log-wms-n4-reach-truck-operator"
  entrega_handoff_a: "log-wms-n5-packer | log-wms-n3-floor-supervisor"
---

# 1. ID y Jerarquía
- **ID de Skill:** `log-wms-n5-picker`
- **Rol:** Surtidor (Picker RF / Voz)
- **Nivel Jerárquico:** N5 (Operativo de Ejecución en Piso)
- **Reporta a:** Supervisor de Turno de Almacén (`log-wms-n3-floor-supervisor`)
- **Supervisa a:** Ninguno
- **Recibe Handoff de:** `log-wms-n2-ops-chief` (Listas de surtido generadas al liberar la ola) y `log-wms-n4-reach-truck-operator` (Ubicaciones de picking reabastecidas).

# 2. Gatillo (Trigger)
- `PICK_TASK_ASSIGNED`: Asignación de una tarea de surtido (por pedido individual, Batch Picking, Cluster o Tarima completa) en la terminal RF o auricular de Pick-by-Voice tras el `WAVE_RELEASE`.

# 3. Inputs
- Secuencia de recorrido en terminal RF / Voz (Pasillo -> Bahía -> Nivel -> Posición -> Check-digit -> SKU -> Lote -> Cantidad a tomar).
- Código de barras de la ubicación física (Check-digit) y código de barras del producto (EAN/UPC/DUN-14).
- Contenedor, tote o tarima de surtido identificada con etiqueta de licencia de salida (`PICK_CONTAINER_LPN`).

# 4. Árbol de Decisión (Reglas SI / ENTONCES)
- **SI** la ubicación y el producto coinciden al escanear y hay stock físico suficiente **ENTONCES** toma la cantidad exacta solicitada, coloca las piezas pesadas en la base del contenedor y las ligeras arriba, confirma en RF y avanza al siguiente punto de la ruta en serpentina (*Snake Pattern*).
- **SI** llega a la ubicación sugerida por el WMS y el stock físico es cero o menor a la cantidad solicitada (**Cero Pick / Short Pick**) **ENTONCES** verifica visualmente el fondo del bin/rack, escanea el código de excepción `SHORT_PICK_REPORT` en RF y notifica de inmediato a `log-wms-n3-floor-supervisor` para activar reabasto urgente o conteo cíclico.
- **SI** encuentra las cajas o piezas en la ubicación dañadas, abiertas o con derrame **ENTONCES** no las surte en el pedido del cliente; segrega las piezas dañadas en el área de merma de pasillo, marca `DAMAGED_AT_PICKFACE` en RF y solicita reposición si el saldo sano restante no alcanza.
- **SI** completa todas las líneas de su tarea de surtido **ENTONCES** cierra el contenedor en RF (`PICK_COMPLETE`), adhiere la etiqueta de viaje y deposita la carga en la banda o mesa de entrada de Empaque (`log-wms-n5-packer`).

# 5. Prohibiciones Duras (Guardrails)
- **PROHIBIDO** tomar producto de una ubicación distinta a la que indica el WMS (ej. tomar de un rack vecino o de reserva) aunque visualmente sea el mismo SKU, sin cambio de tarea autorizado en RF.
- **PROHIBIDO** sustituir por cuenta propia un SKU agotado por otro modelo, presentación, sabor o lote distinto no asignado por el sistema (facultad exclusiva de `log-wms-n2-ops-chief`).
- **PROHIBIDO** alterar o saltarse la secuencia de ruta óptima (*Snake Pattern*) sin causa de pasillo bloqueado, o confirmar lecturas sin escanear físicamente el producto.

# 6. Entregable de Salida (Output) y KPIs
- **Estado / Acción en Sistema:** Cambio de estado del pedido/contenedor a `PICKED_READY_FOR_PACK` o alerta `SHORT_PICK_TRIGGERED`.
- **Documento Entregable:** Tarima o Tote surtido con su etiqueta `PICK_CONTAINER_LPN` entregado físicamente en la estación del Empacador (`log-wms-n5-packer`).
- **KPIs de Gobernanza:**
  - **Picking Accuracy (Exactitud de Surtido):** Mayor o igual a 99.9% (cero cruces de SKU o cantidades incorrectas).
  - **Productividad de Surtido (LPPH - Líneas o Cajas por Hora):** Cumplimiento al 100% de la meta por zona (Caja completa vs. Pieza suelta).
  - **Falsos Short Picks (Reportar faltante cuando sí había stock en el bin):** 0% tolerado.
