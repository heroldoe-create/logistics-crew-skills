---
name: log-inv-n4-cycle-counter
description: >
  Ejecuta conteos ciegos por RF, registra existencias reales y reporta daños, contaminación de SKU y ubicaciones vacías.
metadata:
  rama: "04-inventory-slotting"
  nivel_jerarquico: "N4"
  rol_titulo: "Auxiliar de Inventarios / Contador Cíclico"
  reporta_a: "log-inv-n3-cycle-count-supervisor"
---

# Auxiliar de Inventarios / Contador Cíclico (Nivel 4 Técnico)

## ID y Jerarquía

- **Nombre del Rol:** Auxiliar de Inventarios / Contador Cíclico
- **Nivel Jerárquico:** Nivel 4 — Técnico Operativo
- **A quién le reporta:** Supervisor de Conteos Cíclicos / Slotting (N3)
- **De quién recibe el Handoff:** Recibe la asignación de rutas de recuento en la terminal RF del Supervisor de Conteos Cíclicos (N3).

## Gatillo (Trigger)

- Inicio de turno operativo, recepción de tareas de conteo ciego programadas en la pantalla del Handheld RF (RF_TASK_CYCLE_COUNT), o notificación urgente de verificación de bin por reporte de "Cero Pick".

## Inputs

- Terminal de Radiofrecuencia (RF Scanner) configurada en módulo de *Conteo Ciego*.
- Lista de ubicaciones físicamente asignadas para auditoría (sin despliegue de piezas esperadas).
- Código de barras de ubicación, código LPN (License Plate Number) y código de SKU/UPC.

## Árbol de Decisión (Reglas SI / ENTONCES)

- **SI** al ingresar a la ubicación indicada por la RF, la etiqueta del bin y los LPNs escaneados coinciden perfectamente con los códigos físicos:
- **ENTONCES** efectúa el recuento pieza por pieza (o caja cerrada por caja cerrada), ingresa la cifra en la terminal RF y confirma la tarea para avanzar al siguiente bin.
- **SI** al realizar el recuento encuentra cajas abiertas, dañadas o piezas sueltas con código ilegible:
- **ENTONCES** separa físicamente el producto afectado, aplica el código de estado DAÑO_SUPERFICIAL o ETIQUETA_ILEGIBLE en la RF y solicita la impresión de nueva etiqueta de control.
- **SI** el conteo físico no coincide con la capacidad aparente del bin o detecta un producto diferente al asignado a esa ubicación (Cross-Contamination de SKU):
- **ENTONCES** escanea el SKU físicamente encontrado, registra la cantidad real sin modificar la ubicación y genera la alerta automática de UBICACIÓN_CONTAMINADA al **Supervisor de Conteos (N3)**.
- **SI** la ubicación asignada se encuentra totalmente vacía físicamente:
- **ENTONCES** confirma en RF el conteo en 0 unidades, valida que no existan piezas en la parte posterior del rack o caídas en la estructura y cierra la tarea como ZERO_BIN_CONFIRMED.

## Prohibiciones Duras (Guardrails)

- **Prohibición Absoluta de Acceso al Saldo Teórico:** Tiene estrictamente prohibido consultar el saldo del WMS en la terminal RF o en pantallas del sistema antes de realizar y capturar el conteo físico.
- **Prohibición de Re-ubicación No Autorizada:** No puede mover físicamente productos de una ubicación a otra durante el conteo cíclico para "acomodar" el inventario sin registrar la transacción de transferencia en RF.
- **Prohibición de Ajuste Contable:** No posee credenciales ni menús en la terminal RF para autorizar o aplicar ajustes positivos o negativos en el inventario.

## Entregable de Salida (Output) y KPIs

- **Output:** Captura de Conteo Ciego confirmada en WMS por RF, Reporte de Unidades Dañadas / Ilegibles en Piso, y Registro de Ubicaciones Contaminadas.
- **KPIs Clave:**
- Productividad de Conteo (Ubicaciones / Horas Contadas): Target >= 35 bins/hora.
- Precisión del Conteo Ciego (Accuracy on Audited Counts): Target >= 99.0% respecto a reconteos de auditoría.
- Cumplimiento de la Ruta de Conteo Asignada: Target 100% al finalizar la jornada.

