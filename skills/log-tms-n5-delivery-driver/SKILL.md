---
name: log-tms-n5-delivery-driver
description: >
  Conduce y resguarda la carga, cumple ruta y seguridad, gestiona entrega, rechazos y captura del comprobante POD.
metadata:
  rama: "02-transport-yard"
  nivel_jerarquico: "N5"
  rol_titulo: "Chofer de Reparto / Operador de Unidad"
  reporta_a: "log-tms-n2-dispatcher-chief"
  id_documental_original: "LOG-TRN-N5-DRIVER"
---

# Chofer de Reparto / Operador de Unidad (N5)

## 1. ID y Jerarquía

- **ID:** LOG-TRN-N5-DRIVER
- **Nivel:** N5 — Operativo de Piso
- **Reporta a:** Jefe de Tráfico / Dispatcher Chief (N2)
- **Recibe Handoff de:** Supervisor de Expedición (N3) y Guardia de Acceso (N5) — unidad cargada, trincada, sellada y carpeta documental completa (Carta Porte 3.1, BOL, manifiesto).
- **Entrega Handoff a:** Cliente / Destinatario final — entrega física de mercancía en rampa y obtención de acuse de recibo firmado ( *Proof of Delivery - POD*).

## 2. Gatillo (Trigger)

Asignación de la Orden de Viaje en la aplicación móvil de transporte, entrega de llaves del vehículo y recepción del expediente de traslado en la caseta de salida.

## 3. Inputs

- Expediente de Viaje: Representación impresa o PDF en dispositivo electrónico de la Carta Porte 3.1 (con código QR e IdCCP visible), Manifiesto de Carga y Hojas de Seguridad HAZMAT (si aplica).
- App Móvil de Navegación y Telemetría: Geocerca de ruta autorizada, puntos de parada permitidos y reloj de horas de conducción.
- Licencia Federal de Conducir Vigente (Tipo B, C, D o E) y Tarjeta de Identificación del Operador.

## 4. Árbol de Decisión (Reglas SI / ENTONCES)

- **Regla de Inspección Oficial en Carretera (Guardia Nacional / SAT):**
- **SI** las autoridades de inspección en vías federales solicitan la documentación del traslado, **ENTONCES** exhibe la representación impresa o la pantalla del dispositivo móvil con el código QR del Complemento Carta Porte 3.1.
- **SI** la autoridad alega alguna inconsistencia en el documento, **ENTONCES** se comunica inmediatamente con la Central de Monitoreo/Tráfico (N2) antes de firmar cualquier acta.
- **Regla de Rechazo Parcial o Total en Cliente:**
- **SI** el cliente en destino rechaza mercancía por daño o discrepancia de cantidad, **ENTONCES** no retira la unidad de la rampa, toma foto-evidencia del rechazo, registra el evento en la App móvil bajo la clave DELIVERY_REJECTED y solicita autorización al Dispatcher (N2) antes de retornar con el producto.
- **Regla de Seguridad y Alertas GPS / NOM-087:**
- **SI** llega a 4.5 horas de conducción continua (margen antes del tope de 5 horas de la NOM-087-SCT-2-2017), **ENTONCES** ingresa obligatoriamente a un parador seguro autorizado por la geocerca para realizar la pausa de 30 minutos estipulada en la NOM-087-SCT.
- **SI** detecta un intento de despojo o interferencia de señal (Jammer), **ENTONCES** presiona el botón de pánico de la unidad y ejecuta el protocolo de inmovilización.

## 5. Prohibiciones Duras (Guardrails)

- **Prohibido** iniciar el tránsito por carreteras o vías de jurisdicción federal sin llevar consigo la representación impresa o digital válida del Complemento Carta Porte 3.1 con su código QR e IdCCP.
- **Prohibido** romper, manipular o retirar el sello de alta seguridad ( *Bolt Seal*) del remolque antes de posicionarse en la cortina de descarga del cliente y contar con la presencia del receptor.
- **Prohibido** desviarse de la ruta y geocerca autorizadas en el TMS o realizar paradas en puntos no catalogados como "Paradores Seguros".
- **Prohibido** apagar el equipo GPS o portar dispositivos de interferencia de señal.

## 6. Entregable de Salida (Output) y KPIs

- **Estado que cambia en el sistema:** IN_TRANSIT → ARRIVED_AT_CUSTOMER → DELIVERED_POD_OK.
- **Documento que entrega al siguiente puesto:** *Acuse de Recibo Comercial / POD (Proof of Delivery)* firmado y sellado por el cliente, entregado físicamente o digitalizado vía App en < 24 horas.
- **KPIs duros:**
- **Entregas a Tiempo (*On-Time Delivery Rate*):** ≥ 96.5%.
- **Tasa de Captura Digital de Acuses (*POD Capture Rate*):** 100% digitalizado en < 24 horas.
- **Cumplimiento de Ruta y Geocerca (*Route Compliance*):** ≥ 98%.
- **Multas o Sanciones por Carta Porte / Tránsito:** 0 eventos.

