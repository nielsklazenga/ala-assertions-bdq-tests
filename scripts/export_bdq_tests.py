from pathlib import Path

import pandas as pd
import yaml

INPUT_DIR = Path("bdq_tests")
OUTPUT = Path("reports/bdq_tests.csv")

OUTPUT.parent.mkdir(parents=True, exist_ok=True)

rows = []

for path in sorted(INPUT_DIR.glob("*.yaml")):

    with open(path, encoding="utf-8") as f:
        record = yaml.safe_load(f)

    rows.append(
        {
            "id": record.get("id", ""),
            "label": record.get("label", ""),
            "type": record.get("type", ""),
            "dwc_class": ", ".join(
                record.get("dwc_class", [])
            ),
            "dwc_terms": ", ".join(
                record.get("dwc_terms", [])
            ),
            "description": record.get(
                "description",
                "",
            ),
        }
    )

df = pd.DataFrame(rows)

df = df.sort_values(
    ["type", "label"]
)

df.to_csv(
    OUTPUT,
    index=False,
)

print(f"Wrote {OUTPUT}")