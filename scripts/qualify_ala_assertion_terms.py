from pathlib import Path

import yaml

from lib.indexing import build_term_map, qualify_terms
from lib.yaml_utils import load_yaml_records

BDQ_DIR = Path("bdq_tests")
ALA_DIR = Path("assertions")

# Build local-name -> fully-qualified term map
bdq_records = load_yaml_records(BDQ_DIR)
term_map = build_term_map(bdq_records)

updated = 0
unknown_terms = set()

for path in sorted(ALA_DIR.glob("*.yaml")):

    with open(path, encoding="utf-8") as f:
        record = yaml.safe_load(f)

    changed = False

    for field in ("dwc_class", "dwc_terms"):

        values = record.get(field)

        if not values:
            continue

        qualified = qualify_terms(values, term_map)

        if qualified != values:
            record[field] = qualified
            changed = True

        for term in values:
            if ":" not in term and term not in term_map:
                unknown_terms.add(term)

    if changed:
        with open(path, "w", encoding="utf-8") as f:
            yaml.safe_dump(
                record,
                f,
                sort_keys=False,
                allow_unicode=True,
                width=1000,
            )

        updated += 1

print(f"Updated {updated} assertion files")

if unknown_terms:
    print("\nUnmapped terms:")
    for term in sorted(unknown_terms):
        print(f"  {term}")