"""Vérifie que les fichiers YAML sont valides et que les manifestes Kubernetes ont les champs essentiels."""
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
errors = []

for path in sorted([*ROOT.glob("*.yml"), *ROOT.glob("k8s/*.yaml"), *ROOT.glob(".github/workflows/*.yml")]):
    try:
        docs = [d for d in yaml.safe_load_all(path.read_text()) if d is not None]
    except yaml.YAMLError as e:
        errors.append(f"{path.relative_to(ROOT)} : YAML invalide ({e})")
        continue
    if path.parent.name == "k8s":
        for d in docs:
            for key in ("apiVersion", "kind", "metadata"):
                if key not in d:
                    errors.append(f"{path.relative_to(ROOT)} : champ '{key}' manquant")
    print(f"OK  {path.relative_to(ROOT)}")

if errors:
    print("\n".join(errors), file=sys.stderr)
    sys.exit(1)
