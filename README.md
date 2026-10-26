# Logistics Crew Skills

**30 puestos de una operación logística mexicana, escritos como skills para agentes de IA:** del orquestador al surtidor, en cuatro ramas — almacén/CEDIS, transporte y patio, aduanas y comercio exterior, inventario y slotting.

Cada skill es una ficha de puesto que un agente puede seguir: **quién es, a quién reporta, qué evento lo activa, qué lee, qué decide (reglas SI / ENTONCES), qué tiene prohibido y qué entrega**, con los indicadores con que se le mide. El orquestador recibe el evento («llegó un contenedor», «el conteo no cuadra») y se lo pasa al puesto que es dueño de la decisión.

Autor: **Heroldo Escobedo** · [heroldo.org](https://heroldo.org) · español de México.

## Para qué sirve

- **Darle criterio de piso a un agente.** Un modelo genérico no sabe que un surtidor no sustituye un SKU agotado por su cuenta, ni que un verificador NOM detiene el despacho sin certificado. Estas fichas se lo dicen con reglas que se pueden revisar.
- **Diseñar o auditar un flujo.** Las fichas sirven igual sin IA: son un mapa de quién decide qué, con sus límites de autoridad y sus escalamientos.
- **Entrenar a un equipo.** Cada regla SI / ENTONCES es un caso de piso que se puede discutir con supervisores.

## Las 30 skills

| Rama | Nivel | Puesto | Skill |
|---|---|---|---|
| Orquestador | N0 | Director de Supply Chain / Orquestador General | [`log-n0-supply-chain-router`](skills/log-n0-supply-chain-router/SKILL.md) |
| Almacén / CEDIS | N1 | Warehouse Manager (Gerente de CEDIS) | [`log-wms-n1-warehouse-manager`](skills/log-wms-n1-warehouse-manager/SKILL.md) |
| Almacén / CEDIS | N2 | Jefe de Operaciones de Almacén (Inbound/Outbound/Inversa) | [`log-wms-n2-ops-chief`](skills/log-wms-n2-ops-chief/SKILL.md) |
| Almacén / CEDIS | N3 | Supervisor de Turno de Almacén (Floor / Dock Supervisor) | [`log-wms-n3-floor-supervisor`](skills/log-wms-n3-floor-supervisor/SKILL.md) |
| Almacén / CEDIS | N4 | Operador de Cross-Docking | [`log-wms-n4-crossdock-operator`](skills/log-wms-n4-crossdock-operator/SKILL.md) |
| Almacén / CEDIS | N4 | Montacarguista / Reach Truck Operator | [`log-wms-n4-reach-truck-operator`](skills/log-wms-n4-reach-truck-operator/SKILL.md) |
| Almacén / CEDIS | N4 | Operador de Devoluciones (Reverse Logistics / RMA Processor) | [`log-wms-n4-reverse-logistics-tech`](skills/log-wms-n4-reverse-logistics-tech/SKILL.md) |
| Almacén / CEDIS | N5 | Cargador / Estibador de Piso | [`log-wms-n5-loader-stower`](skills/log-wms-n5-loader-stower/SKILL.md) |
| Almacén / CEDIS | N5 | Revisor de Mercancía / Checador | [`log-wms-n5-merchandise-checker`](skills/log-wms-n5-merchandise-checker/SKILL.md) |
| Almacén / CEDIS | N5 | Empacador (Packer) | [`log-wms-n5-packer`](skills/log-wms-n5-packer/SKILL.md) |
| Almacén / CEDIS | N5 | Surtidor (Picker) | [`log-wms-n5-picker`](skills/log-wms-n5-picker/SKILL.md) |
| Transporte y patio | N1 | Fleet & Transport Manager (Gerente de Transporte) | [`log-tms-n1-fleet-manager`](skills/log-tms-n1-fleet-manager/SKILL.md) |
| Transporte y patio | N2 | Jefe de Tráfico / Dispatcher Chief | [`log-tms-n2-dispatcher-chief`](skills/log-tms-n2-dispatcher-chief/SKILL.md) |
| Transporte y patio | N3 | Yard Supervisor / Dock Coordinator | [`log-tms-n3-yard-dock-coordinator`](skills/log-tms-n3-yard-dock-coordinator/SKILL.md) |
| Transporte y patio | N4 | Inspector C-TPAT / Seguridad e Inspección | [`log-tms-n4-ctpat-inspector`](skills/log-tms-n4-ctpat-inspector/SKILL.md) |
| Transporte y patio | N4 | Controlador de Patio / Yard Hostler | [`log-tms-n4-yard-hostler`](skills/log-tms-n4-yard-hostler/SKILL.md) |
| Transporte y patio | N5 | Chofer de Reparto / Operador de Unidad | [`log-tms-n5-delivery-driver`](skills/log-tms-n5-delivery-driver/SKILL.md) |
| Transporte y patio | N5 | Guardia de Acceso de Transporte / Gate Controller | [`log-tms-n5-gate-controller`](skills/log-tms-n5-gate-controller/SKILL.md) |
| Aduanas y comercio exterior | N1 | Customs & Foreign Trade Manager (Gerente de Comex) | [`log-cmx-n1-customs-manager`](skills/log-cmx-n1-customs-manager/SKILL.md) |
| Aduanas y comercio exterior | N2 | Jefe de Aduanas / Glosa / Clasificador Senior | [`log-cmx-n2-glosa-classifier-senior`](skills/log-cmx-n2-glosa-classifier-senior/SKILL.md) |
| Aduanas y comercio exterior | N3 | Supervisor de Despacho Aduanal y VUCEM | [`log-cmx-n3-vucem-supervisor`](skills/log-cmx-n3-vucem-supervisor/SKILL.md) |
| Aduanas y comercio exterior | N4 | Tramitador Aduanal / Ejecutor de Previo | [`log-cmx-n4-previo-inspector`](skills/log-cmx-n4-previo-inspector/SKILL.md) |
| Aduanas y comercio exterior | N5 | Etiquetador / Preparador NOM | [`log-cmx-n5-nom-labeler`](skills/log-cmx-n5-nom-labeler/SKILL.md) |
| Aduanas y comercio exterior | N5 | Verificador de Cumplimiento de NOMs | [`log-cmx-n5-nom-verifier`](skills/log-cmx-n5-nom-verifier/SKILL.md) |
| Inventario y slotting | N1 | Inventory Control Manager (Gerente de Inventarios) | [`log-inv-n1-inventory-manager`](skills/log-inv-n1-inventory-manager/SKILL.md) |
| Inventario y slotting | N2 | Jefe de Control de Inventarios y Slotting | [`log-inv-n2-slotting-chief`](skills/log-inv-n2-slotting-chief/SKILL.md) |
| Inventario y slotting | N3 | Supervisor de Conteos Cíclicos / Slotting | [`log-inv-n3-cycle-count-supervisor`](skills/log-inv-n3-cycle-count-supervisor/SKILL.md) |
| Inventario y slotting | N4 | Auxiliar de Inventarios / Contador Cíclico | [`log-inv-n4-cycle-counter`](skills/log-inv-n4-cycle-counter/SKILL.md) |
| Inventario y slotting | N4 | Analista de Ajustes / Conciliador ERP-WMS | [`log-inv-n4-erp-wms-reconciler`](skills/log-inv-n4-erp-wms-reconciler/SKILL.md) |
| Inventario y slotting | N5 | Auxiliar de Acomodo y Compactación | [`log-inv-n5-compaction-assistant`](skills/log-inv-n5-compaction-assistant/SKILL.md) |

Los niveles van de N0 (orquestación) a N5 (ejecución en piso). `crew.yaml` declara la jerarquía, los handoffs entre puestos y los casos que **siempre** escalan a una persona (bloqueo legal, castigo financiero mayor al que autoriza el gerente, emergencia de seguridad, conflicto entre ramas sin resolver).

## Cómo instalarlas

**Claude Code** (una, varias o todas):

```bash
git clone https://github.com/heroldoe-create/logistics-crew-skills
mkdir -p ~/.claude/skills
cp -r logistics-crew-skills/skills/log-wms-n5-picker ~/.claude/skills/        # una
cp -r logistics-crew-skills/skills/log-* ~/.claude/skills/                   # todas
```

Para un solo proyecto, cópialas a `.claude/skills/` dentro del repositorio en vez de `~/.claude/skills/`.

**Codex, Cursor, Antigravity y otros agentes que leen `SKILL.md`:** copia la carpeta `skills/<nombre>/` a la carpeta de skills de tu herramienta. Si tu herramienta solo lee `AGENTS.md`, pega ahí el contenido de la ficha que necesites.

**CrewAI u otro orquestador multiagente:** `crew.yaml` es un manifiesto declarativo. Cada agente apunta a su ficha con `skill_file` y trae su huella `skill_sha256`, para que tu adaptador cargue la ficha correcta y detecte si alguien la editó. El manifiesto no ejecuta nada ni guarda credenciales.

**Antes de usarlas, revísalas:**

```bash
python3 validar.py               # 30 skills · 0 fallas
python3 validar.py --autoprueba  # comprueba que el validador caza las fallas que debe
```

## Límites — léelos antes de usarlas en una operación real

- **Los umbrales son ejemplos de política, no normas.** «Escala si la diferencia supera 2 %» o «MXN 10,000» son puntos de partida razonables; cada empresa debe poner los suyos.
- **Las referencias legales se verificaron el 26 de octubre de 2026** (Ley Aduanera arts. 153 y 178, NOM-087-SCT-2-2017, Carta Porte 3.1, Anexos 22 y 24 de las Reglas Generales de Comercio Exterior, Anexo 4-B del T-MEC, NOM-050 y NOM-051, C-TPAT). La regulación cambia: confírmala en el DOF y con tu agente aduanal antes de decidir. **Esto no es asesoría legal ni fiscal.**
- **Un agente no sustituye la firma de una persona.** Ninguna ficha autoriza a un agente a firmar pedimentos, liberar mercancía regulada o ajustar inventario contable por su cuenta; las fichas dicen a quién se escala.
- **Origen:** las fichas se redactaron con asistentes de IA y después se auditaron (formato, coherencia entre puestos y datos legales). Si encuentras un error de piso, abre un issue: es la forma en que esto mejora.

## Licencia

Contenido bajo [CC BY 4.0](LICENSE): úsalo, adáptalo y compártelo, también con fines comerciales, citando a Heroldo Escobedo como autor.
