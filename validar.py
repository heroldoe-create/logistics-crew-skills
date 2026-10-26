#!/usr/bin/env python3
"""validar.py — revisa que el crew esté completo y coherente antes de publicarlo o instalarlo.

    python3 validar.py               revisa skills/ y crew.yaml; sale 1 si algo falla
    python3 validar.py --autoprueba  planta fallas en una copia temporal y comprueba que las caza

Qué revisa, por skill: que exista skills/<nombre>/SKILL.md, que su encabezado YAML tenga `name` igual a la carpeta y una
`description` de 1 024 caracteres o menos (el límite del estándar de Agent Skills), que tenga las seis secciones del método
(ID y Jerarquía, Gatillo, Inputs, Árbol de Decisión, Prohibiciones Duras, Entregable de Salida), que cada puesto que nombra
como jefe o handoff exista, y que no queden restos de exportación (\\`, fórmulas LaTeX, tablas pegadas como CSV).
En crew.yaml: que cada `skill_file` apunte a un archivo que existe, que su `skill_sha256` sea la huella real del archivo y
que los 30 puestos estén declarados. Sin dependencias fuera de la biblioteca estándar.
"""
import hashlib, os, re, shutil, sys, tempfile

AQUI = os.path.dirname(os.path.abspath(__file__))
SECCIONES = ("ID y Jerarquía", "Gatillo", "Inputs", "Árbol de Decisión", "Prohibiciones Duras", "Entregable de Salida")
# el orquestador N0 usa sus propios títulos (misión, ruteo, handoffs maestros): se le piden los equivalentes
SECCIONES_N0 = ("jerarquía", "Gatillos", "Inputs", "Árbol de decisión", "Prohibiciones duras", "Entregables de salida")
RESTOS = (("escape \\`", r"\\`"), ("fórmula LaTeX", r"\\\\(le|ge|rightarrow)|\\%|\$\\"), ("tabla CSV", r"^Condición \(SI\),"),
          ("anglicismo", r"\bstrictly\b"))


def encabezado(texto):
    m = re.match(r"---\n(.*?)\n---\n", texto, re.S)
    if not m:
        return None
    campos, clave = {}, None
    for linea in m.group(1).splitlines():
        if re.match(r"^[a-z_]+:", linea):
            clave, _, valor = linea.partition(":")
            campos[clave] = valor.strip()
        elif clave and linea.startswith("  ") and clave == "description":
            campos[clave] = (campos[clave].lstrip(">|").strip() + " " + linea.strip()).strip()
    campos["_crudo"] = m.group(1)
    return campos


def revisar(raiz):
    fallas = []
    base = os.path.join(raiz, "skills")
    nombres = sorted(os.listdir(base)) if os.path.isdir(base) else []
    if not nombres:
        return ["no hay skills/"]
    for n in nombres:
        p = os.path.join(base, n, "SKILL.md")
        if not os.path.isfile(p):
            fallas.append(f"{n}: falta SKILL.md"); continue
        t = open(p, encoding="utf-8").read()
        e = encabezado(t)
        if not e:
            fallas.append(f"{n}: sin encabezado YAML"); continue
        if e.get("name") != n:
            fallas.append(f"{n}: name «{e.get('name')}» no es el de la carpeta")
        if not e.get("description") or len(e["description"]) > 1024:
            fallas.append(f"{n}: description vacía o de más de 1 024 caracteres")
        for s in (SECCIONES_N0 if "-n0-" in n else SECCIONES):
            if s not in t:
                fallas.append(f"{n}: falta la sección «{s}»")
        for ref in set(re.findall(r"log-[a-z]+-n[0-5]-[a-z0-9-]+|log-n0-[a-z-]+", e["_crudo"])):
            if ref not in nombres:
                fallas.append(f"{n}: nombra al puesto {ref}, que no existe")
        for etiqueta, patron in RESTOS:
            if re.search(patron, t, re.M):
                fallas.append(f"{n}: resto de exportación ({etiqueta})")
    c = os.path.join(raiz, "crew.yaml")
    if not os.path.isfile(c):
        fallas.append("falta crew.yaml")
    else:
        y = open(c, encoding="utf-8").read()
        rutas = re.findall(r"skill_file:\s*['\"]?([^'\"\s]+)", y)
        for r in rutas:
            if not os.path.isfile(os.path.join(raiz, r)):
                fallas.append(f"crew.yaml: skill_file {r} no existe")
        for r, h in re.findall(r"skill_file: (\S+)\n(?:.*\n){0,12}?\s*skill_sha256: ([0-9a-f]{64})", y):
            p = os.path.join(raiz, r)
            if os.path.isfile(p) and hashlib.sha256(open(p, "rb").read()).hexdigest() != h:
                fallas.append(f"crew.yaml: la huella de {r} no es la del archivo (se editó sin recalcular)")
        faltan = [n for n in nombres if f"skills/{n}/SKILL.md" not in rutas]
        if faltan:
            fallas.append(f"crew.yaml: no declara {faltan}")
    return fallas


def autoprueba():
    casos = []
    with tempfile.TemporaryDirectory() as d:
        copia = os.path.join(d, "crew")
        shutil.copytree(AQUI, copia, ignore=shutil.ignore_patterns(".git", "__pycache__"))
        casos.append(("el crew tal como está pasa", revisar(copia) == []))
        uno = sorted(os.listdir(os.path.join(copia, "skills")))[1]
        p = os.path.join(copia, "skills", uno, "SKILL.md")
        bueno = open(p, encoding="utf-8").read()
        plantadas = (
            ("name distinto a la carpeta", bueno.replace(f"name: {uno}", "name: otro-nombre", 1), "no es el de la carpeta"),
            ("sección borrada", bueno.replace("Prohibiciones Duras", "Reglas"), "Prohibiciones Duras"),
            ("handoff a un puesto inexistente", bueno.replace("---\n\n", "  extra: \"log-wms-n4-fantasma\"\n---\n\n", 1), "no existe"),
            ("fórmula LaTeX olvidada", bueno + "\n- KPI: $\\\\ge 99.5\\\\%$\n", "LaTeX"),
            ("tabla CSV pegada", bueno + "\nCondición (SI),Acción (ENTONCES),Nivel\n", "CSV"),
            ("skill editada sin recalcular su huella", bueno + "\n", "huella"),
        )
        for nombre, texto, espera in plantadas:
            open(p, "w", encoding="utf-8").write(texto)
            casos.append((f"caza: {nombre}", any(espera in f for f in revisar(copia))))
        open(p, "w", encoding="utf-8").write(bueno)
        y = os.path.join(copia, "crew.yaml")
        open(y, "a", encoding="utf-8").write("\n  - skill_file: skills/no-existe/SKILL.md\n")
        casos.append(("caza: crew.yaml apunta a un archivo que no existe", any("no-existe" in f for f in revisar(copia))))
    for n, ok in casos:
        print(("  OK   " if ok else "  MAL  ") + n)
    return 0 if all(ok for _, ok in casos) else 1


if __name__ == "__main__":
    if "--autoprueba" in sys.argv:
        sys.exit(autoprueba())
    f = revisar(AQUI)
    for x in f:
        print("  ✗ " + x)
    print(f"{len(os.listdir(os.path.join(AQUI, 'skills')))} skills · {len(f)} fallas")
    sys.exit(1 if f else 0)
