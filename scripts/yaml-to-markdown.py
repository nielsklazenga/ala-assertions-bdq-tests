from pathlib import Path

import yaml


INPUT_DIR = Path("assertions")
OUTPUT_FILE = Path("reports/ala_assertions.md")


def format_value(value):
    if value is None:
        return ""

    if isinstance(value, list):
        return "<br>".join(str(v) for v in value)

    return str(value)


files = sorted(INPUT_DIR.glob("*.yaml"))

with open(OUTPUT_FILE, "w", encoding="utf-8") as out:

    out.write("# ALA Data Quality Assertions\n\n")

    # out.write("## Table of Contents\n\n")

    # for file in files:
    #     with open(file, encoding="utf-8") as f:
    #         data = yaml.safe_load(f)

    #     identifier = data.get("id", file.stem)

    #     anchor = identifier.lower().replace("_", "-")

    #     out.write(
    #         f"- [{identifier}](#{anchor})\n"
    #     )

    # out.write("\n---\n\n")

    for file in files:

        with open(file, encoding="utf-8") as f:
            data = yaml.safe_load(f)

        identifier = data.get("id", file.stem)

        out.write(f"## {identifier}\n\n")

        out.write("| Field | Value |\n")
        out.write("|-------|-------|\n")

        metadata_fields = [
            ("Status", data.get("status")),
            ("Count", data.get("count")),
            ("Recommendation", data.get("recommendation")),
            ("DwC Class", data.get("dwc_class")),
            ("DwC Terms", data.get("dwc_terms")),
            ("Wiki Page", data.get("wiki_page")),
            ("GitHub Search", data.get("github_search")),
        ]

        for label, value in metadata_fields:

            if value in (None, "", [], {}):
                continue

            out.write(
                f"| {label} | {format_value(value)} |\n"
            )

        out.write("\n")

        gbif = data.get("gbif", {})

        if gbif:

            out.write("### GBIF\n\n")

            for key in [
                "class_asserted_in",
                "method_asserted_by",
                "assertion_logic",
            ]:

                value = gbif.get(key)

                if value:

                    out.write(
                        f"**{key.replace('_', ' ').title()}**\\\n"
                    )
                    out.write(f"{value}\n\n")

        ala = data.get("ala", {})

        if ala:

            out.write("### ALA\n\n")

            for key in [
                "class_asserted_in",
                "method_asserted_by",
                "assertion_logic",
            ]:

                value = ala.get(key)

                if value:

                    out.write(
                        f"**{key.replace('_', ' ').title()}**\\\n"
                    )
                    out.write(f"{value}\n\n")

        actions = data.get("actions")

        if actions:

            out.write("### Actions\n\n")
            out.write(f"{actions}\n\n")

        out.write("---\n\n")

print(f"Wrote {OUTPUT_FILE}")