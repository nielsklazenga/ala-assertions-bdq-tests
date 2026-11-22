# lib/indexing.py

from collections import defaultdict
from pathlib import Path

import yaml


def build_term_index(directory):
    index = defaultdict(list)

    for path in sorted(Path(directory).glob("*.yaml")):
        with open(path, encoding="utf-8") as f:
            record = yaml.safe_load(f)

        classes = record.get("dwc_class", [])
        terms = record.get("dwc_terms", [])

        if not classes or not terms:
            continue

        for dwc_class in classes:
            for term in terms:
                index[(dwc_class, term)].append(record)

    return index