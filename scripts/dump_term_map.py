from lib.indexing import build_term_map
from lib.yaml_utils import load_yaml_records

records = load_yaml_records("bdq_tests")

term_map = build_term_map(records)

for key in sorted(term_map):
    print(f"{key} -> {term_map[key]}")