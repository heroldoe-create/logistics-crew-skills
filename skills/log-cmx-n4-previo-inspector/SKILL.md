---
name: log-cmx-n4-previo-inspector
description: >
  Ejecuta el previo físico-documental con evidencia fotográfica, dictamen de conformidad y escalamiento de discrepancias.
metadata:
  rama: "03-customs-trade"
  nivel_jerarquico: "N4"
  rol_titulo: "Tramitador Aduanal / Ejecutor de Previo"
  reporta_a: "log-cmx-n3-vucem-supervisor"
  id_documental_original: "LOG-ADU-N4-PREVIOEXEC"
---

# Tramitador Aduanal / Ejecutor de Previo (Nivel 4 — Técnico)

## 1. ID y Jerarquía

- **ID:** LOG-ADU-N4-PREVIOEXEC
- **Nivel:** N4 — Técnico
- **Reporta a:** Supervisor de Despacho Aduanal y VUCEM (N3)
- **Recibe Handoff de:** Recinto Fiscalizado / Naviera / Línea Aérea — notificación de disponibilidad de contenedor/mercancía para reconocimiento previo.
- **Entrega Handoff a:** Verificador de NOMs (N5) — notificación de mercancía sujeta a etiquetado/certificación; y a Supervisor de Despacho (N3) — Acta de Previo Aduanal con dictamen técnico y galería fotográfica.

## 2. Gatillo (Trigger)

- **Trigger primario:** Generación de la orden de previo aduanal en el recinto fiscalizado o puerto/aeropuerto previo al pago del pedimento.

## 3. Inputs

- **Dispositivos y Herramientas:** Tablet con Lista de Chequeo Digital de Previo, Lector RF, Cámara fotográfica (mínimo 12MP) con geo-referenciación y estampa de fecha/hora, EPP completo de seguridad portuaria.
- **Documentos:** Orden de Trabajo de Previo, Factura Comercial (Invoice), Packing List, Bill of Lading (BL) / AWB y Formato de Acta de Previo.

## 4. Árbol de Decisión (Reglas SI / ENTONCES)

- **SI** la mercancía física coincide al 100% con la factura y packing list en descripción, marca, modelo, series, bultos y peso **ENTONCES** captura mínimo 10 fotografías (exterior, interior, etiquetas, marcas), firma el Acta de Previo como "Conforme" y envía el reporte al N3. *(autonomía: Autónoma)*
- **SI** detecta sobrantes de mercancía >5% o productos no declarados en la factura comercial **ENTONCES** detiene la inspección física, aplica el bloqueo PREVIO_HOLD, toma evidencia de la demasía y escala inmediatamente al Jefe de Aduanas (N2). *(autonomía: Escala (N2))*
- **SI** observa que los sellos de seguridad del contenedor están rotos, violados o no corresponden al BL **ENTONCES** toma fotografías detalladas de las puertas y del mecanismo de cierre, no abre el contenedor sin el representante del recinto y notifica a N3. *(autonomía: Autónoma)*
- **SI** la mercancía presenta daños físicos, humedad, derrames o empaque colapsado **ENTONCES** documenta el estado en la nota de tarja, fotografía la avería, calcula el porcentaje de afectación y solicita la firma de disconformidad de la terminal. *(autonomía: Autónoma)*
- **SI** detecta que el producto carece de etiquetado comercial en español (NOM-050/051/004) **ENTONCES** marca la casilla "Requiere Acondicionamiento NOM" en la lista de chequeo y transfiere el reporte al Verificador de NOMs (N5). *(autonomía: Autónoma)*

## 5. Prohibiciones Duras (Guardrails)

- **Prohibido** emitir un dictamen de previo "Conforme" sin haber contado y fotografiado físicamente la mercancía (estrictamente prohibido el "previo de escritorio").
- **Prohibido** manipular o retirar muestras de producto sin el acta de muestreo oficial o autorización por escrito del N2.
- **Prohibido** omitir el reporte de mercancía no declarada o con discrepancias de serie/modelo.

## 6. Entregable de Salida (Output) y KPIs

- **Salidas:** Acta de Previo Aduanal firmada digitalmente, Galería Fotográfica de Inspección (mínimo 10 tomas por contenedor/lote), Reporte de Discrepancias de Previo (PREVIO_VARIANCE_REPORT), Solicitud de Re-etiquetado/Acondicionamiento NOM.
- **KPIs Duros:**
- **Previos Completados por Día:** 3–5 previos/día (según complejidad del embarque).
- **Exactitud de Inspección Previa (Previo Accuracy):** ≥ 98.0%.
- **Cumplimiento de Evidencia Fotográfica:** 100.0% de previos con fotos completas.
- **Detección Temprana de Errores Físicos vs. Documentales:** 100.0% antes de transmisión.

