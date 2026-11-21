from collections import defaultdict
from pathlib import Path

import yaml

INPUT_DIR = Path("mappings")
OUTPUT = Path("reports/bdq_by_class_and_term.md")

OUTPUT.parent.mkdir(parents=True, exist_ok=True)

groups = defaultdict(lambda: defaultdict(list))

for path in sorted(INPUT_DIR.glob("*.yaml")):
    with open(path, encoding="utf-8") as f:
        record = yaml.safe_load(f)

    classes = record.get("dwc_class", []) or ["Unclassified"]
    terms = record.get("dwc_terms", []) or ["No term specified"]

    for dwc_class in classes:
        for term in terms:
            groups[dwc_class][term].append(record)

with open(OUTPUT, "w", encoding="utf-8") as out:
    out.write("# BDQ Tests by Darwin Core Class and Term\n\n")

    for dwc_class in sorted(groups):
        out.write(f"## {dwc_class}\n\n")

        for term in sorted(groups[dwc_class]):
            out.write(f"### {term}\n\n")
            out.write("| Test | Description |\n")
            out.write("|------|-------------|\n")

            tests = sorted(
                groups[dwc_class][term],
                key=lambda r: r.get("label", ""),
            )

            for test in tests:
                label = test.get("label", "")
                description = (
                    test.get("description", "")
                    .replace("\n", " ")
                    .replace("|", "\\|")
                )

                out.write(
                    f"| {label} | {description} |\n"
                )

            out.write("\n")

print(f"Wrote {OUTPUT}")