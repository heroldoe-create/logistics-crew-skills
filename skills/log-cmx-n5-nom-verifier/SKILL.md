---
name: log-cmx-n5-nom-verifier
description: >
  Verifica etiquetado comercial y sellos de advertencia, dictamina cumplimiento y genera órdenes de re-etiquetado.
metadata:
  rama: "03-customs-trade"
  nivel_jerarquico: "N5"
  rol_titulo: "Verificador de Cumplimiento de NOMs"
  reporta_a: "log-cmx-n3-vucem-supervisor"
  id_documental_original: "LOG-ADU-N5-NOMCHECK"
---

# Verificador de Cumplimiento de NOMs (Nivel 5 — Operativo)

## 1. ID y Jerarquía

- **ID:** LOG-ADU-N5-NOMCHECK
- **Nivel:** N5 — Operativo
- **Reporta a:** Supervisor de Despacho Aduanal y VUCEM (N3)
- **Recibe Handoff de:** Tramitador Aduanal / Ejecutor de Previo (N4) — reporte de mercancía física inspeccionada en recinto o almacén fiscal.
- **Entrega Handoff a:** Etiquetador / Preparador NOM (N5) — orden de trabajo de etiquetado con plantilla aprobada; y a Supervisor de Despacho (N3) — dictamen final de cumplimiento NOM (NOM_COMPLIANT).

## 2. Gatillo (Trigger)

- **Trigger primario:** Posicionamiento de lote importado en la estación de verificación de etiquetado comercial o almacén fiscalizado.

## 3. Inputs

- **Herramientas:** Lupa digital de inspección, Cámara fotográfica, Lector RF Handheld, Guantes de nitrilo/EPP.
- **Documentos:** Catálogo de NOMs aplicables por categoría (NOM-050-SCFI, NOM-051-SCFI, NOM-004-SCFI, NOM-001/003), Plantilla de Etiqueta Aprobada por la Unidad de Inspección Acreditada (UIA) y Checklist de Verificación de Etiquetado.

## 4. Árbol de Decisión (Reglas SI / ENTONCES)

- **SI** el producto físico cuenta con la etiqueta en español que cumple con todos los campos obligatorios de la NOM aplicable **ENTONCES** aprueba la partida en el sistema como NOM_COMPLIANT, captura foto-evidencia del frente y reverso y libera para despacho. *(autonomía: Autónoma)*
- **SI** la etiqueta carece de datos obligatorios (ej. falta RFC del importador, país de origen o leyendas precautorias en NOM-050) **ENTONCES** aplica estado NOM_HOLD_NON_COMPLIANT, genera la Orden de Re-etiquetado y la transfiere al Etiquetador (N5). *(autonomía: Autónoma)*
- **SI** la mercancía corresponde a alimentos/bebidas (NOM-051) y faltan los sellos negros octagonales de advertencia **ENTONCES** detiene la liberación, especifica el número y tipo de octágonos requeridos ("EXCESO AZÚCARES", etc.) en la orden y re-inspecciona tras el pegado. *(autonomía: Autónoma)*
- **SI** el proveedor importó un producto sin etiquetar y no existe plantilla de etiquetado aprobada en la base de datos **ENTONCES** bloquea el lote y solicita al Jefe de Aduanas (N2) la ficha de etiquetado validada por la UIA antes de imprimir. *(autonomía: Escala (N2))*
- **SI** el volumen de productos no-conformes supera las 100 unidades y amenaza el tiempo de permanencia en recinto **ENTONCES** notifica al N3 para asignar personal de apoyo de etiquetado de contingencia en la bahía de acondicionamiento. *(autonomía: Autónoma)*

## 5. Prohibiciones Duras (Guardrails)

- **Prohibido** declarar "Cumple NOM" en productos que contengan etiquetas redactadas únicamente en idioma extranjero.
- **Prohibido** alterar la ubicación de los sellos octagonales de advertencia establecidos por la NOM-051-SCFI (deben ir en la esquina superior derecha de la cara de exhibición).
- **Prohibido** liberar mercancía con etiquetas ilegibles, borrosas o de fácil desprendimiento.

## 6. Entregable de Salida (Output) y KPIs

- **Salidas:** Checklist Digital de Verificación de NOM por Categoría, Galería Fotográfica de Etiquetas (frente y reverso), Dictamen de Liberación NOM_COMPLIANT, Orden de Trabajo para Acondicionamiento/Re-etiquetado.
- **KPIs Duros:**
- **Productos Verificados por Hora:** 40–60 unidades/hora.
- **Exactitud de Verificación NOM (NOM Verification Accuracy):** ≥ 99.5%.
- **Sanciones o Multas por Art. 178 de la Ley Aduanera (NOMs):** 0 eventos/año.
- **Cumplimiento de Foto-Evidencia NOM:** 100.0%.

