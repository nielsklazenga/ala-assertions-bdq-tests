from pathlib import Path

import pandas as pd
import yaml


INPUT_FILE = "data/ala-data-quality-assertions-code-review.xlsx"
OUTPUT_DIR = Path("assertions")


def split_list(value):
    """Convert comma-separated values into a list."""
    if pd.isna(value):
        return []

    values = [
        v.strip()
        for v in str(value).split(",")
        if v.strip()
    ]

    return values


def clean(value):
    """Convert NaN to None and strip whitespace."""
    if pd.isna(value):
        return None

    value = str(value).strip()

    return value if value else None


OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_excel(
    INPUT_FILE,
    sheet_name="Data quality Wiki",
    engine="openpyxl"
)

for _, row in df.iterrows():

    issue = clean(row["Issue"])

    if not issue:
        continue

    data = {
        "id": issue,

        "dwc_class": split_list(row["DwC class"]),
        "dwc_terms": split_list(row["DwC term"]),

        "wiki_page": clean(row["Wiki Page"]),
        "github_search": clean(row["GitHub Search"]),

        "count": clean(row["Count"]),
        "status": clean(row["Status"]),

        "gbif": {
            "class_asserted_in": clean(row["GBIF Class asserted in"]),
            "method_asserted_by": clean(row["GBIF Method asserted by"]),
            "assertion_logic": clean(row["GBIF Assertion logic"]),
        },

        "ala": {
            "class_asserted_in": clean(row["LA Class asserted in"]),
            "method_asserted_by": clean(row["LA Method asserted by"]),
            "assertion_logic": clean(row["LA Assertion logic"]),
        },

        "recommendation": clean(row["Keep/Remove"]),
        "actions": clean(row["Actions to be taken"]),
    }

    # Remove empty values recursively
    def prune(obj):
        if isinstance(obj, dict):
            obj = {
                k: prune(v)
                for k, v in obj.items()
            }
            return {
                k: v
                for k, v in obj.items()
                if v not in (
                    None,
                    "",
                    [],
                    {}
                )
            }

        if isinstance(obj, list):
            return [
                prune(v)
                for v in obj
                if v not in (
                    None,
                    "",
                    []
                )
            ]

        return obj

    data = prune(data)

    output_file = OUTPUT_DIR / f"{issue}.yaml"

    with open(output_file, "w", encoding="utf-8") as f:
        yaml.dump(
            data,
            f,
            allow_unicode=True,
            sort_keys=False,
            default_flow_style=False
        )

    print(output_file)

print("Done.")