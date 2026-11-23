# ALA Data Quality Assertions

## ALTITUDE_IN_FEET

| Field | Value |
|-------|-------|
| Status | Not implemented |
| DwC Class | dcterms:Location |
| DwC Terms | dwc:minimumElevationInMeters<br>dwc:maximumElevationInMeters |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/ALTITUDE_IN_FEET |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+ALTITUDE_IN_FEET&type=code |

---

## ALTITUDE_NON_NUMERIC

| Field | Value |
|-------|-------|
| Status | Not implemented |
| Recommendation | Remove |
| DwC Class | dcterms:Location |
| DwC Terms | dwc:minimumElevationInMeters<br>dwc:maximumElevationInMeters |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/ALTITUDE_NON_NUMERIC |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+ALTITUDE_NON_NUMERIC&type=code |

**Actions**

Duplicate of ELEVATION_NON_NUMERIC

---

## ALTITUDE_OUT_OF_RANGE

| Field | Value |
|-------|-------|
| Status | Not implemented |
| Recommendation | Remove |
| DwC Class | dcterms:Location |
| DwC Terms | dwc:minimumElevationInMeters<br>dwc:maximumElevationInMeters |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/ALTITUDE_OUT_OF_RANGE |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+ALTITUDE_OUT_OF_RANGE&type=code |

**Actions**

Probably a duplicate of ELEVATION_UNLIKELY

---

## AMBIGUOUS_COLLECTION

| Field | Value |
|-------|-------|
| Status | Unused |
| Recommendation | Keep |
| DwC Class | Record Level<br>EML |
| DwC Terms | ? |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/AMBIGUOUS_COLLECTION |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+AMBIGUOUS_COLLECTION&type=code |

**GBIF**

| Field | Value |
|-------|-------|
| **Class Asserted In** | GrscicollInterpreter |
| **Method Asserted By** | getCollectionMatchNoneIssue |
| **Assertion Logic** | The collection name is looked up in GRSciColl and a CollectionMatch with a Status is returned. It is not explained what Status.AMBIGUOUS means, but presumably the collection could be matched to more than one collection. It is also unclear if the match is based on the data or information in the EML. |

**Actions**

No action required. The best way to prevent institution and collection match issues is to provide `collectionID` and `institutionID` with the GRSciColl identifiers (i.e., doing the matching ourselves).

---

## AMBIGUOUS_INSTITUTION

| Field | Value |
|-------|-------|
| Status | Unused |
| Recommendation | Keep |
| DwC Class | Record Level<br>EML |
| DwC Terms | ? |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/AMBIGUOUS_INSTITUTION |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+AMBIGUOUS_INSTITUTION&type=code |

**GBIF**

| Field | Value |
|-------|-------|
| **Class Asserted In** | GrscicollInterpreter |
| **Method Asserted By** | getInstitutionMatchNoneIssue |
| **Assertion Logic** | This is a lookup in GRSciColl. It is not explained what AMBIGUOUS means, but presumably the institution could be not be unambiguously match to a single institution in GrSciColl. Also not certain what data is used. |

**Actions**

No action required.

---

## AMBIGUOUS_NAME

| Field | Value |
|-------|-------|
| Status | Not implemented |
| Recommendation | Remove |
| DwC Class | ? |
| DwC Terms | ? |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/AMBIGUOUS_NAME |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+AMBIGUOUS_NAME&type=code |

---

## BADLY_FORMED_ALTITUDE

| Field | Value |
|-------|-------|
| Status | Not implemented |
| Recommendation | Remove |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/BADLY_FORMED_ALTITUDE |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+BADLY_FORMED_ALTITUDE&type=code |

---

## BADLY_FORMED_BASIS_OF_RECORD

| Field | Value |
|-------|-------|
| Status | Not implemented |
| Recommendation | Remove |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/BADLY_FORMED_BASIS_OF_RECORD |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+BADLY_FORMED_BASIS_OF_RECORD&type=code |

---

## BASIS_OF_RECORD_INVALID

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 657306.0 |
| Recommendation | Keep |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/BASIS_OF_RECORD_INVALID |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+BASIS_OF_RECORD_INVALID&type=code |

**GBIF**

| Field | Value |
|-------|-------|
| **Class Asserted In** | BasicInterpreter |
| **Method Asserted By** | interpretBasisOfRecord |
| **Assertion Logic** | Value for basisOfRecord cannot be interpreted. (basisOfRecord is required in a Darwin Core Archive) |

**Actions**

No action required.

---

## COLLECTING_PATTERNS_GENERAL

| Field | Value |
|-------|-------|
| Status | Not implemented |
| Recommendation | Remove |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/COLLECTING_PATTERNS_GENERAL |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+COLLECTING_PATTERNS_GENERAL&type=code |

---

## COLLECTION_MATCH_FUZZY

| Field | Value |
|-------|-------|
| Status | Unused |
| Recommendation | Keep |
| DwC Class | Record Level<br>EML |
| DwC Terms | ? |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/COLLECTION_MATCH_FUZZY |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+COLLECTION_MATCH_FUZZY&type=code |

**GBIF**

| Field | Value |
|-------|-------|
| **Class Asserted In** | GrscicollInterpreter |
| **Method Asserted By** | getCollectionMatch |
| **Assertion Logic** | Lookup in GrScicoll. Match is fuzzy. |

**Actions**

No action required.

---

## COLLECTION_MATCH_NONE

| Field | Value |
|-------|-------|
| Status | Unused |
| Recommendation | Keep |
| DwC Class | Record Level<br>EML |
| DwC Terms | ? |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/COLLECTION_MATCH_NONE |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+COLLECTION_MATCH_NONE&type=code |

**GBIF**

| Field | Value |
|-------|-------|
| **Class Asserted In** | GrscicollInterpreter |
| **Method Asserted By** | getCollectionMatchNoneIssue |
| **Assertion Logic** | Lookup in GrScicoll. No match. |

**Actions**

No action required.

---

## CONTINENT_COORDINATE_MISMATCH

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 4408990.0 |
| Recommendation | Keep |
| DwC Class | dcterms:Location |
| DwC Terms | dwc:continent<br>dwc:decimalLongitude<br>dwc:decimalLatitude |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/CONTINENT_COORDINATE_MISMATCH |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+CONTINENT_COORDINATE_MISMATCH&type=code |

**GBIF**

| Field | Value |
|-------|-------|
| **Class Asserted In** | ContinentParser |
| **Method Asserted By** | parseContinent |
| **Assertion Logic** | Lookup. Coordinates land the record in a different continent than the value for `continent` indicates. |

**Actions**

No action required.

---

## CONTINENT_COUNTRY_MISMATCH

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 15195.0 |
| Recommendation | Keep |
| DwC Class | dcterms:Location |
| DwC Terms | dwc:continent<br>dwc:country |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/CONTINENT_COUNTRY_MISMATCH |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+CONTINENT_COUNTRY_MISMATCH&type=code |

**GBIF**

| Field | Value |
|-------|-------|
| **Class Asserted In** | ContinentParser |
| **Method Asserted By** | parseContinent |
| **Assertion Logic** | Lookup. Country is in a different continent than indicated by the value for `continent`. |

**Actions**

No action required.

---

## CONTINENT_DERIVED_FROM_COORDINATES

| Field | Value |
|-------|-------|
| Status | Unused |
| Recommendation | Keep |
| DwC Class | dcterms:Location |
| DwC Terms | dwc:decimalLongitude<br>dwc:decimalLatitude |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/CONTINENT_DERIVED_FROM_COORDINATES |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+CONTINENT_DERIVED_FROM_COORDINATES&type=code |

**GBIF**

| Field | Value |
|-------|-------|
| **Class Asserted In** | ContinentParser |
| **Method Asserted By** | parseContinent |
| **Assertion Logic** | Lookup. There is no value for `continent`, so the processed continent is based on the coordinates. |

**Actions**

No action required.

---

## CONTINENT_DERIVED_FROM_COUNTRY

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 1022422.0 |
| Recommendation | Keep |
| DwC Class | dcterms:Location |
| DwC Terms | dwc:country |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/CONTINENT_DERIVED_FROM_COUNTRY |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+CONTINENT_DERIVED_FROM_COUNTRY&type=code |

**GBIF**

| Field | Value |
|-------|-------|
| **Class Asserted In** | ContinentParser |
| **Method Asserted By** | parseContinent |
| **Assertion Logic** | If no continent and no coordinates are provided, but a country is provided, the continent is derived from the country. |

**Actions**

No action required.

---

## CONTINENT_INVALID

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 97796.0 |
| Recommendation | Keep |
| DwC Class | dcterms:Location |
| DwC Terms | dwc:continent |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/CONTINENT_INVALID |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+CONTINENT_INVALID&type=code |

**GBIF**

| Field | Value |
|-------|-------|
| **Class Asserted In** | ContinentParser |
| **Method Asserted By** | parseContinent |
| **Assertion Logic** | Lookup. Provided continent is not in vocabulary. |

**Actions**

No action required.

---

## COORDINATES_CENTRE_OF_COUNTRY

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 3585.0 |
| Recommendation | Keep |
| DwC Class | dcterms:Location |
| DwC Terms | dwc:country<br>dwc:decimalLatitude<br>dwc:decimalLongitude<br>dwc:verbatimLatitude |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/COORDINATES_CENTRE_OF_COUNTRY |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+COORDINATES_CENTRE_OF_COUNTRY&type=code |

**ALA**

| Field | Value |
|-------|-------|
| **Class Asserted In** | AlaLocationInterpreter |
| **Method Asserted By** | verifyLocationInfo |
| **Assertion Logic** | Lookup in https://github.com/gbif/pipelines/blob/master/livingatlas/pipelines/src/main/resources/countryCentrePoints.txt |

**Actions**

No action required.

---

## COORDINATES_CENTRE_OF_STATEPROVINCE

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 4236.0 |
| Recommendation | Keep |
| DwC Class | dcterms:Location |
| DwC Terms | dwc:decimalLatitude<br>dwc:decimalLongitude<br>dwc:verbatimLatitude<br>dwc:verbatimLongitude |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/COORDINATES_CENTRE_OF_STATEPROVINCE |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+COORDINATES_CENTRE_OF_STATEPROVINCE&type=code |

**ALA**

| Field | Value |
|-------|-------|
| **Class Asserted In** | ALALocationInterpreter |
| **Method Asserted By** | verifyLocationInfo |
| **Assertion Logic** | Lookup in https://github.com/gbif/pipelines/blob/master/livingatlas/pipelines/src/main/resources/stateProvinceCentrePoints.txt |

**Actions**

No action required

---

## COORDINATES_OUT_OF_RANGE

| Field | Value |
|-------|-------|
| Status | Not implemented (probably a typo for COORDINATE_OUT_OF_RANGE) |
| Recommendation | Remove |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/COORDINATES_OUT_OF_RANGE |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+COORDINATES_OUT_OF_RANGE&type=code |

---

## COORDINATE_ACCURACY_INVALID

| Field | Value |
|-------|-------|
| Status | Not implemented (probably replaced by COORDINATE_PRECISION_INVALID and COORDINATE_UNCERTAINTY_METERS_INVALID) |
| Recommendation | Remove |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/COORDINATE_ACCURACY_INVALID |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+COORDINATE_ACCURACY_INVALID&type=code |

---

## COORDINATE_HABITAT_MISMATCH

| Field | Value |
|-------|-------|
| Status | Not implemented |
| Recommendation | Remove |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/COORDINATE_HABITAT_MISMATCH |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+COORDINATE_HABITAT_MISMATCH&type=code |

---

## COORDINATE_INVALID

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 35365.0 |
| Recommendation | Keep |
| DwC Class | dcterms:Location |
| DwC Terms | dwc:decimalLatitude<br>dwc:decimalLongitude<br>dwc:verbatimLatitude<br>dwc:verbatimLongitude |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/COORDINATE_INVALID |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+COORDINATE_INVALID&type=code |

**GBIF**

| Field | Value |
|-------|-------|
| **Class Asserted In** | CoordinateParseUtils |
| **Method Asserted By** | parseLatLng |

**Actions**

No action required

---

## COORDINATE_OUT_OF_RANGE

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 1259.0 |
| Recommendation | Keep |
| DwC Class | dcterms:Location |
| DwC Terms | dwc:decimalLatitude<br>dwc:decimalLongitude<br>dwc:verbatimLatitude<br>dwc:verbatimLongitude |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/COORDINATE_OUT_OF_RANGE |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+COORDINATE_OUT_OF_RANGE&type=code |

**GBIF**

| Field | Value |
|-------|-------|
| **Class Asserted In** | CoordinateParseUtils |
| **Method Asserted By** | parseLatLng |
| **Assertion Logic** | latitude > 90 or < -90; longitude > 180 or < -180 |

**Actions**

No action required

---

## COORDINATE_PRECISION_INVALID

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 148678.0 |
| Recommendation | Keep |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/COORDINATE_PRECISION_INVALID |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+COORDINATE_PRECISION_INVALID&type=code |

**GBIF**

| Field | Value |
|-------|-------|
| **Class Asserted In** | LocationInterpreter |
| **Method Asserted By** | interpretCoordinatePrecision |
| **Assertion Logic** | Valid values of `coordinatePrecision` are between 0 and 1. |

**Actions**

No action required

---

## COORDINATE_PRECISION_MISMATCH

| Field | Value |
|-------|-------|
| Status | Not implemented (probably error for COORDINATE_PRECISION_UNCERTAINTY_MISMATCH) |
| Recommendation | Remove |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/COORDINATE_PRECISION_MISMATCH |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+COORDINATE_PRECISION_MISMATCH&type=code |

---

## COORDINATE_PRECISION_UNCERTAINTY_MISMATCH

| Field | Value |
|-------|-------|
| Status | Unused (listed among evaluation types, but there is no code for it; it could be among other location assertions, but this seems to be something that requires special code) |
| Recommendation | Remove |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/COORDINATE_PRECISION_UNCERTAINTY_MISMATCH |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+COORDINATE_PRECISION_UNCERTAINTY_MISMATCH&type=code |

**Actions**

The assertion might be useful, but not if we do not know what it does.

---

## COORDINATE_REPROJECTED

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 1083296.0 |
| Recommendation | Keep |
| DwC Class | dcterms:Location |
| DwC Terms | dwc:geodeticDatum<br>dwc:decimalLongitude<br>dwc:decimalLatitude |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/COORDINATE_REPROJECTED |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+COORDINATE_REPROJECTED&type=code |

**GBIF**

| Field | Value |
|-------|-------|
| **Class Asserted In** | Wgs84Projection |
| **Method Asserted By** | reproject |
| **Assertion Logic** | Issue is created when `geodeticDatum` is provided and projected coordinates are different from provided coordinates. |

**Actions**

No action required

---

## COORDINATE_REPROJECTION_FAILED

| Field | Value |
|-------|-------|
| Status | Unused |
| DwC Class | dcterms:Location |
| DwC Terms | dwc:geodeticDatum<br>dwc:decimalLongitude<br>dwc:decimalLatitude |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/COORDINATE_REPROJECTION_FAILED |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+COORDINATE_REPROJECTION_FAILED&type=code |

**GBIF**

| Field | Value |
|-------|-------|
| **Class Asserted In** | Wgs84Projection |
| **Method Asserted By** | reproject |
| **Assertion Logic** | Reprojection failed |

---

## COORDINATE_REPROJECTION_SUSPICIOUS

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 19567.0 |
| Recommendation | Keep |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/COORDINATE_REPROJECTION_SUSPICIOUS |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+COORDINATE_REPROJECTION_SUSPICIOUS&type=code |

**GBIF**

| Field | Value |
|-------|-------|
| **Class Asserted In** | Wgs84Projection |
| **Method Asserted By** | reproject |
| **Assertion Logic** | Reprojection is suspicious if there is a shift of more then 0.1° in either of the coordinates. |

**Actions**

No action required

---

## COORDINATE_ROUNDED

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 81230524.0 |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/COORDINATE_ROUNDED |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+COORDINATE_ROUNDED&type=code |

---

## COORDINATE_UNCERTAINTY_METERS_INVALID

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 98478381.0 |
| Recommendation | Keep |
| DwC Class | dcterms:Location |
| DwC Terms | dwc:coordinateUncertaintyInMeters |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/COORDINATE_UNCERTAINTY_METERS_INVALID |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+COORDINATE_UNCERTAINTY_METERS_INVALID&type=code |

**GBIF**

| Field | Value |
|-------|-------|
| **Class Asserted In** | LocationInterpreter |
| **Method Asserted By** | interpretCoordinateUncertaintyInMeters |
| **Assertion Logic** | COORDINATE_UNCERTAINTY_METERS_LOWER_BOUND = 0;
COORDINATE_UNCERTAINTY_METERS_UPPER_BOUND = 20,037,509;

dwc:coordinateUncertaintyInMeters < COORDINATE_UNCERTAINTY_METERS_LOWER_BOUND;
dwc:coordinateUncertainty > COORDINATE_UNCERTAINTY_METERS_UPPER_BOUND |

**ALA**

| Field | Value |
|-------|-------|
| **Class Asserted In** | AlaLocationInterpreter |
| **Method Asserted By** | interpretCoordinateUncertaintyInMeters |
| **Assertion Logic** | COORDINATE_UNCERTAINTY_METERS_LOWER_BOUND = 0;
COORDINATE_UNCERTAINTY_METERS_UPPER_BOUND = 5,000,000;

dwc:coordinateUncertaintyInMeters null or empty;
dwc:coordinateUncertaintyInMeters non-numeric;
dwc:coordinateUncertaintyInMeters < COORDINATE_UNCERTAINTY_METERS_LOWER_BOUND;
dwc:coordinateUncertainty > COORDINATE_UNCERTAINTY_METERS_UPPER_BOUND |

**Actions**

1. When null or empty an UNCERTAINTY_NOT_SPECIFIED issue should be asserted instead
2. Use the GBIF upper bound. A coordinate uncertainty of 10,000,000 m might be extremely unlikely (and is definitely wrong), but is not invalid. The ALA DQ Profile filters out records with uncertainty greater than 10,000 m.

---

## COORDINATE_UNCERTAINTY_PRECISION_MISMATCH

| Field | Value |
|-------|-------|
| Status | Deprecated |
| Recommendation | Remove |
| DwC Class | dcterms:Location |
| DwC Terms | coordinatePrecision<br>dwc:coordinateUncertaintyInMeters |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/COORDINATE_UNCERTAINTY_PRECISION_MISMATCH |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+COORDINATE_UNCERTAINTY_PRECISION_MISMATCH&type=code |

**GBIF**

| Field | Value |
|-------|-------|
| **Class Asserted In** | https://github.com/gbif/gbif-api/blob/master/src/main/java/org/gbif/api/vocabulary/OccurrenceIssue.java |

---

## COUNTRY_COORDINATE_MISMATCH

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 172330.0 |
| Recommendation | Keep |
| DwC Class | dcterms:Location |
| DwC Terms | dwc:country<br>dwc:decimalLatitude<br>dwc:decimalLongitude |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/COUNTRY_COORDINATE_MISMATCH |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+COUNTRY_COORDINATE_MISMATCH&type=code |

**GBIF**

| Field | Value |
|-------|-------|
| **Class Asserted In** | LocationMatcher |
| **Method Asserted By** | applyWithCountry, applyWithoutCountry |
| **Assertion Logic** | Provided country does not match the country the coordinates are in. |

**Actions**

No action required.

---

## COUNTRY_DERIVED_FROM_COORDINATES

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 19946786.0 |
| Recommendation | Keep |
| DwC Class | dcterms:Location |
| DwC Terms | dwc:decimalLatitude<br>dwc:decimalLongitude |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/COUNTRY_DERIVED_FROM_COORDINATES |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+COUNTRY_DERIVED_FROM_COORDINATES&type=code |

**GBIF**

| Field | Value |
|-------|-------|
| **Class Asserted In** | LocationMatcher |
| **Method Asserted By** | applyWithoutCountry |
| **Assertion Logic** | `country` is not provided, but `decimalLatitude` and `decimalLongitude` are. |

**Actions**

No action required.

---

## COUNTRY_INFERRED_FROM_COORDINATES

| Field | Value |
|-------|-------|
| Status | Not implemented (probably error for COUNTRY_DERIVED_FROM_COORDINATES) |
| Recommendation | Remove |
| DwC Class | dcterms:Location |
| DwC Terms | dwc:decimalLatitude<br>dwc:decimalLongitude |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/COUNTRY_INFERRED_FROM_COORDINATES |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+COUNTRY_INFERRED_FROM_COORDINATES&type=code |

---

## COUNTRY_INVALID

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 167351.0 |
| Recommendation | Keep |
| DwC Class | dcterms:Location |
| DwC Terms | dwc:country |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/COUNTRY_INVALID |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+COUNTRY_INVALID&type=code |

**GBIF**

| Field | Value |
|-------|-------|
| **Class Asserted In** | LocationParser |
| **Method Asserted By** | parse |
| **Assertion Logic** | Provided value for `country` can not be matched to country vocabulary. |

**Actions**

No action required

---

## COUNTRY_MISMATCH

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 3957.0 |
| Recommendation | Keep |
| DwC Class | dcterms:Location |
| DwC Terms | dwc:countryCode<br>dwc:decimalLatitude<br>dwc:decimalLongitude |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/COUNTRY_MISMATCH |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+COUNTRY_MISMATCH&type=code |

**GBIF**

| Field | Value |
|-------|-------|
| **Class Asserted In** | LocationParser |
| **Method Asserted By** | parse |
| **Assertion Logic** | There is a mismatch between the country and countryCode |

**Actions**

No action required

---

## DATA_ARE_GENERALISED

| Field | Value |
|-------|-------|
| Status | Not implemented |
| Recommendation | Remove |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/DATA_ARE_GENERALISED |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+DATA_ARE_GENERALISED&type=code |

---

## DATE_PRECISION_MISMATCH

| Field | Value |
|-------|-------|
| Status | Not implemented |
| Recommendation | Remove |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/DATE_PRECISION_MISMATCH |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+DATE_PRECISION_MISMATCH&type=code |

---

## DAY_MONTH_TRANSPOSED

| Field | Value |
|-------|-------|
| Status | Not implemented |
| Recommendation | Remove |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/DAY_MONTH_TRANSPOSED |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+DAY_MONTH_TRANSPOSED&type=code |

---

## DECIMAL_LAT_LONG_CALCULATION_FROM_EASTING_NORTHING_FAILED

| Field | Value |
|-------|-------|
| Status | Not implemented |
| Recommendation | Remove |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/DECIMAL_LAT_LONG_CALCULATION_FROM_EASTING_NORTHING_FAILED |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+DECIMAL_LAT_LONG_CALCULATION_FROM_EASTING_NORTHING_FAILED&type=code |

---

## DECIMAL_LAT_LONG_CONVERSION_FAILED

| Field | Value |
|-------|-------|
| Status | Not implemented |
| Recommendation | Remove |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/DECIMAL_LAT_LONG_CONVERSION_FAILED |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+DECIMAL_LAT_LONG_CONVERSION_FAILED&type=code |

---

## DEPTH_IN_FEET

| Field | Value |
|-------|-------|
| Status | Not implemented |
| Recommendation | Remove |
| DwC Class | dcterms:Location |
| DwC Terms | dwc:minimumDepthInMeters<br>dwc:maximumDepthInMeters |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/DEPTH_IN_FEET |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+DEPTH_IN_FEET&type=code |

---

## DEPTH_MIN_MAX_SWAPPED

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 24254.0 |
| Recommendation | Keep |
| DwC Class | dcterms:Location |
| DwC Terms | dwc:minimumDepthInMeters<br>dwc:maximumDepthInMeters |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/DEPTH_MIN_MAX_SWAPPED |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+DEPTH_MIN_MAX_SWAPPED&type=code |

**GBIF**

| Field | Value |
|-------|-------|
| **Class Asserted In** | https://github.com/gbif/gbif-api/blob/master/src/main/java/org/gbif/api/vocabulary/OccurrenceIssue.java |

**Actions**

Check if there are any records that do not pass this test. If there are none, the test is probably not implemented. Might be useful to download all records with both minumimElevationInMeters and maxElevationInMeters and see if there are any where minimumElevationInMeters > maximumElevationInMeters.

---

## DEPTH_NON_NUMERIC

| Field | Value |
|-------|-------|
| Status | Active? |
| Count | 357.0 |
| Recommendation | Keep? |
| DwC Class | dcterms:Location |
| DwC Terms | dwc:minimumDepthInMeters<br>dwc:maximumDepthInMeters |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/DEPTH_NON_NUMERIC |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+DEPTH_NON_NUMERIC&type=code |

**GBIF**

| Field | Value |
|-------|-------|
| **Class Asserted In** | https://github.com/gbif/gbif-api/blob/master/src/main/java/org/gbif/api/vocabulary/OccurrenceIssue.java |

**Actions**

Check if there are any records for which this warning is issued.

---

## DEPTH_NOT_METRIC

| Field | Value |
|-------|-------|
| Status | Active? |
| Count | 1.0 |
| Recommendation | Keep? |
| DwC Class | dcterms:Location |
| DwC Terms | dwc:minimumDepthInMeters<br>dwc:maximumDepthInMeters |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/DEPTH_NOT_METRIC |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+DEPTH_NOT_METRIC&type=code |

**GBIF**

| Field | Value |
|-------|-------|
| **Class Asserted In** | https://github.com/gbif/gbif-api/blob/master/src/main/java/org/gbif/api/vocabulary/OccurrenceIssue.java |

**Actions**

Check if there are any records for which this warning is issued.

---

## DEPTH_OUT_OF_RANGE

| Field | Value |
|-------|-------|
| Status | Not implemented |
| Recommendation | Remove |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/DEPTH_OUT_OF_RANGE |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+DEPTH_OUT_OF_RANGE&type=code |

---

## DEPTH_UNLIKELY

| Field | Value |
|-------|-------|
| Status | Active? |
| Count | 5789.0 |
| Recommendation | Keep? |
| DwC Class | dcterms:Location |
| DwC Terms | dwc:minimumDepthInMeters<br>dwc:maximumDepthInMeters |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/DEPTH_UNLIKELY |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+DEPTH_UNLIKELY&type=code |

**GBIF**

| Field | Value |
|-------|-------|
| **Class Asserted In** | https://github.com/gbif/gbif-api/blob/master/src/main/java/org/gbif/api/vocabulary/OccurrenceIssue.java |
| **Assertion Logic** | Set if depth is larger than 11,000m or negative. |

**Actions**

Check data.

---

## DETECTED_OUTLIER_GEOGRAPHIC

| Field | Value |
|-------|-------|
| Status | Not implemented |
| Recommendation | Remove |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/DETECTED_OUTLIER_GEOGRAPHIC |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+DETECTED_OUTLIER_GEOGRAPHIC&type=code |

---

## DETECTED_OUTLIER_JACKKNIFE

| Field | Value |
|-------|-------|
| Status | Not a data quality assertion anymore: we use the outlier_layer and outlier_layer_count filters for this |
| Recommendation | ? |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/DETECTED_OUTLIER_JACKKNIFE |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+DETECTED_OUTLIER_JACKKNIFE&type=code |

**Actions**

Find out if we are still doing this.

---

## DETECTED_OUTLIER_OTHER

| Field | Value |
|-------|-------|
| Status | Not implemented |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/DETECTED_OUTLIER_OTHER |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+DETECTED_OUTLIER_OTHER&type=code |

---

## DIFFERENT_OWNER_INSTITUTION

| Field | Value |
|-------|-------|
| Status | Unused |
| Recommendation | Keep |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/DIFFERENT_OWNER_INSTITUTION |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+DIFFERENT_OWNER_INSTITUTION&type=code |

**GBIF**

| Field | Value |
|-------|-------|
| **Class Asserted In** | GrscicollInterpreter |
| **Method Asserted By** | grscicollInterpreter, getInstitutionMatchNoneIssue |
| **Assertion Logic** | Not clear, issue is asserted when the lookup response contains 'DIFFERENT_OWNER' among its reasons, or when the status of the lookup is 'AMBIGUOUS_OWNER'. |

---

## ELEVATION_MIN_MAX_SWAPPED

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 9580.0 |
| Recommendation | Keep |
| DwC Class | dcterms:Location |
| DwC Terms | dwc:minimumElevationInMeters<br>dwc:maximumElevationInMeters |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/ELEVATION_MIN_MAX_SWAPPED |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+ELEVATION_MIN_MAX_SWAPPED&type=code |

**GBIF**

| Field | Value |
|-------|-------|
| **Class Asserted In** | src/main/java/org/gbif/common/parsers/geospatial/MeterRangeParser.java |
| **Method Asserted By** | parseElevation |
| **Assertion Logic** | Min. and max. elevation are swapped. |

---

## ELEVATION_NON_NUMERIC

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 2576.0 |
| Recommendation | Keep |
| DwC Class | dcterms:Location |
| DwC Terms | dwc:minimumElevationInMeters<br>dwc:maximumElevationInMeters |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/ELEVATION_NON_NUMERIC |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+ELEVATION_NON_NUMERIC&type=code |

**GBIF**

| Field | Value |
|-------|-------|
| **Class Asserted In** | ? |
| **Assertion Logic** | Value provided for minimumElevationInMeters or maxiumumElevationInMeters is not numeric |

---

## ELEVATION_NOT_METRIC

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 4.0 |
| Recommendation | Keep |
| DwC Class | dcterms:Location |
| DwC Terms | dwc:minimumElevationInMeters<br>dwc:maximumElevationInMeters |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/ELEVATION_NOT_METRIC |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+ELEVATION_NOT_METRIC&type=code |

**GBIF**

| Field | Value |
|-------|-------|
| **Class Asserted In** | ? |
| **Assertion Logic** | Value provided for minimumElevationInMeters or maxiumumElevationInMeters is not metric (might be sexagesimal) |

---

## ELEVATION_UNLIKELY

| Field | Value |
|-------|-------|
| Status | Unused |
| Recommendation | Keep |
| DwC Class | dcterms:Location |
| DwC Terms | dwc:minimumElevationInMeters<br>dwc:maximumElevationInMeters |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/ELEVATION_UNLIKELY |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+ELEVATION_UNLIKELY&type=code |

**GBIF**

| Field | Value |
|-------|-------|
| **Class Asserted In** | https://github.com/gbif/gbif-api/blob/master/src/main/java/org/gbif/api/vocabulary/OccurrenceIssue.java |
| **Assertion Logic** | Set if elevation is above the troposphere (17km) or below 11km (Mariana Trench). |

---

## FIRST_OF_CENTURY

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 174299.0 |
| Recommendation | Remove |
| DwC Class | dwc:Event |
| DwC Terms | dwc:eventDate<br>dwc:year<br>dwc:month<br>dwc:day |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/FIRST_OF_CENTURY |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+FIRST_OF_CENTURY&type=code |

**ALA**

| Field | Value |
|-------|-------|
| **Class Asserted In** | ALATemporalInterpreter |
| **Method Asserted By** | checkRecordDateQuality |
| **Assertion Logic** | This checks if a year is provided and if the year is the first (or last) of a century. The issue is asserted when the month and day are either not provided, or are '1'. This means that this issue is asserted for event dates like '1900' and '19-01', which is misleading if you ask me. |

**Actions**

I would just ditch it

---

## FIRST_OF_MONTH

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 8296090.0 |
| Recommendation | Remove |
| DwC Class | dwc:Event |
| DwC Terms | dwc:eventDate<br>dwc:year<br>dwc:month<br>dwc:day |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/FIRST_OF_MONTH |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+FIRST_OF_MONTH&type=code |

**ALA**

| Field | Value |
|-------|-------|
| **Class Asserted In** | ALATemporalInterpreter |
| **Method Asserted By** | checkRecordDateQuality |
| **Assertion Logic** | The day provided is the first day of the month. |

**Actions**

I would just ditch it

---

## FIRST_OF_YEAR

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 2378349.0 |
| Recommendation | Remove |
| DwC Class | dwc:Event |
| DwC Terms | dwc:eventDate<br>dwc:year<br>dwc:month<br>dwc:day |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/FIRST_OF_YEAR |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+FIRST_OF_YEAR&type=code |

**ALA**

| Field | Value |
|-------|-------|
| **Class Asserted In** | ALATemporalInterpreter |
| **Method Asserted By** | checkRecordDateQuality |
| **Assertion Logic** | This issue is asserted if the month is January and the day is either the first or not provided; incorrect if you ask me. |

**Actions**

I would just ditch it

---

## FOOTPRINT_SRS_INVALID

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 1121933.0 |
| Recommendation | Keep |
| DwC Class | dcterms:Location |
| DwC Terms | footprintSRS |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/FOOTPRINT_SRS_INVALID |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+FOOTPRINT_SRS_INVALID&type=code |

**GBIF**

| Field | Value |
|-------|-------|
| **Class Asserted In** | LocationInterpreter |
| **Method Asserted By** | interpretFootprintWKT |
| **Assertion Logic** | footprintSRS is provided, but cannot be interpreted |

**Actions**

No action required

---

## FOOTPRINT_WKT_INVALID

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 2202700.0 |
| Recommendation | Keep |
| DwC Class | dcterms:Location |
| DwC Terms | dwc:footprintWKT |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/FOOTPRINT_WKT_INVALID |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+FOOTPRINT_WKT_INVALID&type=code |

**GBIF**

| Field | Value |
|-------|-------|
| **Class Asserted In** | FootprintWKTParser |
| **Method Asserted By** | parseFootprintWKT |
| **Assertion Logic** | footprintWKT cannot be parsed |

**Actions**

No action required

---

## FOOTPRINT_WKT_MISMATCH

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 156994.0 |
| Recommendation | Keep |
| DwC Class | dcterms:Location |
| DwC Terms | dwc:footprintWKT<br>dwc:decimalLatitude<br>dwc:decimalLongitude |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/FOOTPRINT_WKT_MISMATCH |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+FOOTPRINT_WKT_MISMATCH&type=code |

**GBIF**

| Field | Value |
|-------|-------|
| **Class Asserted In** | LocationInterpretor |
| **Method Asserted By** | intepretFootprintWKT |
| **Assertion Logic** | footprintWKT is a POINT and is not the same as that of the decimalLatitude and decimalLongitude |

**Actions**

No action required

---

## GEODETIC_DATUM_INVALID

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 1312188.0 |
| Recommendation | Keep |
| DwC Class | dcterms:Location |
| DwC Terms | dwc:geodeticDatum |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/GEODETIC_DATUM_INVALID |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+GEODETIC_DATUM_INVALID&type=code |

**GBIF**

| Field | Value |
|-------|-------|
| **Class Asserted In** | Wgs84Projection |
| **Method Asserted By** | reproject |
| **Assertion Logic** | Provided geodeticDatum could not be interpreted |

**Actions**

No action required

---

## GEOREFERENCED_DATE_INVALID

| Field | Value |
|-------|-------|
| Status | Unused |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/GEOREFERENCED_DATE_INVALID |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+GEOREFERENCED_DATE_INVALID&type=code |

---

## GEOREFERENCED_DATE_UNLIKELY

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 78.0 |
| Recommendation | Remove |
| DwC Class | dcterms:Location |
| DwC Terms | georeferencedDate |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/GEOREFERENCED_DATE_UNLIKELY |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+GEOREFERENCED_DATE_UNLIKELY&type=code |

**ALA**

| Field | Value |
|-------|-------|
| **Class Asserted In** | AlaLocationInterpreter |
| **Method Asserted By** | interpretGeoreferencedDate |
| **Assertion Logic** | Ostensibly, it converts the GBIF IDENTIFIED_DATE_UNLIKELY to GEOREFERENCED_DATE_UNLIKELY (which seems silly), but the numbers do not match. The records that are pulled up by this assertion have a georeferencedDate that is in the future (some almost 8,000 years in the future). |

**Actions**

No action required

---

## GEOREFERENCE_POST_OCCURRENCE

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 117217.0 |
| Recommendation | Keep |
| DwC Class | dcterms:Location |
| DwC Terms | georeferencedDate |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/GEOREFERENCE_POST_OCCURRENCE |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+GEOREFERENCE_POST_OCCURRENCE&type=code |

**ALA**

| Field | Value |
|-------|-------|
| **Class Asserted In** | ALATemporalInterpreter |
| **Method Asserted By** | checkGeoreferencedDate |
| **Assertion Logic** | georeferencedDate is after the eventDate |

**Actions**

No action required

---

## GEOREFERENCE_UNCERTAIN

| Field | Value |
|-------|-------|
| Status | Not implemented |
| Recommendation | Remove |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/GEOREFERENCE_UNCERTAIN |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+GEOREFERENCE_UNCERTAIN&type=code |

---

## GEOREFERENCE_VERIFIED

| Field | Value |
|-------|-------|
| Status | Not implemented |
| Recommendation | Remove |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/GEOREFERENCE_VERIFIED |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+GEOREFERENCE_VERIFIED&type=code |

---

## HOMONYM_ISSUE

| Field | Value |
|-------|-------|
| Status | Not implemented |
| Recommendation | Remove |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/HOMONYM_ISSUE |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+HOMONYM_ISSUE&type=code |

---

## IDENTIFICATION_UNCERTAIN

| Field | Value |
|-------|-------|
| Status | Not implemented |
| Recommendation | Remove |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/IDENTIFICATION_UNCERTAIN |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+IDENTIFICATION_UNCERTAIN&type=code |

---

## IDENTIFICATION_VERIFIED

| Field | Value |
|-------|-------|
| Status | Not implemented |
| Recommendation | Remove |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/IDENTIFICATION_VERIFIED |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+IDENTIFICATION_VERIFIED&type=code |

---

## IDENTIFIED_DATE_INVALID

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 63479.0 |
| Recommendation | Keep |
| DwC Class | dwc:Identification |
| DwC Terms | dwc:dateIdentified |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/IDENTIFIED_DATE_INVALID |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+IDENTIFIED_DATE_INVALID&type=code |

**GBIF**

| Field | Value |
|-------|-------|
| **Class Asserted In** | TemporalInterpreter |
| **Method Asserted By** | interpretDateIdentified |
| **Assertion Logic** | dateIdentified is not a valid ISO 8601 string |

**Actions**

No action required

---

## IDENTIFIED_DATE_UNLIKELY

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 8451.0 |
| Recommendation | Keep |
| DwC Class | dwc:Identification |
| DwC Terms | dwc:dateIdentified |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/IDENTIFIED_DATE_UNLIKELY |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+IDENTIFIED_DATE_UNLIKELY&type=code |

**GBIF**

| Field | Value |
|-------|-------|
| **Class Asserted In** | TemporalInterpreter |
| **Method Asserted By** | interpretDateIdentified |
| **Assertion Logic** | dateIdentified is in the future |

**Actions**

No action required

---

## ID_PRE_OCCURRENCE

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 3460430.0 |
| Recommendation | Keep |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/ID_PRE_OCCURRENCE |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+ID_PRE_OCCURRENCE&type=code |

**ALA**

| Field | Value |
|-------|-------|
| **Class Asserted In** | ALATemporalInterpreter |
| **Method Asserted By** | checkDateIdentified |
| **Assertion Logic** | eventDate is after dateIdentified. This often gives misleading results, as the precision of the dates are not taken into accound (identification dates are often given as just month and year). |

**Actions**

It would be better to have separate tests for incomplete eventDate and dateIdentified and then compare dates of the same precision. The latter will be hard in pipelines.

---

## INCOMPLETE_COLLECTION_DATE

| Field | Value |
|-------|-------|
| Status | Not implemented |
| DwC Class | dwc:Identification |
| DwC Terms | dwc:dateIdentified |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/INCOMPLETE_COLLECTION_DATE |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+INCOMPLETE_COLLECTION_DATE&type=code |

**Actions**

I would like to have this test back.

---

## INDIVIDUAL_COUNT_CONFLICTS_WITH_OCCURRENCE_STATUS

| Field | Value |
|-------|-------|
| Count | 92408.0 |
| DwC Class | dwc:Occurrence |
| DwC Terms | dwc:occurrenceStatus<br>individualCount |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/INDIVIDUAL_COUNT_CONFLICTS_WITH_OCCURRENCE_STATUS |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+INDIVIDUAL_COUNT_CONFLICTS_WITH_OCCURRENCE_STATUS&type=code |

---

## INDIVIDUAL_COUNT_INVALID

| Field | Value |
|-------|-------|
| Count | 2123039.0 |
| DwC Class | dwc:Occurrence |
| DwC Terms | individualCount<br>dwc:occurrenceStatus |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/INDIVIDUAL_COUNT_INVALID |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+INDIVIDUAL_COUNT_INVALID&type=code |

---

## INFERRED_DUPLICATE_RECORD

| Field | Value |
|-------|-------|
| Status | Not a data quality assertion anymore: we use the duplicate_status filter for this |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/INFERRED_DUPLICATE_RECORD |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+INFERRED_DUPLICATE_RECORD&type=code |

---

## INFERRED_FALSE_PRECISION

| Field | Value |
|-------|-------|
| Status | Not implemented |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/INFERRED_FALSE_PRECISION |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+INFERRED_FALSE_PRECISION&type=code |

---

## INSTITUTION_COLLECTION_MISMATCH

| Field | Value |
|-------|-------|
| Status | Unused |
| Recommendation | Keep |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/INSTITUTION_COLLECTION_MISMATCH |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+INSTITUTION_COLLECTION_MISMATCH&type=code |

**GBIF**

| Field | Value |
|-------|-------|
| **Class Asserted In** | GrscicollInterpreter |
| **Method Asserted By** | getCollectionsMatchNoneIssue |
| **Assertion Logic** | Not exactly clear, but it seems to be a fuzzy match to a collection in another institution than given in the data. |

**Actions**

No action required

---

## INSTITUTION_MATCH_FUZZY

| Field | Value |
|-------|-------|
| Status | Unused |
| Recommendation | Keep |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/INSTITUTION_MATCH_FUZZY |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+INSTITUTION_MATCH_FUZZY&type=code |

**GBIF**

| Field | Value |
|-------|-------|
| **Class Asserted In** | GrscicollInterpreter |
| **Method Asserted By** | grscicollInterpreter |
| **Assertion Logic** | Institution match is fuzzy (probably matched by name rather than institutionID or institutionCode) |

**Actions**

No action required

---

## INSTITUTION_MATCH_NONE

| Field | Value |
|-------|-------|
| Status | Unused |
| Recommendation | Keep |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/INSTITUTION_MATCH_NONE |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+INSTITUTION_MATCH_NONE&type=code |

**GBIF**

| Field | Value |
|-------|-------|
| **Method Asserted By** | getInstitutionMatchNoneIssue |
| **Assertion Logic** | Institution coul not be matched to GRSciColl |

**Actions**

No action required

---

## INTERPRETATION_ERROR

| Field | Value |
|-------|-------|
| Status | Unused |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/INTERPRETATION_ERROR |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+INTERPRETATION_ERROR&type=code |

---

## INVALID_COLLECTION_DATE

| Field | Value |
|-------|-------|
| Status | Not implemented |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/INVALID_COLLECTION_DATE |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+INVALID_COLLECTION_DATE&type=code |

---

## INVALID_GEODETICDATUM

| Field | Value |
|-------|-------|
| Status | Not implemented. Replaced by GEODETIC_DATUM_INVALID. |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/INVALID_GEODETICDATUM |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+INVALID_GEODETICDATUM&type=code |

---

## INVALID_IMAGE_URL

| Field | Value |
|-------|-------|
| Status | Not implemented |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/INVALID_IMAGE_URL |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+INVALID_IMAGE_URL&type=code |

---

## INVALID_SCIENTIFIC_NAME

| Field | Value |
|-------|-------|
| Count | 3434536.0 |
| Recommendation | Keep |
| DwC Class | dwc:Taxon |
| DwC Terms | dwc:scientificName |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/INVALID_SCIENTIFIC_NAME |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+INVALID_SCIENTIFIC_NAME&type=code |

**ALA**

| Field | Value |
|-------|-------|
| **Class Asserted In** | ALATaxonomyInterpreter |
| **Method Asserted By** | alaResultQualityChecks |
| **Assertion Logic** | Issue is assered if the name type is NO_NAME, INFORMAL or PLACEHOLDER |

**Actions**

No action required

---

## INVERTED_COORDINATES

| Field | Value |
|-------|-------|
| Status | Not implemented |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/INVERTED_COORDINATES |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+INVERTED_COORDINATES&type=code |

---

## LOCATION_NOT_SUPPLIED

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 3186367.0 |
| Recommendation | Keep |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/LOCATION_NOT_SUPPLIED |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+LOCATION_NOT_SUPPLIED&type=code |

**ALA**

| Field | Value |
|-------|-------|
| **Class Asserted In** | CoordinatesParser |
| **Method Asserted By** | parseCoords |
| **Assertion Logic** | decimalLatitude + decimalLongitude, or verbatimLatitude + verbatimLongitude, or verbatimCoordinates are either not provided or cannot be parsed. |

**Actions**

COORDINATES_NOT_SUPPLIED' would make more sense as a name.

---

## MIN_MAX_ALTITUDE_REVERSED

| Field | Value |
|-------|-------|
| Status | Not implemented. Replaced by ELEVATION_MIN_MAX_SWAPPED. |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/MIN_MAX_ALTITUDE_REVERSED |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+MIN_MAX_ALTITUDE_REVERSED&type=code |

---

## MIN_MAX_DEPTH_REVERSED

| Field | Value |
|-------|-------|
| Status | Not implementedReplaced by DEPTH_MIN_MAX_SWAPPED. |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/MIN_MAX_DEPTH_REVERSED |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+MIN_MAX_DEPTH_REVERSED&type=code |

---

## MISSING_BASIS_OF_RECORD

| Field | Value |
|-------|-------|
| Status | Not implemented |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/MISSING_BASIS_OF_RECORD |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+MISSING_BASIS_OF_RECORD&type=code |

---

## MISSING_COLLECTION_DATE

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 4035164.0 |
| Recommendation | Keep |
| DwC Class | dwc:Event |
| DwC Terms | dwc:eventDate<br>dwc:year<br>dwc:month<br>dwc:day |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/MISSING_COLLECTION_DATE |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+MISSING_COLLECTION_DATE&type=code |

**ALA**

| Field | Value |
|-------|-------|
| **Class Asserted In** | ALATemporalInterpreter |
| **Method Asserted By** | checkRecordDateQuality |
| **Assertion Logic** | Neither eventDate, nor year, month, day are provided |

**Actions**

No action required

---

## MISSING_COORDINATEPRECISION

| Field | Value |
|-------|-------|
| Status | Unused |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/MISSING_COORDINATEPRECISION |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+MISSING_COORDINATEPRECISION&type=code |

---

## MISSING_DATEIDENTIFIED

| Field | Value |
|-------|-------|
| Status | Not implemented |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/MISSING_DATEIDENTIFIED |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+MISSING_DATEIDENTIFIED&type=code |

---

## MISSING_GEODETICDATUM

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 54282339.0 |
| Recommendation | Keep |
| DwC Class | dcterms:Location |
| DwC Terms | dwc:geodeticDatum |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/MISSING_GEODETICDATUM |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+MISSING_GEODETICDATUM&type=code |

**ALA**

| Field | Value |
|-------|-------|
| **Class Asserted In** | CoordinatesParser |
| **Method Asserted By** | parseCoords |
| **Assertion Logic** | geodeticDatum is not supplied |

**Actions**

No action required

---

## MISSING_GEOREFERENCEDBY

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 148037081.0 |
| Recommendation | Keep |
| DwC Class | dcterms:Location |
| DwC Terms | georeferencedBy |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/MISSING_GEOREFERENCEDBY |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+MISSING_GEOREFERENCEDBY&type=code |

**ALA**

| Field | Value |
|-------|-------|
| **Class Asserted In** | ALALocationInterpreter |
| **Method Asserted By** | interpretGeoReferenceTerms |
| **Assertion Logic** | georeferencedBy is not supplied |

**Actions**

No action required

---

## MISSING_GEOREFERENCEPROTOCOL

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 166528546.0 |
| Recommendation | Keep |
| DwC Class | dcterms:Location |
| DwC Terms | georeferenceProtocol |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/MISSING_GEOREFERENCEPROTOCOL |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+MISSING_GEOREFERENCEPROTOCOL&type=code |

**ALA**

| Field | Value |
|-------|-------|
| **Class Asserted In** | ALALocationInterpreter |
| **Method Asserted By** | interpretGeoReferenceTerms |
| **Assertion Logic** | georeferenceProtocol not supplied |

**Actions**

No action required

---

## MISSING_GEOREFERENCESOURCES

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 175869329.0 |
| Recommendation | Remove? |
| DwC Class | dcterms:Location |
| DwC Terms | georeferenceSources |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/MISSING_GEOREFERENCESOURCES |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+MISSING_GEOREFERENCESOURCES&type=code |

**ALA**

| Field | Value |
|-------|-------|
| **Class Asserted In** | ALALocationInterpreter |
| **Method Asserted By** | interpretGeoReferenceTerms |
| **Assertion Logic** | georeferenceSources not supplied |

**Actions**

Consider removing

---

## MISSING_GEOREFERENCEVERIFICATIONSTATUS

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 152650741.0 |
| Recommendation | Remove |
| DwC Class | dcterms:Location |
| DwC Terms | georeferenceVerificationStatus |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/MISSING_GEOREFERENCEVERIFICATIONSTATUS |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+MISSING_GEOREFERENCEVERIFICATIONSTATUS&type=code |

**ALA**

| Field | Value |
|-------|-------|
| **Class Asserted In** | ALALocationInterpreter |
| **Method Asserted By** | interpretGeoReferenceTerms |
| **Assertion Logic** | georeferenceVerificationStatus not supplied |

**Actions**

I would remove this, as you would generally only verify a georeference if there has been an assertion that it might be incorrect.

---

## MISSING_GEOREFERENCE_DATE

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 179057440.0 |
| Recommendation | Keep |
| DwC Class | dcterms:Location |
| DwC Terms | georeferencedDate |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/MISSING_GEOREFERENCE_DATE |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+MISSING_GEOREFERENCE_DATE&type=code |

**ALA**

| Field | Value |
|-------|-------|
| **Class Asserted In** | ALALocationInterpreter |
| **Method Asserted By** | interpretGeoReferenceTerms |
| **Assertion Logic** | georeferencedDate not supplied |

**Actions**

I am probably the only one who delivers this, so I'd say 'Keep it!'

---

## MISSING_IDENTIFICATIONQUALIFIER

| Field | Value |
|-------|-------|
| Status | Not implemented |
| DwC Class | dwc:Taxon |
| DwC Terms | identificationQualifier |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/MISSING_IDENTIFICATIONQUALIFIER |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+MISSING_IDENTIFICATIONQUALIFIER&type=code |

**Actions**

Good riddance

---

## MISSING_IDENTIFICATIONREFERENCES

| Field | Value |
|-------|-------|
| Status | Not implemented |
| DwC Class | dwc:Taxon |
| DwC Terms | identificationReferences |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/MISSING_IDENTIFICATIONREFERENCES |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+MISSING_IDENTIFICATIONREFERENCES&type=code |

---

## MISSING_IDENTIFIEDBY

| Field | Value |
|-------|-------|
| Status | Not implemented |
| DwC Class | dwc:Identification |
| DwC Terms | identifiedBy |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/MISSING_IDENTIFIEDBY |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+MISSING_IDENTIFIEDBY&type=code |

**Actions**

This might be a good one to get back.

---

## MISSING_TAXONRANK

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 40411927.0 |
| Recommendation | Remove |
| DwC Class | dwc:Taxon |
| DwC Terms | dwc:taxonRank |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/MISSING_TAXONRANK |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+MISSING_TAXONRANK&type=code |

**ALA**

| Field | Value |
|-------|-------|
| **Class Asserted In** | ALATaxonomyInterpreter |
| **Method Asserted By** | alaSourceQualityChecks |
| **Assertion Logic** | taxonRank not supplued |

**Actions**

This is not a data quality issue.

---

## MODIFIED_DATE_INVALID

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 481992.0 |
| Recommendation | Keep |
| DwC Class | Record Level |
| DwC Terms | dcterms:modified |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/MODIFIED_DATE_INVALID |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+MODIFIED_DATE_INVALID&type=code |

**GBIF**

| Field | Value |
|-------|-------|
| **Class Asserted In** | TemporalInterpreter |
| **Method Asserted By** | interpretModified |
| **Assertion Logic** | dcterms:modified is invalid IS 8601 string |

**Actions**

No action required

---

## MODIFIED_DATE_UNLIKELY

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 66.0 |
| Recommendation | Keep |
| DwC Class | Record Level |
| DwC Terms | dcterms:modified |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/MODIFIED_DATE_UNLIKELY |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+MODIFIED_DATE_UNLIKELY&type=code |

**GBIF**

| Field | Value |
|-------|-------|
| **Class Asserted In** | TemporalInterpreter |
| **Method Asserted By** | interpretModified |
| **Assertion Logic** | dcterms:modified is in the future |

**Actions**

No action required

---

## MULTIMEDIA_DATE_INVALID

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 291727.0 |
| Recommendation | Keep |
| DwC Class | dwc:Occurrence |
| DwC Terms | associatedMedia |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/MULTIMEDIA_DATE_INVALID |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+MULTIMEDIA_DATE_INVALID&type=code |

**GBIF**

| Field | Value |
|-------|-------|
| **Class Asserted In** | ImageInterpreter |
| **Method Asserted By** | interpret |
| **Assertion Logic** | dcterms:created of at least one of the associate images is invalid |

**Actions**

No action required

---

## MULTIMEDIA_URI_INVALID

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 308724.0 |
| DwC Class | dwc:Occurrence |
| DwC Terms | associatedMedia |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/MULTIMEDIA_URI_INVALID |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+MULTIMEDIA_URI_INVALID&type=code |

**GBIF**

| Field | Value |
|-------|-------|
| **Class Asserted In** | ImageInterpreter |
| **Method Asserted By** | interpret |
| **Assertion Logic** | dcterms:identifier of at least one of the associated images is invalid |

---

## NAME_NOT_IN_NATIONAL_CHECKLISTS

| Field | Value |
|-------|-------|
| Status | Not implemented |
| DwC Class | dwc:Taxon |
| DwC Terms | dwc:scientificName |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/NAME_NOT_IN_NATIONAL_CHECKLISTS |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+NAME_NOT_IN_NATIONAL_CHECKLISTS&type=code |

**Actions**

This would be a nice thing to have back, but it needs to be part of the name matching.

---

## NAME_NOT_RECOGNISED

| Field | Value |
|-------|-------|
| Status | Not implemented |
| DwC Class | dwc:Taxon |
| DwC Terms | dwc:scientificName |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/NAME_NOT_RECOGNISED |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+NAME_NOT_RECOGNISED&type=code |

---

## NAME_NOT_SUPPLIED

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 1417291.0 |
| Recommendation | Keep |
| DwC Class | dwc:Taxon |
| DwC Terms | dwc:scientificName |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/NAME_NOT_SUPPLIED |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+NAME_NOT_SUPPLIED&type=code |

**ALA**

| Field | Value |
|-------|-------|
| **Class Asserted In** | ALATaxonomyInterpreter |
| **Method Asserted By** | alaSourceQualityChecks |
| **Assertion Logic** | neither scientificName nor vernacularName have been supplied |

**Actions**

I would change this to SCIENTIFIC_NAME_NOT_SUPPLIED and only check for scientificName. I am with Cam that we should not try to match vernacular names.

---

## NEGATED_LATITUDE

| Field | Value |
|-------|-------|
| Status | Replaced by PRESUMED_NEGATED_LATITUDE |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/NEGATED_LATITUDE |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+NEGATED_LATITUDE&type=code |

---

## NEGATED_LONGITUDE

| Field | Value |
|-------|-------|
| Status | Replaced by PRESUMED_NEGATED_LATITUDE. |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/NEGATED_LONGITUDE |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+NEGATED_LONGITUDE&type=code |

---

## OCCURRENCE_IS_CULTIVATED_OR_ESCAPEE

| Field | Value |
|-------|-------|
| Status | Not implemented |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/OCCURRENCE_IS_CULTIVATED_OR_ESCAPEE |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+OCCURRENCE_IS_CULTIVATED_OR_ESCAPEE&type=code |

---

## OCCURRENCE_IS_EXTRALIMITAL

| Field | Value |
|-------|-------|
| Status | Not implemented |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/OCCURRENCE_IS_EXTRALIMITAL |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+OCCURRENCE_IS_EXTRALIMITAL&type=code |

---

## OCCURRENCE_STATUS_INFERRED_FROM_BASIS_OF_RECORD

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 1200.0 |
| Recommendation | Keep |
| DwC Class | Record Level<br>dwc:Occurrence |
| DwC Terms | dwc:basisOfRecord<br>dwc:occurrenceStatus |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/OCCURRENCE_STATUS_INFERRED_FROM_BASIS_OF_RECORD |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+OCCURRENCE_STATUS_INFERRED_FROM_BASIS_OF_RECORD&type=code |

**GBIF**

| Field | Value |
|-------|-------|
| **Class Asserted In** | BasicInterpreter |
| **Method Asserted By** | interpretOccurrenceStatus |
| **Assertion Logic** | If there is a specimen, occurrenceStatus is 'present'. |

**Actions**

No action required

---

## OCCURRENCE_STATUS_INFERRED_FROM_INDIVIDUAL_COUNT

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 1797103.0 |
| Recommendation | Keep |
| DwC Class | dwc:Occurrence |
| DwC Terms | individualCount<br>dwc:occurrenceStatus |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/OCCURRENCE_STATUS_INFERRED_FROM_INDIVIDUAL_COUNT |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+OCCURRENCE_STATUS_INFERRED_FROM_INDIVIDUAL_COUNT&type=code |

**GBIF**

| Field | Value |
|-------|-------|
| **Class Asserted In** | BasicInterpreter |
| **Method Asserted By** | interpretOccurrenceStatus |
| **Assertion Logic** | occurrenceStatus is 'absent' if indivudualCount is 0 and 'present' if individualCount is greater than 0. |

**Actions**

No action required

---

## OCCURRENCE_STATUS_UNPARSABLE

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 384.0 |
| Recommendation | Keep |
| DwC Class | dwc:Occurrence |
| DwC Terms | dwc:occurrenceStatus |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/OCCURRENCE_STATUS_UNPARSABLE |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+OCCURRENCE_STATUS_UNPARSABLE&type=code |

**GBIF**

| Field | Value |
|-------|-------|
| **Class Asserted In** | BasicInterpreter |
| **Method Asserted By** | interpretOccurrenceStatus |
| **Assertion Logic** | occurrenceStatus has been provided but is unparsable |

**Actions**

No action required

---

## OCCURRENCE_VERIFIED

| Field | Value |
|-------|-------|
| Status | Not implemented |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/OCCURRENCE_VERIFIED |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+OCCURRENCE_VERIFIED&type=code |

---

## POSSIBLY_ON_LOAN

| Field | Value |
|-------|-------|
| Status | Unused |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/POSSIBLY_ON_LOAN |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+POSSIBLY_ON_LOAN&type=code |

---

## PRECISION_RANGE_MISMATCH

| Field | Value |
|-------|-------|
| Status | Replaced by COORDINATE_PRECISION_INVALID |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/PRECISION_RANGE_MISMATCH |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+PRECISION_RANGE_MISMATCH&type=code |

---

## PRESUMED_NEGATED_LATITUDE

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 12337.0 |
| Recommendation | Keep |
| DwC Class | dcterms:Location |
| DwC Terms | dwc:decimalLatitude |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/PRESUMED_NEGATED_LATITUDE |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+PRESUMED_NEGATED_LATITUDE&type=code |

**GBIF**

| Field | Value |
|-------|-------|
| **Class Asserted In** | CoordinatesFunction |
| **Method Asserted By** | getIssueTypes |
| **Assertion Logic** | The value for latitude has probably been negated, e.g., by forgetting to add the '-' for Southern Hemisphere latitudes. |

**Actions**

No action required

---

## PRESUMED_NEGATED_LONGITUDE

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 7937.0 |
| Recommendation | Keep |
| DwC Class | dcterms:Location |
| DwC Terms | dwc:decimalLongitude |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/PRESUMED_NEGATED_LONGITUDE |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+PRESUMED_NEGATED_LONGITUDE&type=code |

**GBIF**

| Field | Value |
|-------|-------|
| **Class Asserted In** | CoordinatesFunction |
| **Method Asserted By** | getIssueTypes |
| **Assertion Logic** | The value for longitude has probably been negated, e.g., by forgetting to add the '-' for Western Hemisphere latitudes. |

**Actions**

No action required

---

## PRESUMED_SWAPPED_COORDINATE

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 6655.0 |
| Recommendation | Keep |
| DwC Class | dcterms:Location |
| DwC Terms | dwc:decimalLatitude<br>dwc:decimalLongitude |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/PRESUMED_SWAPPED_COORDINATE |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+PRESUMED_SWAPPED_COORDINATE&type=code |

**GBIF**

| Field | Value |
|-------|-------|
| **Class Asserted In** | CoordinatesFunction |
| **Method Asserted By** | getIssueTypes |
| **Assertion Logic** | Latitude and longitude have likely been swapped. |

**Actions**

No action required

---

## RECORDED_DATE_INVALID

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 3435118.0 |
| Recommendation | Keep |
| DwC Class | dwc:Event |
| DwC Terms | dwc:eventDate<br>dwc:year<br>dwc:month<br>dwc:day<br>dwc:startDayOfYear<br>dwc:endDayOfYear |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/RECORDED_DATE_INVALID |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+RECORDED_DATE_INVALID&type=code |

**GBIF**

| Field | Value |
|-------|-------|
| **Class Asserted In** | https://github.com/gbif/parsers/blob/master/src/main/java/org/gbif/common/parsers/date/MultiinputTemporalParser.java |
| **Method Asserted By** | parseRecordedDate |
| **Assertion Logic** | Only one of `eventDate`, or `year`-`month`-`day`, or `startDayOfYear`-`endDayOfYear` has to be invalid for this assertion to be issued. |

**Actions**

No action required

---

## RECORDED_DATE_MISMATCH

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 143596.0 |
| Recommendation | Keep |
| DwC Class | dwc:Event |
| DwC Terms | dwc:eventDate<br>dwc:year<br>dwc:month<br>dwc:day<br>dwc:startDayOfYear<br>dwc:endDayOfYear |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/RECORDED_DATE_MISMATCH |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+RECORDED_DATE_MISMATCH&type=code |

**GBIF**

| Field | Value |
|-------|-------|
| **Class Asserted In** | https://github.com/gbif/parsers/blob/master/src/main/java/org/gbif/common/parsers/date/MultiinputTemporalParser.java |
| **Method Asserted By** | parseRecordedDate |
| **Assertion Logic** | One of `eventDate`, `year`-`month`-`day`, `startDayOfYear`, `endDayOfYear` is in contradiction with the others. |

**Actions**

No action required

---

## RECORDED_DATE_UNLIKELY

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 256440.0 |
| Recommendation | Keep |
| DwC Class | dwc:Event |
| DwC Terms | dwc:eventDate<br>dwc:year<br>dwc:month<br>dwc:day<br>dwc:startDayOfYear<br>dwc:endDayOfYear |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/RECORDED_DATE_UNLIKELY |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+RECORDED_DATE_UNLIKELY&type=code |

**GBIF**

| Field | Value |
|-------|-------|
| **Class Asserted In** | https://github.com/gbif/parsers/blob/master/src/main/java/org/gbif/common/parsers/date/MultiinputTemporalParser.java |
| **Method Asserted By** | parseRecordedDate |
| **Assertion Logic** | eventDate in the future, or before 1500 |

**Actions**

No action required

---

## REFERENCES_URI_INVALID

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 4705.0 |
| Recommendation | Keep |
| DwC Class | dwc:Occurrence<br>dwc:Identification |
| DwC Terms | associatedReferences<br>identificationReferences |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/REFERENCES_URI_INVALID |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+REFERENCES_URI_INVALID&type=code |

**GBIF**

| Field | Value |
|-------|-------|
| **Class Asserted In** | CoreInterpreter |
| **Method Asserted By** | interpretReferences |
| **Assertion Logic** | One of the provided references could not be parsed. |

**Actions**

No action required

---

## RESOURCE_TAXONOMIC_SCOPE_MISMATCH

| Field | Value |
|-------|-------|
| Status | Not implemented |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/RESOURCE_TAXONOMIC_SCOPE_MISMATCH |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+RESOURCE_TAXONOMIC_SCOPE_MISMATCH&type=code |

---

## SENSITIVITY_REPORT_INVALID

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 66599.0 |
| Recommendation | Keep |
| DwC Class | dcterms:Location<br>dwc:Taxon |
| DwC Terms | dwc:stateProvince<br>dwc:scientificName |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/SENSITIVITY_REPORT_INVALID |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+SENSITIVITY_REPORT_INVALID&type=code |

**ALA**

| Field | Value |
|-------|-------|
| **Class Asserted In** | SensitiveDataInterpreter |
| **Method Asserted By** | sensitiveDataInterpreter |
| **Assertion Logic** | Information received by the SDS cannot be interpreted. |

**Actions**

No action required

---

## SENSITIVITY_REPORT_NOT_LOADABLE

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 66599.0 |
| Recommendation | Keep |
| DwC Class | dcterms:Location<br>dwc:Taxon |
| DwC Terms | dwc:stateProvince<br>dwc:scientificName |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/SENSITIVITY_REPORT_NOT_LOADABLE |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+SENSITIVITY_REPORT_NOT_LOADABLE&type=code |

**ALA**

| Field | Value |
|-------|-------|
| **Class Asserted In** | SensitiveDataInterpreter |
| **Method Asserted By** | sensitiveDataInterpreter |
| **Assertion Logic** | Sensitivity rules for the taxon at the locality could not be loaded, perhaps due to unavailability of the SDS. |

**Actions**

No action required

---

## SPECIES_OUTSIDE_EXPERT_RANGE

| Field | Value |
|-------|-------|
| Status | Not implemented |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/SPECIES_OUTSIDE_EXPERT_RANGE |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+SPECIES_OUTSIDE_EXPERT_RANGE&type=code |

---

## STATEPROVINCE_COORDINATE_MISMATCH

| Field | Value |
|-------|-------|
| Status | Replaced by STATE_COORDINATE_MISMATCH |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/STATEPROVINCE_COORDINATE_MISMATCH |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+STATEPROVINCE_COORDINATE_MISMATCH&type=code |

---

## STATE_COORDINATE_MISMATCH

| Field | Value |
|-------|-------|
| Count | 932957.0 |
| Recommendation | Keep |
| DwC Class | dcterms:Location |
| DwC Terms | dwc:stateProvince<br>dwc:decimalLatitude<br>dwc:decimalLongitude<br>dwc:verbatimLatitude<br>dwc:verbatimLongitude<br>dwc:verbatimCoordinates |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/STATE_COORDINATE_MISMATCH |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+STATE_COORDINATE_MISMATCH&type=code |

**ALA**

| Field | Value |
|-------|-------|
| **Class Asserted In** | ALALocationInterpreter |
| **Method Asserted By** | verifyLocationInfo |
| **Assertion Logic** | stateProvince retrieved using the coordinates is different from the provided stateProvince |

**Actions**

No action required

---

## TAXON_AFFINITY_SPECIES

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 24313.0 |
| Recommendation | Keep |
| DwC Class | dwc:Taxon |
| DwC Terms | dwc:scientificName |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/TAXON_AFFINITY_SPECIES |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+TAXON_AFFINITY_SPECIES&type=code |

**ALA**

| Field | Value |
|-------|-------|
| **Class Asserted In** | ALATaxonomyInterpreter |
| **Method Asserted By** | ISSUE_MAP |
| **Assertion Logic** | scientificName includes 'aff.'. This can be an identificationQualifier, but could also indicate a distinct entity, meaning that the taxon that the name is matched to will be a different taxon than that with the provided scientificName. Also, including these qualifiers in the scientific name is invalid Darwin Core. |

**Actions**

No action required

---

## TAXON_CONFER_SPECIES

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 33262.0 |
| Recommendation | Keep |
| DwC Class | dwc:Taxon |
| DwC Terms | dwc:scientificName |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/TAXON_CONFER_SPECIES |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+TAXON_CONFER_SPECIES&type=code |

**ALA**

| Field | Value |
|-------|-------|
| **Class Asserted In** | ALATaxonomyInterpreter |
| **Method Asserted By** | ISSUE_MAP |
| **Assertion Logic** | scientificName includes 'cf.' indicating an uncertain identification. Including identification qualiers in the scientificName is invalid Darwin Core. |

**Actions**

No action required

---

## TAXON_DEFAULT_MATCH

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 87907.0 |
| Recommendation | Keep |
| DwC Class | dwc:Taxon |
| DwC Terms | dwc:scientificName |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/TAXON_DEFAULT_MATCH |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+TAXON_DEFAULT_MATCH&type=code |

**ALA**

| Field | Value |
|-------|-------|
| **Class Asserted In** | ALATaxonomyInterpreter |
| **Method Asserted By** | alaResultQualityChecks |
| **Assertion Logic** | Check whether the matched taxon matches a supplied default name (I presume this is a default in a Darwin Core Archive). |

**Actions**

No action required

---

## TAXON_ERROR

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 644.0 |
| Recommendation | Keep |
| DwC Class | dwc:Taxon |
| DwC Terms | dwc:scientificName |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/TAXON_ERROR |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+TAXON_ERROR&type=code |

**ALA**

| Field | Value |
|-------|-------|
| **Class Asserted In** | ALATaxonomyInterpreter |
| **Method Asserted By** | ISSUE_MAP |
| **Assertion Logic** | Scientific name either not provided or could not be interpreted. |

**Actions**

No action required

---

## TAXON_EXCLUDED

| Field | Value |
|-------|-------|
| Status | Ostensibly unused |
| Recommendation | Keep |
| DwC Class | dwc:Taxon |
| DwC Terms | dwc:scientificName |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/TAXON_EXCLUDED |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+TAXON_EXCLUDED&type=code |

**ALA**

| Field | Value |
|-------|-------|
| **Class Asserted In** | ALATaxonomyInterpreter |
| **Method Asserted By** | ISSUE_MAP |
| **Assertion Logic** | The taxon name supplied with a record has been matched to a taxon that is not known to occur in Australia. |

**Actions**

Find out why this assertion is never made, as there are lots of records to which this applies.

---

## TAXON_EXCLUDED_ASSOCIATED

| Field | Value |
|-------|-------|
| Status | Ostensibly unused |
| Recommendation | Keep |
| DwC Class | dwc:Taxon |
| DwC Terms | dwc:scientificName |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/TAXON_EXCLUDED_ASSOCIATED |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+TAXON_EXCLUDED_ASSOCIATED&type=code |

**ALA**

| Field | Value |
|-------|-------|
| **Class Asserted In** | ALATaxonomyInterpreter |
| **Method Asserted By** | ISSUE_MAP |
| **Assertion Logic** | The taxon name supplied with a record has been matched to a taxon that is not known to occur in Australia, but can be matched to an Australian taxon because of information provided by the name authorities. |

**Actions**

Find out why this assertion is never made, as there are lots of records to which this applies.

---

## TAXON_HOMONYM

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 425212.0 |
| Recommendation | Keep |
| DwC Class | dwc:Taxon |
| DwC Terms | dwc:scientificName |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/TAXON_HOMONYM |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+TAXON_HOMONYM&type=code |

**ALA**

| Field | Value |
|-------|-------|
| **Class Asserted In** | ALATaxonomyInterpreter |
| **Method Asserted By** | ISSUE_MAP |
| **Assertion Logic** | The provided name matches more than one name in the ALA taxonomy and insufficient additional taxonomic data was supplied to make an unambiguous match. |

**Actions**

No action required

---

## TAXON_INDETERMINATE_SPECIES

| Field | Value |
|-------|-------|
| Status | Ostensibly unused |
| Recommendation | Keep |
| DwC Class | dwc:Taxon |
| DwC Terms | dwc:scientificName |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/TAXON_INDETERMINATE_SPECIES |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+TAXON_INDETERMINATE_SPECIES&type=code |

**ALA**

| Field | Value |
|-------|-------|
| **Class Asserted In** | ALATaxonomyInterpreter |
| **Method Asserted By** | ISSUE_MAP |
| **Assertion Logic** | The provided taxon name ends with 'sp.', indicating that the specimen could not be (or was not) identified to species. In the ALA name matching the suffix will be removed. |

**Actions**

This is a useful test, so we should have it.

---

## TAXON_MATCH_AGGREGATE

| Field | Value |
|-------|-------|
| Status | Ostensibly unused |
| Recommendation | Keep |
| DwC Class | dwc:Taxon |
| DwC Terms | dwc:scientificName |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/TAXON_MATCH_AGGREGATE |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+TAXON_MATCH_AGGREGATE&type=code |

**ALA**

| Field | Value |
|-------|-------|
| **Assertion Logic** | Matching is done at the species level, but the provided identification indicates a species aggregate (presumably though 's.l.' or 'agg.' suffixes), meaning too precise a match. |

**Actions**

This is a useful test, so we should have it.

---

## TAXON_MATCH_FUZZY

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 1539525.0 |
| Recommendation | Keep |
| DwC Class | dwc:Taxon |
| DwC Terms | dwc:scientificName |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/TAXON_MATCH_FUZZY |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+TAXON_MATCH_FUZZY&type=code |

**GBIF**

| Field | Value |
|-------|-------|
| **Class Asserted In** | TaxonomyInterpreter |
| **Method Asserted By** | matchTaxon |
| **Assertion Logic** | Taxon match is based on a fuzzy, so not exact, match of the name. This means that if the match is correct there must be a spelling error in the provided name. |

**ALA**

| Field | Value |
|-------|-------|
| **Class Asserted In** | ALATaxonomyInterpreter |
| **Method Asserted By** | alaResultQualityChecks |
| **Assertion Logic** | Taxon match is based on a fuzzy, so not exact, match of the name. This means that if the match is correct there must be a spelling error in the provided name. |

**Actions**

No action required

---

## TAXON_MATCH_HIGHERRANK

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 9813658.0 |
| Recommendation | Keep |
| DwC Class | dwc:Taxon |
| DwC Terms | dwc:scientificName<br>dwc:kingdom<br>dwc:phylum<br>dwc:class<br>dwc:order<br>dwc:family<br>dwc:genus |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/TAXON_MATCH_HIGHERRANK |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+TAXON_MATCH_HIGHERRANK&type=code |

**GBIF**

| Field | Value |
|-------|-------|
| **Class Asserted In** | TaxonomyInterpreter |
| **Method Asserted By** | matchTaxon |
| **Assertion Logic** | Name could not be matched to a taxon of the same rank, so is matched to a higher taxon, base on the other taxonomic information provided. |

**ALA**

| Field | Value |
|-------|-------|
| **Class Asserted In** | ALATaxonomyInterpreter |
| **Method Asserted By** | alaResultQualityChecks |
| **Assertion Logic** | Name could not be matched to a taxon of the same rank, so is matched to a higher taxon, base on the other taxonomic information provided. |

**Actions**

No action required

---

## TAXON_MATCH_NONE

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 750876.0 |
| Recommendation | Keep |
| DwC Class | dwc:Taxon |
| DwC Terms | dwc:scientificName<br>dwc:kingdom<br>dwc:phylum<br>dwc:class<br>dwc:order<br>dwc:family<br>dwc:genus |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/TAXON_MATCH_NONE |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+TAXON_MATCH_NONE&type=code |

**GBIF**

| Field | Value |
|-------|-------|
| **Class Asserted In** | TaxonomyInterpreter |
| **Method Asserted By** | matchTaxon |
| **Assertion Logic** | Name could not be matched to taxon in taxonomy. |

**ALA**

| Field | Value |
|-------|-------|
| **Class Asserted In** | ALATaxonomyInterpreter |
| **Method Asserted By** | ISSUE_MAP |
| **Assertion Logic** | Name could not be matched to taxonomy. |

**Actions**

No action required

---

## TAXON_MISAPPLIED

| Field | Value |
|-------|-------|
| Status | Unused |
| DwC Class | dwc:Taxon |
| DwC Terms | dwc:scientificName |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/TAXON_MISAPPLIED |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+TAXON_MISAPPLIED&type=code |

**ALA**

| Field | Value |
|-------|-------|
| **Class Asserted In** | ALATaxonomyInterpreter |
| **Method Asserted By** | ISSUE_MAP |
| **Assertion Logic** | Provided name is involved in misapplication. |

**Actions**

This test is not needed if we make sure that misapplications do not make it into the ALA taxonomy.

---

## TAXON_MISAPPLIED_MATCHED

| Field | Value |
|-------|-------|
| Status | Ostensibly unused |
| DwC Class | dwc:Taxon |
| DwC Terms | dwc:scientificName |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/TAXON_MISAPPLIED_MATCHED |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+TAXON_MISAPPLIED_MATCHED&type=code |

**ALA**

| Field | Value |
|-------|-------|
| **Class Asserted In** | ALATaxonomyInterpreter |
| **Method Asserted By** | ISSUE_MAP |
| **Assertion Logic** | Provided name is involved in misapplication and has been matched to a taxon with a different name. |

**Actions**

I hope indeed this never happens, as the data indicates, but we have evidence to the contrary.

---

## TAXON_PARENT_CHILD_SYNONYM

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 16744326.0 |
| Recommendation | Remove |
| DwC Class | dwc:Taxon |
| DwC Terms | dwc:scientificName |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/TAXON_PARENT_CHILD_SYNONYM |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+TAXON_PARENT_CHILD_SYNONYM&type=code |

**ALA**

| Field | Value |
|-------|-------|
| **Class Asserted In** | ALATaxonomyInterpreter |
| **Method Asserted By** | ISSUE_MAP |
| **Assertion Logic** | The supplied name can be matched either onto the parent species or a type subspecies (or variety presumably). |

**Actions**

This is just silly. They are completely different name strings.

---

## TAXON_QUESTION_SPECIES

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 49460.0 |
| Recommendation | Keep |
| DwC Class | dwc:Taxon |
| DwC Terms | dwc:scientificName |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/TAXON_QUESTION_SPECIES |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+TAXON_QUESTION_SPECIES&type=code |

**ALA**

| Field | Value |
|-------|-------|
| **Class Asserted In** | ALATaxonomyInterpreter |
| **Method Asserted By** | ISSUE_MAP |
| **Assertion Logic** | The supplied scientific name contains a question mark. This indicates an uncertain identification and is invalid Darwin Core. |

**Actions**

No action required.

---

## TAXON_SCOPE_MISMATCH

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 7124.0 |
| Recommendation | Keep |
| DwC Class | dwc:Taxon |
| DwC Terms | dwc:scientificName<br>dwc:kingdom<br>dwc:phylum<br>dwc:class<br>dwc:order<br>dwc:family<br>dwc:genus |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/TAXON_SCOPE_MISMATCH |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+TAXON_SCOPE_MISMATCH&type=code |

**ALA**

| Field | Value |
|-------|-------|
| **Class Asserted In** | ALATaxonomyInterpreter |
| **Method Asserted By** | ISSUE_MAP |
| **Assertion Logic** | The other taxonomic hints supplied with the data (classification) do not match the matched taxon. |

**Actions**

No action required. Maybe provide a better description.

---

## TAXON_SPECIES_PLURAL

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 889207.0 |
| Recommendation | Keep |
| DwC Class | dwc:Taxon |
| DwC Terms | dwc:scientificName |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/TAXON_SPECIES_PLURAL |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+TAXON_SPECIES_PLURAL&type=code |

**ALA**

| Field | Value |
|-------|-------|
| **Class Asserted In** | ALATaxonomyInterpreter |
| **Method Asserted By** | ISSUE_MAP |
| **Assertion Logic** | Supplied scientificName contains a plural (e.g., 'spp.') marker, indicating that there are multiple species in the sample. |

**Actions**

No action required.

---

## TYPE_STATUS_INVALID

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 153641.0 |
| Recommendation | Remove |
| DwC Class | dwc:Identification |
| DwC Terms | dwc:typeStatus |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/TYPE_STATUS_INVALID |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+TYPE_STATUS_INVALID&type=code |

**GBIF**

| Field | Value |
|-------|-------|
| **Class Asserted In** | VocabularyInterpreter |
| **Method Asserted By** | interpretTypeStatus |
| **Assertion Logic** | The provided typeStatus cannot be found in the type status lookup. |

**Actions**

This comes from GBIF, so we probably cannot do much about it, but this test is wrong, as dwc:typeStatus is a free text string that contains the typeOfType and typifiedName. GBIF is comparing apples and oranges.

---

## UNCERTAINTY_IN_PRECISION

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 120944.0 |
| Recommendation | Remove |
| DwC Class | dcterms:dcterms:Location |
| DwC Terms | coordinatePrecision<br>dwc:coordinateUncertaintyInMeters |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/UNCERTAINTY_IN_PRECISION |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+UNCERTAINTY_IN_PRECISION&type=code |

**ALA**

| Field | Value |
|-------|-------|
| **Class Asserted In** | AlaLocationInterpreter |
| **Method Asserted By** | interpretCoordinateUncertaintyInMeters |
| **Assertion Logic** | dwc:coordinateUncertainty null or empty && dwc:coordinatePrecision > 1 |

**Actions**

This is a poorly conceived assertion, as it is more a suggestion as to why a value for dwc:coordinatePrecision might be invalid. A value higher than 1 for dwc:coordinatePrecision can just as easily have come from, e.g., dwc:minimumElevationInMeters. Replace with COORDINATE_PRECISION_INVALID assertion that is independent of dwc:coordinateUncertaintyInMeters.

---

## UNCERTAINTY_NOT_SPECIFIED

| Field | Value |
|-------|-------|
| Status | Confuddled with COORDINATE_UNCERTAINTY_METERS_INVALID |
| Recommendation | Keep |
| DwC Class | dcterms:Location |
| DwC Terms | dwc:coordinateUncertaintyInMeters |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/UNCERTAINTY_NOT_SPECIFIED |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+UNCERTAINTY_NOT_SPECIFIED&type=code |

**ALA**

| Field | Value |
|-------|-------|
| **Class Asserted In** | x |
| **Method Asserted By** | x |
| **Assertion Logic** | x |

**Actions**

1. See COORDINATE_UNCERTAINTY_METERS_INVALID. When dwc:coordinateUncertaintyInMeters is null or empty, this issue should be asserted
2. Rename to MISSING_COORDINATE_UNCERTAINTY_METERS for consistency with other missing value issues.

---

## UNCERTAINTY_RANGE_MISMATCH

| Field | Value |
|-------|-------|
| Status | Not implemented. This seems to be the same as  COORDINATE_UNCERTAINTY_METERS_INVALID. |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/UNCERTAINTY_RANGE_MISMATCH |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+UNCERTAINTY_RANGE_MISMATCH&type=code |

---

## UNKNOWN_COUNTRY_NAME

| Field | Value |
|-------|-------|
| Status | Replaced by COUNTRY_INVALID |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/UNKNOWN_COUNTRY_NAME |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+UNKNOWN_COUNTRY_NAME&type=code |

---

## UNKNOWN_KINGDOM

| Field | Value |
|-------|-------|
| Count | 354529.0 |
| Recommendation | Keep |
| DwC Class | dwc:Taxon |
| DwC Terms | dwc:kingdom |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/UNKNOWN_KINGDOM |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+UNKNOWN_KINGDOM&type=code |

**ALA**

| Field | Value |
|-------|-------|
| **Class Asserted In** | ALATaxonomyInterpreter |
| **Method Asserted By** | alaSourceQualityChecks |
| **Assertion Logic** | Provided kingdom not recognised |

**Actions**

No action required

---

## UNRECOGNISED_COLLECTIONCODE

| Field | Value |
|-------|-------|
| Status | Not implemented. |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/UNRECOGNISED_COLLECTIONCODE |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+UNRECOGNISED_COLLECTIONCODE&type=code |

---

## UNRECOGNISED_COLLECTION_CODE

| Field | Value |
|-------|-------|
| Status | Not implemented. |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/UNRECOGNISED_COLLECTION_CODE |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+UNRECOGNISED_COLLECTION_CODE&type=code |

---

## UNRECOGNISED_INSTITUTIONCODE

| Field | Value |
|-------|-------|
| Status | Not implemented. |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/UNRECOGNISED_INSTITUTIONCODE |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+UNRECOGNISED_INSTITUTIONCODE&type=code |

---

## UNRECOGNISED_INSTITUTION_CODE

| Field | Value |
|-------|-------|
| Status | Not implemented. |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/UNRECOGNISED_INSTITUTION_CODE |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+UNRECOGNISED_INSTITUTION_CODE&type=code |

---

## UNRECOGNISED_TYPESTATUS

| Field | Value |
|-------|-------|
| Status | Replaced by TYPE_STATUS_INVALID |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/UNRECOGNISED_TYPESTATUS |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+UNRECOGNISED_TYPESTATUS&type=code |

---

## ZERO_COORDINATE

| Field | Value |
|-------|-------|
| Status | Active |
| Count | 2628.0 |
| Recommendation | Keep |
| DwC Class | dcterms:Location |
| DwC Terms | dwc:decimalLatitude<br>dwc:decimalLongitude<br>dwc:verbatimLatitude<br>dwc:verbatimLongitude<br>dwc:verbatimCoordinates |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/ZERO_COORDINATE |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+ZERO_COORDINATE&type=code |

**GBIF**

| Field | Value |
|-------|-------|
| **Class Asserted In** | CoordinateParseUtils |
| **Method Asserted By** | validateAndRound |
| **Assertion Logic** | Provided coordinates are both 0 |

**Actions**

No action required

---

## ZERO_COORDINATES

| Field | Value |
|-------|-------|
| Status | Not implemented |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/ZERO_COORDINATES |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+ZERO_COORDINATES&type=code |

---

## ZERO_LATITUDE_COORDINATES

| Field | Value |
|-------|-------|
| Status | Not implemented |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/ZERO_LATITUDE_COORDINATES |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+ZERO_LATITUDE_COORDINATES&type=code |

---

## ZERO_LONGITUDE_COORDINATES

| Field | Value |
|-------|-------|
| Status | Not implemented |
| Wiki Page | https://github.com/AtlasOfLivingAustralia/ala-dataquality/wiki/ZERO_LONGITUDE_COORDINATES |
| GitHub Search | https://github.com/search?q=repo%3Agbif%2Fpipelines+ZERO_LONGITUDE_COORDINATES&type=code |

---

