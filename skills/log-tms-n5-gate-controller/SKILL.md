---
name: log-tms-n5-gate-controller
description: >
  Valida citas, identidad, placas, peso, documentos y sellos; controla el bloqueo duro de ingreso y egreso en caseta.
metadata:
  rama: "02-transport-yard"
  nivel_jerarquico: "N5"
  rol_titulo: "Guardia de Acceso de Transporte / Gate Controller"
  reporta_a: "log-tms-n3-yard-dock-coordinator"
  id_documental_original: "LOG-TRN-N5-GATE"
---

# Guardia de Acceso de Transporte / Gate Controller (N5)

## 1. ID y Jerarquía

- **ID:** LOG-TRN-N5-GATE
- **Nivel:** N5 — Operativo de Piso
- **Reporta a:** Yard Supervisor / Dock Coordinator (N3)
- **Recibe Handoff de:** Chofer de Reparto (N5) — presentación en caseta con documentación de viaje; y Supervisor de Patio (N3) — autorización de salida y pase de salida firmado.
- **Entrega Handoff a:** Yard Hostler (N4) — remolque listo en caseta para maniobra de ingreso; y Chofer de Reparto (N5) — entrega de Pase de Salida ( *Gate Pass*) y apertura física de la barrera de caseta.

## 2. Gatillo (Trigger)

Posicionamiento físico de un vehículo de carga sobre los sensores de presencia del carril de ingreso o egreso de la caseta de control ( *Gate*).

## 3. Inputs

- Sistema de Control de Accesos / Gate Management (YMS/TMS): Módulo de validación de citas y registro de placas.
- Lector Automático de Código de Barras / QR / Scanner OCR para tarjetas de circulación y licencias.
- Expediente Físico/Digital de Salida: Representación impresa/digital del CFDI 4.0 con Complemento Carta Porte 3.1 (verificando código QR e IdCCP), Licencia Federal del Chofer e Identificación Oficial.
- Báscula de Piso de Caseta: Registro de peso bruto vehicular.

## 4. Árbol de Decisión (Reglas SI / ENTONCES)

- **Regla de Validación Estricta de Ingreso (Gate In):**
- **SI** el vehículo se presenta en caseta, **ENTONCES** valida en sistema: (1) Cita vigente, (2) Licencia del chofer activa, (3) Placas coincidentes.
- **SI** alguno de estos 3 puntos no coincide o la cita no existe, **ENTONCES** niega el ingreso, desvía la unidad al carril de espera ( *Holding Bay*) y reporta al Supervisor de Patio (N3).
- **Regla de Bloqueo Absoluto de Egreso por Carta Porte 3.1 (Gate Out):**
- **SI** la unidad intenta salir del CEDIS y la representación impresa/digital del CFDI **no incluye el Complemento Carta Porte 3.1**, falta el identificador IdCCP o la lectura del código QR no arroja la estructura oficial del SAT, **ENTONCES** mantiene la barrera abajo, aplica un **bloqueo duro por seguridad fiscal** e impide la salida de la unidad hasta la entrega del documento válido.
- **Regla de Inspección de Sellos de Salida:**
- **SI** al revisar la salida el número de sello de alta seguridad físico no coincide letra por letra con el número registrado en el pase de salida o presenta marcas de corte/violación, **ENTONCES** retiene el vehículo y notifica a Seguridad Patrimonial.
- **Regla de Exceso de Peso (NOM-012-SCT):**
- **SI** la báscula de piso registra un peso bruto vehicular superior al límite máximo permitido para la configuración de la unidad, **ENTONCES** prohíbe la salida y solicita un ajuste de estiba/descarga parcial.

## 5. Prohibiciones Duras (Guardrails)

- **Prohibido** permitir el ingreso de conductores que muestren signos de fatiga extrema, alcoholemia o bajo la influencia de sustancias.
- **Prohibido** autorizar salidas "de palabra" o mediante notas manuscritas sin la validación del sistema y la representación de la Carta Porte 3.1.
- **Prohibido** permitir el ingreso de acompañantes o personas no autorizadas en la cabina del tractocamión.

## 6. Entregable de Salida (Output) y KPIs

- **Estado que cambia en el sistema:** Evento GATE_IN_PROCESSED o GATE_OUT_RELEASED registrado en YMS/TMS.
- **Documento que entrega al siguiente puesto:** *Pase de Salida (Gate Pass)* escaneado y registrado; y Comprobante de Pesaje de Báscula.
- **KPIs duros:**
- **Tiempo de Procesamiento en Caseta (*Gate Cycle Time*):** < 8 minutos por vehículo (Ingreso/Egreso).
- **Exactitud de Registros de Caseta (*Gate Record Accuracy*):** 100%.
- **Salidas sin Carta Porte 3.1 o Sello Válido:** 0 eventos (Bloqueo duro absoluto).
- **Vehículos Procesados por Hora:** 15 a 25 unidades/hora.

