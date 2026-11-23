from collections import defaultdict
from pathlib import Path

import yaml

INPUT_DIR = Path("assertions")
OUTPUT = Path("reports/ala_by_class_and_term.md")

OUTPUT.parent.mkdir(parents=True, exist_ok=True)

groups = defaultdict(lambda: defaultdict(list))

for path in sorted(INPUT_DIR.glob("*.yaml")):
    with open(path, encoding="utf-8") as f:
        record = yaml.safe_load(f)

    classes = record.get("dwc_class", []) or []
    terms = record.get("dwc_terms", [])
    
    if not terms:
        term_key = "No term specified"
    else:
        term_key = ",".join(terms)

    for dwc_class in classes:
        groups[dwc_class][term_key].append(record)

with open(OUTPUT, "w", encoding="utf-8") as out:
    out.write("# ALA Assertions by Darwin Core Class and Term\n\n")

    for dwc_class in sorted(groups):
        out.write(f"## {dwc_class}\n\n")

        for term in sorted(
            groups[dwc_class],
            key=lambda t: (
                "," in t,
                t.lower(),
            ),
        ):
            out.write(f"### {term}\n\n")
            out.write("| Assertion | Description |\n")
            out.write("|-----------|-------------|\n")

            assertions = sorted(
                groups[dwc_class][term],
                key=lambda r: r.get("label", ""),
            )

            for assertion in assertions:
                label = assertion.get("label", "")
                description = (
                    assertion.get("description", "")
                    .replace("\n", " ")
                    .replace("|", "\\|")
                )

                out.write(
                    f"| {label} | {description} |\n"
                )

            out.write("\n")

print(f"Wrote {OUTPUT}")