from pathlib import Path

import pandas as pd
import yaml

INPUT = "data/bdqtest_term_versions.csv"
OUTPUT_DIR = Path("mappings")

Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)

df = pd.read_csv(INPUT)


def split_terms(value):
    if pd.isna(value):
        return []

    return [
        v.strip()
        for v in str(value).split("|")
        if v.strip()
    ]


for _, row in (
    df.dropna(subset=["iri"])
      .sort_values(["Type", "Label"])
      .iterrows()
):
    record = {
        "id": row["iri"],
        "label": row["Label"],
        "type": row["Type"],
        "description": row.get("Description", ""),
        "dwc_class": split_terms(row.get("IE Class")),
        "dwc_terms": split_terms(
            row.get("InformationElement:ActedUpon")
        ),
        "mapping": {
            "object_id": "",
            "object_label": "",
            "predicate_id": "",
            "match_confidence": "",
            "mapping_justification": "",
            "comment": "",
        },
    }

    filename = (
        row["Label"]
        .replace("/", "_")
        .replace(" ", "_")
    )

    output_file = Path(OUTPUT_DIR) / f"{filename}.yaml"

    with output_file.open("w", encoding="utf-8") as f:
        yaml.safe_dump(
            record,
            f,
            sort_keys=False,
            allow_unicode=True,
            width=1000,
        )

print(f"Wrote {len(df.dropna(subset=['iri']))} YAML files to {OUTPUT_DIR}")