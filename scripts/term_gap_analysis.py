from collections import defaultdict
from pathlib import Path

import pandas as pd
import yaml

ASSERTIONS_DIR = Path("assertions")
BDQ_TESTS_DIR = Path("bdq_tests")

OUTPUT_MD = Path("reports/term_coverage.md")
OUTPUT_CSV = Path("reports/term_coverage.csv")

OUTPUT_MD.parent.mkdir(parents=True, exist_ok=True)


def normalize_term(term):
    """Normalize terms for matching and reporting."""
    if ":" in term:
        prefix, _ = term.split(":", 1)

        # Ignore BDQ namespace terms for now
        if prefix.startswith("bdq"):
            return None

        return term

    # Assume unqualified terms are Darwin Core terms
    return f"dwc:{term}"

term_data = defaultdict(
    lambda: {
        "class": "",
        "assertions": set(),
        "tests": set(),
    }
)


#
# Load assertions
#
for path in sorted(ASSERTIONS_DIR.glob("*.y*ml")):
    with open(path, encoding="utf-8") as f:
        assertion = yaml.safe_load(f)

    assertion_id = (
        assertion.get("label")
        or path.stem
    )

    dwc_class = assertion.get("dwc_class", "")

    if isinstance(dwc_class, list):
        dwc_class = dwc_class[0] if dwc_class else ""

    terms = assertion.get("dwc_terms", assertion.get("terms", []))
    

    for term in terms:
        term = normalize_term(term)

        if not term:
            continue

        term_data[term]["assertions"].add(assertion_id)

        if dwc_class and not term_data[term]["class"]:
            term_data[term]["class"] = dwc_class


#
# Load BDQ tests
#
for path in sorted(BDQ_TESTS_DIR.glob("*.y*ml")):
    with open(path, encoding="utf-8") as f:
        test = yaml.safe_load(f)

    test_id = (
        test.get("label")
        or path.stem
    )

    bdq_class = test.get("dwc_class", "")

    if isinstance(bdq_class, list):
        bdq_class = bdq_class[0] if bdq_class else ""

    for term in test.get("dwc_terms", []):
        term = normalize_term(term)

        if not term:
            continue

        term_data[term]["tests"].add(test_id)

        if bdq_class and not term_data[term]["class"]:
            term_data[term]["class"] = bdq_class


#
# Build dataframe
#
rows = []

for term, info in sorted(term_data.items()):
    assertions = sorted(info["assertions"])
    tests = sorted(info["tests"])

    if assertions and tests:
        coverage = "Both"
    elif assertions:
        coverage = "Assertion Only"
    else:
        coverage = "BDQ Only"

    rows.append(
        {
            "Class": info["class"],
            "Term": term,
            "Coverage": coverage,
            "ALA Assertions": "; ".join(assertions),
            "BDQ Tests": "; ".join(tests),
        }
    )

df = pd.DataFrame(rows)

df = df.sort_values(
    ["Class", "Coverage", "Term"],
    na_position="last",
)

#
# Save CSV
#
df.to_csv(OUTPUT_CSV, index=False)

#
# Save Markdown
#
with open(OUTPUT_MD, "w", encoding="utf-8") as f:
    f.write("# Term Coverage Analysis\n\n")
    f.write(
        "Comparison of Darwin Core terms used by "
        "ALA Assertions and BDQ Tests.\n\n"
    )

    classes = sorted(
        c for c in df["Class"].dropna().unique()
        if str(c).strip()
    )

    for cls in classes:
        f.write(f"## {cls}\n\n")

        subset = (
            df[df["Class"] == cls]
            .sort_values(["Term"])
        )

        if not subset.empty:
            f.write("| Class | Term | Coverage | ALA Assertions | BDQ Tests |\n")
            f.write("|-------|------|----------|----------------|-----------|\n")

            for _, row in subset.iterrows():
                f.write(
                    f"| {row['Class']} "
                    f"| {row['Term']} "
                    f"| {row['Coverage']} "
                    f"| {row['ALA Assertions']} "
                    f"| {row['BDQ Tests']} |\n"
                )

            f.write("\n")