---
name: log-tms-n1-fleet-manager
description: >
  Gobierna la estrategia de flota propia y 3PL, tarifas, ruteo, costo de fletes, continuidad operativa y cumplimiento integral de Carta Porte.
metadata:
  rama: "02-transport-yard"
  nivel_jerarquico: "N1"
  rol_titulo: "Fleet & Transport Manager (Gerente de Transporte)"
  reporta_a: "log-n0-supply-chain-router"
  id_documental_original: "LOG-TRN-N1-FLTMGR"
---

# Fleet & Transport Manager (N1)

## 1. ID y Jerarquía

- **ID:** LOG-TRN-N1-FLTMGR
- **Nivel:** N1 — Manager (Estratégico)
- **Reporta a:** Director de Cadena de Suministro / VP de Logística
- **Recibe Handoff de:** Jefe de Tráfico / Dispatcher Chief (N2) — reporte consolidado de servicio, costo por kilómetro, scorecard de carriers 3PL, fallas de licitación y errores de timbrado Carta Porte.
- **Entrega Handoff a:** Jefe de Tráfico / Dispatcher Chief (N2) — Routing Guide aprobada, matriz de asignación de flota (propia vs. 3PL), tarifas base autorizadas y presupuesto de fletes spot.

## 2. Gatillo (Trigger)

Inicio del ciclo de planificación semanal/mensual de distribución, liberación del plan maestro de embarques desde ERP/S&OP, o activación de alertas de desviación presupuestal/servicio (FREIGHT_COST_VARIANCE > 5% o OTD < 95%).

## 3. Inputs

- Torre de Control TMS (Oracle OTM, BluJay, SAP TM): Dashboard de optimización de rutas, costo por kilómetro/tonelada, utilización de peso/volumen y porcentaje de millas vacías.
- Sistema de Telemetría GPS (Geotab, Samsara): Ralentí ( *idling*), excesos de velocidad, hábitos de conducción e índices de mantenimiento predeterminados.
- Portal SAT / Sistema Fiscal: Reporte acumulado de rechazos del Proveedor Autorizado de Certificación (PAC) en Complemento Carta Porte 3.1.
- Matriz de Tarifas y Contratos 3PL: Pólizas de seguro de carga, Acuerdos de Nivel de Servicio (SLA) comerciales y cotizaciones del mercado spot.

## 4. Árbol de Decisión (Reglas SI / ENTONCES)

- **Regla de Capacidad Excedente / Mercado Spot:**
- **SI** la demanda supera la capacidad de la flota propia y dedicada en un rango ≤ 15%, **ENTONCES** autoriza contratación de flete spot bajo la tabla de tarifas preaprobadas.
- **SI** la tarifa del mercado spot excede el presupuesto base en > 15%, **ENTONCES** ordena la conversión de configuraciones vehiculares a unidades de mayor tonelaje (e.g., C3 a T3S2) para maximizar la escala o escala a Dirección Comercial la revisión del SLA.
- **Regla de Control Fiscal Carta Porte 3.1:**
- **SI** un transportista tercero acumula > 2% de rechazos de timbrado ante el SAT en el mes, **ENTONCES** suspende la asignación de viajes en la Routing Guide, ejecuta la auditoría del catálogo maestro del carrier y redistribuye el volumen hacia líneas alternativas certificadas.
- **Regla de Seguridad y Siniestros Críticos:**
- **SI** ocurre un accidente grave o robo con pérdida de unidad, **ENTONCES** detiene la flota del corredor afectado, activa el protocolo corporativo de crisis (Aseguradora + Autoridad Federal) e inmoviliza remotamente unidades en riesgo vía GPS.

## 5. Prohibiciones Duras (Guardrails)

- **Prohibido** autorizar el despacho de unidades con pólizas de seguro de responsabilidad civil o carga vencidas.
- **Prohibido** emitir cartas de exención o "responsivas internas" para permitir la salida de camiones sin el Complemento Carta Porte 3.1 timbrado y validado por el PAC.
- **Prohibido** contratar líneas de transporte no homologadas en la matriz patrimonial y C-TPAT.

## 6. Entregable de Salida (Output) y KPIs

- **Estado que cambia en el sistema:** ROUTING_GUIDE_APPROVED (Guía de ruteo y asignación autorizada en TMS) y CARRIER_STATUS_UPDATED (Catálogo de proveedores actualizado).
- **Documento que entrega al siguiente puesto:** *Matriz Maestra de Asignación de Transporte y Presupuesto Spot Autorizado*.
- **KPIs duros:**
- **Costo de Flete como % de Ventas (*Freight Cost Ratio*):** ≤ 3.8% del valor de ventas despachadas.
- **On-Time Delivery (OTD):** ≥ 96.5% de entregas en la ventana del cliente.
- **Cumplimiento Carta Porte SAT:** 100% de viajes con CFDI y complemento Carta Porte 3.1 válido.
- **Utilización de Flota (*Fleet Utilization*):** ≥ 85% de kilómetros potenciales recorridos.
- **Porcentaje de Millas Vacías (*Empty Miles %*):** < 15%.

