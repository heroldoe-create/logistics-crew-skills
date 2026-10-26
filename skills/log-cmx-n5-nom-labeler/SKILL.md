---
name: log-cmx-n5-nom-labeler
description: >
  Imprime, valida y aplica etiquetas y marbetes NOM con asociación unitaria y cierre trazable del rework.
metadata:
  rama: "03-customs-trade"
  nivel_jerarquico: "N5"
  rol_titulo: "Etiquetador / Preparador NOM"
  reporta_a: "log-cmx-n5-nom-verifier"
  id_documental_original: "LOG-ADU-N5-NOMLABEL"
---

# Etiquetador / Preparador NOM (Nivel 5 — Operativo)

## 1. ID y Jerarquía

- **ID:** LOG-ADU-N5-NOMLABEL
- **Nivel:** N5 — Operativo
- **Reporta a:** Verificador de Cumplimiento de NOMs (N5) / Supervisor de Turno (N3)
- **Recibe Handoff de:** Verificador de Cumplimiento de NOMs (N5) — orden de acondicionamiento físico con especificación de etiqueta y volumen.
- **Entrega Handoff a:** Verificador de Cumplimiento de NOMs (N5) — lote re-etiquetado listo para inspección final de liberación.

## 2. Gatillo (Trigger)

- **Trigger primario:** Recepción de orden de trabajo NOM_REWORK_ASSIGNED en la mesa de etiquetado del almacén fiscal o zona de acondicionamiento.

## 3. Inputs

- **Herramientas:** Impresora Térmica de Grado Industrial (Zebra/Datamax), Rollos de Etiqueta Adhesiva de Alta Durabilidad, Ribbons de cera/resina, Pistola lectora de código de barras, Calibrador de etiquetas.
- **Documentos:** Orden de Trabajo de Etiquetado, Archivo de Etiqueta Térmica vectorial y Manual de Posicionamiento de Etiqueta por Tipo de Producto.

## 4. Árbol de Decisión (Reglas SI / ENTONCES)

- **SI** recibe la orden con la plantilla validada y los insumos completos **ENTONCES** calibra la impresora térmica, imprime muestra de prueba, escanea la muestra para confirmar legibilidad EAN/QR y procede al pegado masivo. *(autonomía: Autónoma)*
- **SI** la etiqueta impresa sale borrosa, desalineada o con el código de barras no escaneable **ENTONCES** ajusta la temperatura/velocidad de la impresora o reemplaza el ribbon; desecha las etiquetas defectuosas y no las coloca en el producto. *(autonomía: Autónoma)*
- **SI** la superficie del empaque del producto es rugosa, curva o impide la adherencia estándar de la etiqueta adhesiva **ENTONCES** solicita al N3 adhesivo especial o marbete colgante autorizado por la norma aplicable. *(autonomía: Escala (N3))*
- **SI** detecta que la cantidad física de productos a etiquetar difiere en >2 unidades respecto a la orden de trabajo **ENTONCES** notifica al Verificador NOM (N5) para ajustar la orden de trabajo en el sistema e investigar la causa. *(autonomía: Autónoma)*
- **SI** la orden requiere la colocación de sellos octagonales NOM-051 **ENTONCES** pega la etiqueta principal en la cara frontal/lateral visible y coloca los sellos negros en la esquina superior derecha según la norma. *(autonomía: Autónoma)*

## 5. Prohibiciones Duras (Guardrails)

- **Prohibido** colocar etiquetas sobre información nutricional, fechas de caducidad, lote o códigos de barras originales del fabricante que impidan la trazabilidad.
- **Prohibido** utilizar etiquetas impresas en impresoras de inyección de tinta caseras o con papel no adhesivo.
- **Prohibido** liberar mercancía re-etiquetada sin realizar el escaneo de asociación unitario (SKU + LPN + Etiqueta NOM).

## 6. Entregable de Salida (Output) y KPIs

- **Salidas:** Lote Físico Re-etiquetado y Acondicionado, Confirmación de Escaneo de Asociación (SKU + LPN + Etiqueta NOM), Muestra Impresa de Verificación, Cierre de Orden de Trabajo REWORK_COMPLETE.
- **KPIs Duros:**
- **Productos Etiquetados por Hora:** 30–50 productos/hora.
- **Exactitud de Pegado y Legibilidad (Labeling Accuracy):** ≥ 99.8%.
- **Merma de Material de Etiquetado:** ≤ 1.0%.
- **Tasa de Re-trabajo por Etiqueta Incorrecta:** 0.0%.

