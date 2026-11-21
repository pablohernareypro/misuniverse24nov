"""Comprueba el calendario, las metas, las candidatas y los enlaces del relevo."""

import csv
import json
import re
from collections import Counter
from datetime import date, timedelta
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


def read_csv(name):
    with (ROOT / "seguimiento" / name).open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream))


def check(condition, message):
    if not condition:
        raise SystemExit(message)


def main():
    goals = json.loads((ROOT / "campana/objetivos.json").read_text(encoding="utf-8"))
    posts = read_csv("publicaciones.csv")
    cast = read_csv("candidatas.csv")
    first = date.fromisoformat(goals["fecha_inicio"])
    last = date.fromisoformat(goals["fecha_final"])
    days = (last - first).days + 1
    expected = {
        (first + timedelta(days=offset)).isoformat(): goals["videos_por_dia"]
        for offset in range(days)
    }
    check(Counter(row["dia_previsto"] for row in posts) == expected, "Revisar la distribución diaria.")
    check(all(int(row["meta_vistas"]) == goals["vistas_minimas_por_video"] for row in posts), "Revisar la meta por video.")
    check([row["banda"] for row in cast] == goals["candidatas"], "Revisar el elenco de la votación.")
    ids = [row["pieza"] for row in posts]
    check(len(ids) == len(set(ids)), "Hay números de pieza repetidos.")
    check(all(row["pieza_presentacion"] in ids for row in cast), "Hay una presentación sin pieza.")
    plan = (ROOT / "campana/plan-20-tiktoks.md").read_text(encoding="utf-8")
    check(re.findall(r"^\| (\d\d) \|", plan, re.MULTILINE) == ids, "El plan y el registro de publicaciones difieren.")
    for file in ROOT.rglob("*.md"):
        if ".git" in file.parts:
            continue
        for link in re.findall(r"\[[^\]\n]+\]\(([^)\s]+)\)", file.read_text(encoding="utf-8")):
            target = urlsplit(link)
            if target.scheme or not target.path:
                continue
            check((file.parent / unquote(target.path)).exists(), f"Enlace roto en {file.relative_to(ROOT)}: {link}")
    for skill in (ROOT / ".agents/skills").glob("*/SKILL.md"):
        content = skill.read_text(encoding="utf-8")
        check(content.startswith(f"---\nname: {skill.parent.name}\ndescription: "), f"Revisar los metadatos de {skill}")
    total = len(posts) * goals["vistas_minimas_por_video"]
    print(f"Plan comprobado: {len(posts)} piezas, {len(cast)} candidatas y {total:,} vistas mínimas acumuladas.")


if __name__ == "__main__":
    main()
