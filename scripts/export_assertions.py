from pathlib import Path

import pandas as pd
import yaml

INPUT_DIR = Path("assertions")
OUTPUT = Path("reports/ala_assertions.csv")

OUTPUT.parent.mkdir(parents=True, exist_ok=True)

rows = []

for path in sorted(INPUT_DIR.glob("*.yaml")):

    with open(path, encoding="utf-8") as f:
        record = yaml.safe_load(f)

    implemented_by = []

    if record.get("gbif"):
        implemented_by.append("GBIF")

    if record.get("ala"):
        implemented_by.append("ALA")

    rows.append(
        {
            "id": record.get("id", ""),
            "label": record.get("label", ""),
            "implemented_by": ", ".join(implemented_by),
            "status": record.get("status", ""),
            "recommendation": record.get("recommendation", ""),
            "dwc_class": ", ".join(
                record.get("dwc_class", [])
            ),
            "dwc_terms": ", ".join(
                record.get("dwc_terms", [])
            ),
            "wiki_page": record.get("wiki_page", ""),
        }
    )

df = pd.DataFrame(rows)

df = df.sort_values("label")

df.to_csv(
    OUTPUT,
    index=False,
)

print(f"Wrote {OUTPUT}")