from pathlib import Path
import sys

from lib.indexing import build_term_index

ALA_DIR = "assertions"
BDQ_DIR = "bdq_tests"

OUTPUT = Path("reports/association_candidates.md")
OUTPUT.parent.mkdir(parents=True, exist_ok=True)

ala_index = build_term_index(ALA_DIR)
bdq_index = build_term_index(BDQ_DIR)

all_keys = sorted(
    set(ala_index.keys()) | set(bdq_index.keys())
)

with open(OUTPUT, "w", encoding="utf-8") as out:

    out.write("# Candidate Associations\n\n")
    out.write(
        "Grouped by Darwin Core class and term acted on.\n\n"
    )

    current_class = None

    for dwc_class, term in all_keys:

        if dwc_class != current_class:
            current_class = dwc_class
            out.write(f"\n# {dwc_class}\n\n")

        ala_assertions = ala_index.get((dwc_class, term), [])
        bdq_tests = bdq_index.get((dwc_class, term), [])

        out.write(f"## {term}\n\n")

        out.write(
            f"ALA assertions: {len(ala_assertions)}  \n"
        )
        out.write(
            f"BDQ tests: {len(bdq_tests)}\n\n"
        )

        out.write("### ALA Assertions\n\n")

        if ala_assertions:
            out.write("| Assertion | Status | Recommendation |\n")
            out.write("|-----------|--------|----------------|\n")

            for assertion in sorted(
                ala_assertions,
                key=lambda r: r.get("label", "")
            ):
                out.write(
                    "| {label} | {status} | {recommendation} |\n".format(
                        label=assertion.get("label", ""),
                        status=assertion.get("status", ""),
                        recommendation=assertion.get("recommendation", ""),
                    )
                )
        else:
            out.write("_None_\n")

        out.write("\n")

        out.write("### BDQ Tests\n\n")

        if bdq_tests:
            out.write("| Test | Description |\n")
            out.write("|------|-------------|\n")

            for test in sorted(
                bdq_tests,
                key=lambda r: r.get("label", "")
            ):
                description = (
                    test.get("description", "")
                    .replace("\n", " ")
                    .replace("|", "\\|")
                )

                out.write(
                    "| {label} | {description} |\n".format(
                        label=test.get("label", ""),
                        description=description,
                    )
                )
        else:
            out.write("_None_\n")

        out.write("\n---\n\n")

print(f"Wrote {OUTPUT}")
