from pathlib import Path

import yaml

INPUT_DIR = Path("assertions")
OUTPUT = Path("reports/ala_missing_metadata.md")

def write_assertion_table(out, assertions):
    out.write("| Assertion | Status | Recommendation |\n")
    out.write("|-----------|--------|----------------|\n")

    table_row = "| {label} | {status} | {recommendation} |\n"

    for assertion in assertions:
        out.write(table_row.format(**assertion))

    out.write("\n")

missing_class = []
missing_terms = []
missing_both = []

for path in sorted(INPUT_DIR.glob("*.yaml")):
    with open(path, encoding="utf-8") as f:
        record = yaml.safe_load(f)

    assertion_status = record.get("status", path.stem)

    assertion = {
        "id": record.get("id", path.stem),
        "label": record.get("label", path.stem),
        "status": record.get("status", path.stem) or "",
        "recommendation": record.get("recommendation") or ""
    }

    classes = record.get("dwc_class", [])
    terms = record.get("dwc_terms", [])

    has_class = bool(classes)
    has_terms = bool(terms)

    if not has_class and not has_terms:
        missing_both.append(assertion)
    elif not has_class:
        missing_class.append(assertion)
    elif not has_terms:
        missing_terms.append(assertion)

with open(OUTPUT, "w", encoding="utf-8") as out:

    out.write("# ALA Assertions Missing Metadata\n\n")

    out.write(f"## Missing both class and terms ({len(missing_both)})\n\n")
    write_assertion_table(out, missing_both)

    out.write(f"## Missing dwc_class ({len(missing_class)})\n\n")
    write_assertion_table(out, missing_class)

    out.write(f"## Missing dwc_terms ({len(missing_terms)})\n\n")
    write_assertion_table(out, missing_terms)

print(f"Wrote {OUTPUT}")
print(
    f"{len(missing_both)} missing both, "
    f"{len(missing_class)} missing class, "
    f"{len(missing_terms)} missing terms"
)