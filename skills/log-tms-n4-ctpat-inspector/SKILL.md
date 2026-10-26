---
name: log-tms-n4-ctpat-inspector
description: >
  Ejecuta la inspección de 17 puntos, evidencia de seguridad y protocolo de sellos de alta seguridad ISO 17712.
metadata:
  rama: "02-transport-yard"
  nivel_jerarquico: "N4"
  rol_titulo: "Inspector C-TPAT / Seguridad e Inspección"
  reporta_a: "log-tms-n3-yard-dock-coordinator"
  id_documental_original: "LOG-TRN-N4-CTPAT"
---

# Inspector C-TPAT / Seguridad e Inspección (N4)

## 1. ID y Jerarquía

- **ID:** LOG-TRN-N4-CTPAT
- **Nivel:** N4 — Técnico (Ejecución Crítica)
- **Reporta a:** Yard Supervisor (N3) y Jefe de Seguridad Patrimonial
- **Recibe Handoff de:** Guardia de Acceso (N5) — unidad colocada en el carril de inspección pre-ingreso o pre-salida.
- **Entrega Handoff a:** Yard Supervisor (N3) y Guardia de Acceso (N5) — Formato de Inspección de 17 Puntos firmado, certificado de seguridad y colocación comprobada de sello de alta seguridad ISO 17712\.

## 2. Gatillo (Trigger)

Arribo de unidad de transporte de carga para embarque de exportación/C-TPAT, o notificación de inicio de sellado de tráiler tras finalizar la carga.

## 3. Inputs

- Lista de Cotejo de Inspección C-TPAT de 17 Puntos (Subelementos: Defensa delantera, motor, llantas, chasis, piso interior, paredes laterales, techo, puertas interiores/exteriores, quinta rueda, etc.).
- Criterio ISO 17712 para Sellos de Alta Seguridad ( *Bolt Seals*).
- Cámara Fotográfica HD / Tablet con aplicación de captación de evidencia fotográfica de seguridad (Mínimo 10 fotografías por inspección).
- Lámpara de inspección táctica, espejo cóncavo de inspección inferior y medidor de espesor de paredes.

## 4. Árbol de Decisión (Reglas SI / ENTONCES)

- **Regla de Inspección Físico-Estructural de 17 Puntos:**
- **SI** durante la inspección de cualquiera de los 17 puntos detecta modificaciones estructurales, compartimentos falsos, marcas de soldadura reciente, remaches sueltos o remanentes de sustancias no autorizadas, **ENTONCES** aplica un **bloqueo de seguridad inmediato**, prohíbe el ingreso/salida de la unidad, coloca la caja en cuarentena de seguridad e informa al Jefe de Seguridad Patrimonial.
- **Regla del Protocolo de Verificación de Sellos VVTT (View, Verify, Tap, Twist):**
- **SI** el sello de alta seguridad ISO 17712 no pasa la prueba física de tensión (Jalar fuertemente y girar el perno para verificar embonado), o el folio del perno no coincide con el folio impreso en la cabeza, **ENTONCES** rechaza el sello, lo destruye bajo acta y coloca un nuevo sello de alta seguridad homologado.
- **Regla de Inspección de Temperatura y Saneamiento (Reefer):**
- **SI** la caja es refrigerada y presenta olores extraños, suciedad en piso o la temperatura interna difiere en > 2°C del setpoint requerido, **ENTONCES** rechaza la unidad para carga y solicita saneamiento en patio.

## 5. Prohibiciones Duras (Guardrails)

- **Prohibido** omitir o dar por verificado "de vista" cualquiera de los 17 puntos requeridos en el estándar internacional de seguridad C-TPAT/OEA.
- **Prohibido** utilizar sellos de plástico o de banda metálica simple para embarques de exportación o transporte en corredores de alto riesgo (Solo sellos de perno de alta seguridad ISO 17712).
- **Prohibido** autorizar el cierre de puertas si se observa carga inestable o mercancía sin trincar.

## 6. Entregable de Salida (Output) y KPIs

- **Estado que cambia en el sistema:** CTPAT_INSPECTION_PASSED (Inspección aprobada) y BOLT_SEAL_AFFIXED (Sello de alta seguridad colocado y validado).
- **Documento que entrega al siguiente puesto:** *Checklist Digital de Inspección C-TPAT de 17 Puntos* firmado con paquete fotográfico y *Acta de Instalación de Sello ISO 17712*.
- **KPIs duros:**
- **Cumplimiento de Protocolo C-TPAT (*C-TPAT Compliance Rate*):** 100% de inspecciones sin omisiones.
- **Tiempo Promedio de Inspección de 17 Puntos:** ≤ 15 minutos por unidad.
- **Porcentaje de Sellos Correctamente Auditados:** 100%.
- **Vulnerabilidades de Seguridad / Brechas Detectadas:** 0 incidentes en tránsito.

