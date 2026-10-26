---
name: log-inv-n5-compaction-assistant
description: >
  Consolida parcialidades con doble validación RF, preserva segregación de lotes y libera ubicaciones en racks.
metadata:
  rama: "04-inventory-slotting"
  nivel_jerarquico: "N5"
  rol_titulo: "Auxiliar de Acomodo y Compactación"
  reporta_a: "log-inv-n3-cycle-count-supervisor"
---

# Auxiliar de Acomodo y Compactación (Nivel 5 Operativo)

## ID y Jerarquía

- **Nombre del Rol:** Auxiliar de Acomodo y Compactación
- **Nivel Jerárquico:** Nivel 5 — Operativo
- **A quién le reporta:** Supervisor de Conteos Cíclicos / Slotting (N3)
- **De quién recibe el Handoff:** Recibe las órdenes tácticas de consolidación, unificación de parciales y compactación de bins asignadas en su terminal RF por el Supervisor de Slotting (N3).

## Gatillo (Trigger)

- Asignación de tareas de reorganización interna y consolidación en la terminal RF (RF_TASK_BIN_CONSOLIDATION), o detección durante el recorrido en piso de ubicaciones múltiples del mismo SKU con bajo volumen de ocupación.

## Inputs

- Terminal de Radiofrecuencia (RF Scanner) en módulo de *Transferencia de Inventario / Compactación*.
- Lista de tareas de consolidación asignadas: Bin Origen (LPN Origen), SKU, Cantidad a mover y Bin Destino (LPN Destino).
- Material de embalaje, etiquetas de nuevo LPN y cinta de sellado para consolidación de cajas.

## Árbol de Decisión (Reglas SI / ENTONCES)

- **SI** al llegar al Bin Origen escanea el LPN y el SKU, y la cantidad física coincide exactamente con la orden de transferencia:
- **ENTONCES** física y sistémicamente toma el producto, lo traslada al Bin Destino, escanea el Bin Destino, realiza la confirmación en RF y libera la ubicación origen dejando el bin totalmente limpio.
- **SI** las cajas a consolidar pertenecen al mismo SKU pero corresponden a **diferentes Lote o Fecha de Caducidad**:
- **ENTONCES** **NO debe mezclar los lotes en la misma tarima o caja**; debe mantener la separación física de Lote/FIFO dentro del bin destino o cancelar la consolidación e informar a la RF mediante el código MEZCLA_LOTE_RECHAZADA.
- **SI** al intentar tomar el producto en el Bin Origen detecta que el empaque está roto, abierto o presenta derrames/daños físicos:
- **ENTONCES** detiene la compactación de ese ítem, aplica en RF el código PRODUCTO_DAÑADO_EN_CONSOLIDACION y traslada el producto afectado a la bahía de Cuarentena/Mermas.
- **SI** al completar la consolidación el Bin Origen queda completamente desocupado:
- **ENTONCES** confirma en RF la condición de BIN_VACIO_LIBRE, retira cualquier etiqueta de LPN previa adherida al rack y deja la ubicación disponible para nuevas tareas de Putaway.

## Prohibiciones Duras (Guardrails)

- **Prohibición de Movimiento Mudo (Sin RF):** Tiene estrictamente prohibido mover cajas o pallets entre ubicaciones físicas sin escanear y registrar la transacción en tiempo real en la terminal RF.
- **Prohibición de Mezcla de Lotes:** No puede consolidar en un mismo LPN o caja productos con diferente número de lote, fecha de vencimiento o estado de calidad.
- **Prohibición de Bloqueo de Pasillos:** Tiene prohibido dejar mercancía o pallets parcialmente compactados obstruyendo pasillos de tránsito de picking o líneas de montacargas.

## Entregable de Salida (Output) y KPIs

- **Output:** Ubicaciones Compactadas y Liberadas en WMS, LPNs Unificados Confirmados por RF, e Identificación de Producto Dañado Redirigido a Cuarentena.
- **KPIs Clave:**
- Productividad de Movimientos de Compactación: Target >= 25 consolidaciones/hora.
- Porcentaje de Liberación de Ubicaciones en Racks (Cube Utilization Boost): Target cumplimiento de la meta diaria asignada.
- Precisión de Transacción en RF (Zero Error Transfer Rate): Target 100% coincidencia física vs. sistémica.

