# Observations from the ALA Assertions and BDQ Tests Comparison

## Validation-Oriented vs Issue-Oriented Modelling

One of the clearest patterns emerging from the review is that the BDQ Tests and ALA Assertions generally operate at different points in the data quality workflow.

BDQ Tests tend to describe expected conditions or validation rules:

- `VALIDATION_COORDINATES_NOTEMPTY`
- `VALIDATION_BASISOFRECORD_STANDARD`
- `VALIDATION_TAXON_NOTEMPTY`

ALA Assertions tend to describe data quality issues identified after validation:

- `ASSERTION_COORDINATES_EMPTY`
- `ASSERTION_BASISOFRECORD_NOTSTANDARD`
- `ASSERTION_TAXON_EMPTY`

While these concepts are closely related, they are not usually equivalent. In many cases the ALA Assertion represents the condition detected when a BDQ Validation fails.

This suggests that many eventual mappings will be better represented as `skos:relatedMatch` rather than `skos:exactMatch`.

It also suggests that future alignment between the ALA Assertions and the BDQ Standard could benefit from adopting a common naming pattern while retaining the distinction between validations and assertions.

Examples:

| BDQ Test | Potential Assertion Pattern |
|-----------|-----------|
| `VALIDATION_COORDINATES_NOTEMPTY` | `ASSERTION_COORDINATES_EMPTY` |
| `VALIDATION_BASISOFRECORD_STANDARD` | `ASSERTION_BASISOFRECORD_NOTSTANDARD` |
| `VALIDATION_TAXON_NOTEMPTY` | `ASSERTION_TAXON_EMPTY` |

No renaming is proposed at this stage. Any consideration of naming alignment should occur only after the BDQ Standard has been ratified.

---

## Associations Are Often More Informative Than Mappings

The review process generated candidate associations by identifying ALA Assertions and BDQ Tests that act on the same Darwin Core classes and terms.

This has proven more informative than attempting to create semantic mappings directly.

The candidate association table answers the question:

> Which ALA Assertions and BDQ Tests intersect on the same Darwin Core concepts?

whereas a mapping attempts to answer:

> What is the semantic relationship between these concepts?

The association table therefore acts as a discovery tool that exposes how the two systems are modelled, rather than immediately forcing a mapping decision.

In many cases the associations reveal potential relationships that would not be obvious from labels alone.

---

## Composite Assertions and Mixed Concepts

The review has reinforced an issue that had already been identified in the ALA Assertions: some assertions appear to combine multiple concepts or validation outcomes into a single assertion.

For example, `COUNTRY_COORDINATE_MISMATCH` intersects with several BDQ validations, including:

- `VALIDATION_COUNTRY_FOUND`
- `VALIDATION_COUNTRYCOUNTRYCODE_CONSISTENT`
- `VALIDATION_COORDINATESCOUNTRYCODE_CONSISTENT`
- `VALIDATION_COORDINATES_NOTZERO`

The assertion may therefore depend on several independent validation outcomes rather than corresponding to a single validation rule.

This suggests that some ALA Assertions (and inherited GBIF assertions) may represent compound data quality concepts that could potentially be decomposed into more granular assertions.

The association analysis is particularly useful for identifying these cases because it exposes all relevant connections rather than trying to force a one-to-one mapping.

---

## BDQ Tests Tend to Be More Granular

A recurring pattern is that BDQ Tests generally model individual validation rules, whereas ALA Assertions often model higher-level data quality outcomes.

As a result:

- one ALA Assertion may relate to several BDQ Tests;
- one BDQ Test may contribute to several ALA Assertions; and
- many relationships are better understood as dependencies or associations rather than mappings.

This difference in granularity needs to be considered when comparing the two systems.

---

## Implications for Mapping

The review suggests that many useful relationships will not be expressible as simple one-to-one mappings.

Possible outcomes include:

- `skos:relatedMatch`
- no direct mapping
- relationships to multiple BDQ Tests
- relationships that depend on combinations of BDQ Test outcomes

Consequently, the candidate association spreadsheet may be a more valuable review artefact than the eventual mapping set.

The association analysis helps explain *why* concepts are related, whereas mappings merely record *that* they are related.

---

## Role of SSSOM Mappings

SSSOM mappings are likely to be most useful after implementation decisions arising from this review have been made.

At the current stage, the priority is understanding:

- overlaps between ALA Assertions and BDQ Tests;
- differences in modelling approach;
- differences in granularity; and
- opportunities for improving assertion design.

Once those questions have been addressed and any resulting changes have been implemented, SSSOM mappings can provide a useful mechanism for formally documenting and exchanging the resulting relationships.

---

## Developing an Assertion Framework Alongside the BDQ Test Framework

An important conclusion emerging from the comparison is that the BDQ Tests should not necessarily be treated as an external standard to which the existing ALA Assertions are mapped.

The analysis suggests a more productive approach:

1. Review the BDQ Tests grouped by Darwin Core class and term.
2. Develop an assertion framework that complements the BDQ Test Framework and represents the data quality issues identified by those tests.
3. Implement those assertions directly.
4. Deprecate existing ALA (and inherited GBIF) assertions where they no longer represent the preferred model.
5. Record the relationships between deprecated and replacement assertions using the provenance vocabulary rather than a mapping vocabulary.

This approach aligns with the distinction identified earlier between validation-oriented and issue-oriented modelling.

The BDQ Framework is primarily concerned with asking questions such as:

> Is this value valid?

> Is this field populated?

> Is this information internally consistent?

The ALA Assertion Framework should focus on the complementary question:

> What data quality issue has been detected?

Under this approach, BDQ Tests and ALA Assertions are not alternative implementations of the same concepts. Instead, they form two related layers within a broader data quality framework:

```text
BDQ Tests
    ↓
Validation outcomes
    ↓
ALA Assertions
    ↓
Data quality issues
```

The report:

```text
reports/bdq_by_class_and_term.md
```

is particularly valuable because it provides a structured view of the validation concepts covered by the BDQ Standard and therefore provides a starting point for designing a corresponding assertion framework.

This approach has several advantages:

- It treats the BDQ Standard as the primary validation framework.
- It recognises that assertions and validations serve different purposes.
- It allows compound assertions to be replaced by more granular assertions derived from BDQ validations.
- It avoids preserving legacy assertion structures merely because they already exist.
- It provides a clearer separation between validation outcomes and data quality issues.

For example, rather than mapping:

```text
COUNTRY_COORDINATE_MISMATCH
```

to one or more BDQ Tests, it may be preferable to replace it with a set of more focused assertions derived from the relevant BDQ validations.

In this scenario, the important relationship is not:

```text
old assertion
    skos:relatedMatch
new assertion
```

but:

```text
old assertion
    dcterms:isReplacedBy
new assertion
```

or the inverse:

```text
new assertion
    dcterms:replaces
old assertion
```

The goal is therefore not simply to map the existing ALA Assertions to the BDQ Standard, but to develop an assertion framework that sits alongside the BDQ Test Framework and expresses the data quality issues identified through validation.

Formal mappings such as SSSOM mappings become most useful after the new assertions have been designed and implemented. At that point they can document relationships between concepts, whereas the current review is primarily concerned with improving the underlying assertion model itself.

In summary:

> We should implement the standard, not map the implementation to the standard.