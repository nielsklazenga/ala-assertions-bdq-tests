# ALA Assertions and BDQ Tests Comparison

This repository supports the review of the Atlas of Living Australia (ALA) Data Quality Assertions against the Biodiversity Data Quality (BDQ) Tests currently under public review by TDWG.

The aim is to understand:

- how ALA Assertions relate to BDQ Tests;
- where the two systems address similar data quality concepts;
- differences in modelling approach and granularity;
- opportunities for improving ALA Assertions;
- opportunities for future alignment with the BDQ Standard.

This repository is primarily a review and analysis tool. It is not intended to be an implementation of either framework.

---

## Repository Structure

```text
assertions/         ALA Assertion YAML files
bdq_tests/          BDQ Test YAML files

data/               Source data files

lib/                Shared Python functions

reports/            Generated reports and exports

scripts/            Report generation and data processing scripts
```

---

## Source Data

### ALA Assertions

The ALA Assertions are maintained as individual YAML files in:

```text
assertions/
```

Each assertion contains:

- identifier
- label
- Darwin Core classes acted upon
- Darwin Core terms acted upon
- implementation status
- recommendation
- implementation references
- review notes

The YAML files are the authoritative source for the ALA Assertions.

### BDQ Tests

The BDQ Tests are maintained as individual YAML files in:

```text
bdq_tests/
```

These files are generated from the BDQ test catalogue and contain:

- identifier
- label
- type
- description
- Darwin Core classes acted upon
- Darwin Core terms acted upon

The YAML files are the authoritative source for the BDQ Tests within this repository.

---

## Workflow

The repository follows a simple pattern:

```text
YAML
  ↓
Reports
  ↓
Review
```

YAML files are the primary source of information.

Reports and CSV exports are generated from the YAML files and should generally not be edited manually.

---

## Generated Reports

### Assertions by Class and Term

```text
reports/ala_by_class_and_term.md
```

Groups ALA Assertions by Darwin Core class and term.

### BDQ Tests by Class and Term

```text
reports/bdq_by_class_and_term.md
```

Groups BDQ Tests by Darwin Core class and term.

### Candidate Mappings

```text
reports/candidate_mappings.md
reports/candidate_mappings.csv
```

Lists potential relationships between ALA Assertions and BDQ Tests based on shared Darwin Core terms.

The CSV version is intended for further analysis in Excel, Power Query, or other tools.

### Missing Metadata

```text
reports/ala_missing_metadata.md
```

Identifies ALA Assertions that are missing Darwin Core class and/or term information.

### Observations

```text
reports/observations.md
```

Documents findings and conclusions arising from the comparison.

---

## CSV Exports

The repository provides CSV exports for use in tools such as Microsoft Excel and Power Query.

### ALA Assertions

```text
reports/ala_assertions.csv
```

### BDQ Tests

```text
reports/bdq_tests.csv
```

### Candidate Mappings

```text
reports/candidate_mappings.csv
```

A recommended workflow is:

```text
YAML
  ↓
CSV exports
  ↓
Power Query
  ↓
Excel workbook
```

This keeps the YAML files as the source of truth while allowing flexible analysis in Excel.

---

## Mapping Philosophy

The comparison distinguishes between:

### Associations

Assertions and tests that act on the same Darwin Core concepts.

Associations are used to identify potentially related concepts and to understand how the two systems are modelled.

### Mappings

Explicit semantic relationships between concepts.

Initial review suggests that many relationships are likely to be:

```text
skos:relatedMatch
```

rather than:

```text
skos:exactMatch
```

because:

- BDQ Tests are generally validation-oriented; and
- ALA Assertions are generally issue-oriented.

The comparison therefore focuses first on identifying associations and understanding modelling differences.

Formal mappings are expected to be developed after review findings have been evaluated and any resulting implementation changes have been made.

---

## Development

Most scripts can be run using:

```bash
uv run python -m scripts.<script_name>
```

Examples:

```bash
uv run python -m scripts.bdq_tests_yaml
uv run python -m scripts.ala_assertions_yaml
uv run python -m scripts.candidate_mappings
```

---

## Status

This repository is under active development as part of the review of the ALA Data Quality Assertions and the emerging BDQ Standard.

The focus is currently on:

- comparison of concepts;
- identification of overlaps and gaps;
- identification of composite assertions;
- assessment of future alignment opportunities.