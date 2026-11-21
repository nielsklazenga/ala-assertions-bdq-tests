import pandas as pd

INPUT = "data/bdqtest_term_versions.csv"
OUTPUT = "data/bdq_ala_mapping.csv"

df = pd.read_csv(INPUT)

out = pd.DataFrame({
    "subject_id": df["iri"],
    "subject_label": df["Label"],
    "subject_category": df["Type"],
    "object_id": "",
    "object_label": "",
    "predicate_id": "",
    "match_confidence": "",
    "creator_id": "",
    "mapping_justification": "",
    "comment": ""
})

out = (
    out
    .dropna(subset=["subject_id"])
    .sort_values(["subject_category", "subject_label"])
)

out.to_csv(OUTPUT, index=False)

print(f"Wrote {OUTPUT}")