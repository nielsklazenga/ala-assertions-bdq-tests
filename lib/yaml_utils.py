# lib/yaml_utils.py

from pathlib import Path
import yaml


def load_yaml_records(directory):
    records = []

    for path in sorted(Path(directory).glob("*.yaml")):
        with open(path, encoding="utf-8") as f:
            record = yaml.safe_load(f)

        record["_file"] = path
        records.append(record)

    return records