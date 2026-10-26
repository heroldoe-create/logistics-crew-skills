---
name: log-tms-n4-yard-hostler
description: >
  Ejecuta movimientos seguros de remolques entre patio y cortina con trazabilidad YMS y control físico-mecánico.
metadata:
  rama: "02-transport-yard"
  nivel_jerarquico: "N4"
  rol_titulo: "Controlador de Patio / Yard Hostler"
  reporta_a: "log-tms-n3-yard-dock-coordinator"
  id_documental_original: "LOG-TRN-N4-HOSTLER"
---

# Controlador de Patio / Yard Hostler (N4)

## 1. ID y Jerarquía

- **ID:** LOG-TRN-N4-HOSTLER
- **Nivel:** N4 — Técnico (Ejecución Crítica)
- **Reporta a:** Yard Supervisor / Dock Coordinator (N3)
- **Recibe Handoff de:** Yard Supervisor (N3) — orden de movimiento en terminal YMS/Radio (e.g., "Mover remolque X de Cajón A-12 a Cortina 05").
- **Entrega Handoff a:** Cargador / Surtidor de Piso (N5) — remolque posicionado, centrado y asegurado en cortina; y Supervisor de Patio (N3) — confirmación SPOTTED_AT_DOCK en YMS.

## 2. Gatillo (Trigger)

Recepción de tarea de movimiento de remolque ( *Jalón / Movimiento de Patio*) asignada en la terminal embarcada del tractor de patio o vía radio de comunicación.

## 3. Inputs

- Terminal RF / Tablet Embarcada en Tractor de Patio (Yard Goat): Interfaz YMS con mapa de patio, cola de movimientos y prioridades.
- Radio de Comunicación VHF/UHF de alta frecuencia.
- Checklist Pre-operacional del Tractor de Patio (Nivel de fluidos, presión 80-100 PSI, acoplamiento de quinta rueda hidráulica, mangueras de aire).

## 4. Árbol de Decisión (Reglas SI / ENTONCES)

- **Regla de Acoplamiento y Seguridad Físico-Mecánica:**
- **SI** al intentar acoplar un remolque detecta que las patas de apoyo ( *landing gear*) están trabadas, las líneas de aire dañadas o el piso del remolque colapsado, **ENTONCES** detiene la maniobra, aplica los frenos de estacionamiento del tractor, reporta inmediatamente la falla en el YMS y solicita la intervención del mecánico de patio.
- **Regla de Cortinas Ocupadas o Mal Centradas:**
- **SI** al llegar a la cortina asignada esta se encuentra bloqueada por otro remolque o el espacio no permite un centrado < 30 cm con respecto a la rampa de nivelación, **ENTONCES** no fuerza la maniobra, reporta la obstrucción al Supervisor de Patio y espera la liberación del muelle.
- **Regla de Velocidad y Prioridad de Movimiento:**
- **SI** opera en los pasillos de patio, **ENTONCES** mantiene velocidad < 15 km/h; al aproximarse a la zona de cortinas reduce a < 5 km/h.
- **SI** compiten dos movimientos, **ENTONCES** prioriza remolques refrigerados con unidades Thermo King activas sobre remolques secos.

## 5. Prohibiciones Duras (Guardrails)

- **Prohibido** mover remolques sin haber conectado las líneas de aire de servicio y emergencia ( *Gladhands*) y verificado el enganche físico de la quinta rueda.
- **Prohibido** realizar movimientos de patio si hay personal u operadores trabajando dentro del remolque o sobre la rampa de carga.
- **Prohibido** abandonar el tractor de patio con el motor encendido o sin los frenos de mano aplicados.

## 6. Entregable de Salida (Output) y KPIs

- **Estado que cambia en el sistema:** SPOTTED_AT_DOCK (Remolque posicionado en cortina) o MOVED_TO_STAGING (Remolque movido a estacionamiento).
- **Documento que entrega al siguiente puesto:** Confirmación digital en YMS de tarea finalizada y reporte de anomalías de cajas.
- **KPIs duros:**
- **Movimientos de Remolque por Hora (*Trailer Moves per Hour*):** 8 a 12 movimientos/hora.
- **Precisión de Posicionamiento en Cortina (*Dock Positioning Accuracy*):** ≥ 98% (Centrado perfecto para permitir paso de montacargas).
- **Cumplimiento de Tareas de Patio (*Move Completion Rate*):** ≥ 95%.
- **Tiempo de Inactividad de Equipo (*Equipment Downtime*):** < 3% del turno.

