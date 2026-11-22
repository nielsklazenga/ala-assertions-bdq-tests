from collections import defaultdict
from pathlib import Path

from lib.indexing import build_term_index


ALA_DIR = "assertions"
BDQ_DIR = "bdq_tests"

OUTPUT = Path("reports/candidate_mappings.md")
OUTPUT.parent.mkdir(parents=True, exist_ok=True)


def display_terms(terms):
    return ", ".join(
        term.split(":")[-1]
        for term in sorted(terms)
    )


ala_index = build_term_index(ALA_DIR)
bdq_index = build_term_index(BDQ_DIR)

pairs = {}

shared_keys = set(ala_index.keys()) & set(bdq_index.keys())

for (dwc_class, term) in sorted(shared_keys):

    ala_assertions = ala_index[(dwc_class, term)]
    bdq_tests = bdq_index[(dwc_class, term)]

    for ala in ala_assertions:
        for bdq in bdq_tests:

            pair_key = (
                ala["id"],
                bdq["id"],
            )

            if pair_key not in pairs:

                ala_terms = set(
                    ala.get("dwc_terms", [])
                )

                bdq_terms = set(
                    bdq.get("dwc_terms", [])
                )

                pairs[pair_key] = {
                    "ala_label": ala["label"],
                    "bdq_label": bdq["label"],
                    "ala_terms": ala_terms,
                    "bdq_terms": bdq_terms,
                    "bdq_classes": set(
                        bdq.get("dwc_class", [])
                    ),
                    "connecting_terms": set(),
                }

            pairs[pair_key]["connecting_terms"].add(term)


for pair in pairs.values():

    pair["ala_only_terms"] = (
        pair["ala_terms"]
        - pair["connecting_terms"]
    )

    pair["bdq_only_terms"] = (
        pair["bdq_terms"]
        - pair["connecting_terms"]
    )


grouped = defaultdict(list)

for pair in pairs.values():

    for bdq_class in pair["bdq_classes"]:
        grouped[bdq_class].append(pair)


with open(OUTPUT, "w", encoding="utf-8") as out:

    out.write("# Candidate Mappings\n\n")

    out.write(
        "Potential ALA Assertion ↔ BDQ Test associations "
        "grouped by BDQ class and based on shared Darwin Core terms.\n\n"
    )

    for bdq_class in sorted(grouped):

        out.write(f"## {bdq_class}\n\n")

        out.write(
            "| ALA Assertion | BDQ Test | "
            "Connecting Terms | "
            "ALA-only Terms | "
            "BDQ-only Terms |\n"
        )

        out.write(
            "|---------------|----------|"
            "------------------|"
            "----------------|"
            "----------------|\n"
        )

        class_pairs = sorted(
            grouped[bdq_class],
            key=lambda p: (
                len(p["connecting_terms"]),
                p["ala_label"],
                p["bdq_label"],
            ),
            reverse=True,
        )

        for pair in class_pairs:

            out.write(
                "| {ala} | {bdq} | "
                "{connecting} | "
                "{ala_only} | "
                "{bdq_only} |\n".format(
                    ala=pair["ala_label"],
                    bdq=pair["bdq_label"],
                    connecting=display_terms(
                        pair["connecting_terms"]
                    ),
                    ala_only=display_terms(
                        pair["ala_only_terms"]
                    ),
                    bdq_only=display_terms(
                        pair["bdq_only_terms"]
                    ),
                )
            )

        out.write("\n")

print(f"Wrote {OUTPUT}")

import pandas as pd

rows = []

for bdq_class in sorted(grouped):

    class_pairs = sorted(
        grouped[bdq_class],
        key=lambda p: (
            p["ala_label"],
            p["bdq_label"],
        ),
    )

    for pair in class_pairs:

        rows.append(
            {
                "BDQ Class": bdq_class,
                "ALA Assertion": pair["ala_label"],
                "BDQ Test": pair["bdq_label"],
                "Connecting Terms": display_terms(
                    pair["connecting_terms"]
                ),
                "ALA-only Terms": display_terms(
                    pair["ala_only_terms"]
                ),
                "BDQ-only Terms": display_terms(
                    pair["bdq_only_terms"]
                ),
            }
        )

df = pd.DataFrame(rows)

csv_file = "reports/candidate_mappings.csv"

df.to_csv(
    csv_file,
    index=False,
)

print("Wrote ", csv_file)