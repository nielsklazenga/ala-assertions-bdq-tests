from collections import Counter
from pathlib import Path

import yaml

from lib.indexing import normalize_term

ALA_DIR = Path("assertions")
BDQ_DIR = Path("bdq_tests")

OUTPUT = Path("reports/vocabulary_comparison.md")
OUTPUT.parent.mkdir(parents=True, exist_ok=True)


def collect_vocab(directory):
    classes = Counter()
    terms = Counter()

    for path in sorted(directory.glob("*.yaml")):
        with open(path, encoding="utf-8") as f:
            record = yaml.safe_load(f)

        for cls in record.get("dwc_class", []):
            classes[normalize_term(cls)] += 1

        for term in record.get("dwc_terms", []):
            terms[normalize_term(term)] += 1

    return classes, terms


ala_classes, ala_terms = collect_vocab(ALA_DIR)
bdq_classes, bdq_terms = collect_vocab(BDQ_DIR)


def write_table(out, values1, values2, heading1, heading2):
    out.write(f"| Value | {heading1} | {heading2} |\n")
    out.write("|-------|-----|-----|\n")

    all_values = sorted(set(values1) | set(values2))

    for value in all_values:
        out.write(
            f"| {value} "
            f"| {values1.get(value, 0)} "
            f"| {values2.get(value, 0)} |\n"
        )

    out.write("\n")


with open(OUTPUT, "w", encoding="utf-8") as out:

    out.write("# Vocabulary Comparison\n\n")

    out.write("## Darwin Core Classes\n\n")
    write_table(
        out,
        ala_classes,
        bdq_classes,
        "ALA",
        "BDQ",
    )

    out.write("## Darwin Core Terms\n\n")
    write_table(
        out,
        ala_terms,
        bdq_terms,
        "ALA",
        "BDQ",
    )

print(f"Wrote {OUTPUT}")