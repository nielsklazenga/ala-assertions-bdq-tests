# ALA Assertions Missing Metadata

## Missing both class and terms (65)

| Assertion | Status | Recommendation |
|-----------|--------|----------------|
| BADLY_FORMED_ALTITUDE | Not implemented | Remove |
| BADLY_FORMED_BASIS_OF_RECORD | Not implemented | Remove |
| BASIS_OF_RECORD_INVALID | Active | Keep |
| COLLECTING_PATTERNS_GENERAL | Not implemented | Remove |
| COORDINATES_OUT_OF_RANGE | Not implemented (probably a typo for COORDINATE_OUT_OF_RANGE) | Remove |
| COORDINATE_ACCURACY_INVALID | Not implemented (probably replaced by COORDINATE_PRECISION_INVALID and COORDINATE_UNCERTAINTY_METERS_INVALID) | Remove |
| COORDINATE_HABITAT_MISMATCH | Not implemented | Remove |
| COORDINATE_PRECISION_INVALID | Active | Keep |
| COORDINATE_PRECISION_MISMATCH | Not implemented (probably error for COORDINATE_PRECISION_UNCERTAINTY_MISMATCH) | Remove |
| COORDINATE_PRECISION_UNCERTAINTY_MISMATCH | Unused (listed among evaluation types, but there is no code for it; it could be among other location assertions, but this seems to be something that requires special code) | Remove |
| COORDINATE_REPROJECTION_SUSPICIOUS | Active | Keep |
| COORDINATE_ROUNDED | Active |  |
| DATA_ARE_GENERALISED | Not implemented | Remove |
| DATE_PRECISION_MISMATCH | Not implemented | Remove |
| DAY_MONTH_TRANSPOSED | Not implemented | Remove |
| DECIMAL_LAT_LONG_CALCULATION_FROM_EASTING_NORTHING_FAILED | Not implemented | Remove |
| DECIMAL_LAT_LONG_CONVERSION_FAILED | Not implemented | Remove |
| DEPTH_OUT_OF_RANGE | Not implemented | Remove |
| DETECTED_OUTLIER_GEOGRAPHIC | Not implemented | Remove |
| DETECTED_OUTLIER_JACKKNIFE | Not a data quality assertion anymore: we use the outlier_layer and outlier_layer_count filters for this | ? |
| DETECTED_OUTLIER_OTHER | Not implemented |  |
| DIFFERENT_OWNER_INSTITUTION | Unused | Keep |
| GEOREFERENCED_DATE_INVALID | Unused |  |
| GEOREFERENCE_UNCERTAIN | Not implemented | Remove |
| GEOREFERENCE_VERIFIED | Not implemented | Remove |
| HOMONYM_ISSUE | Not implemented | Remove |
| IDENTIFICATION_UNCERTAIN | Not implemented | Remove |
| IDENTIFICATION_VERIFIED | Not implemented | Remove |
| ID_PRE_OCCURRENCE | Active | Keep |
| INFERRED_DUPLICATE_RECORD | Not a data quality assertion anymore: we use the duplicate_status filter for this |  |
| INFERRED_FALSE_PRECISION | Not implemented |  |
| INSTITUTION_COLLECTION_MISMATCH | Unused | Keep |
| INSTITUTION_MATCH_FUZZY | Unused | Keep |
| INSTITUTION_MATCH_NONE | Unused | Keep |
| INTERPRETATION_ERROR | Unused |  |
| INVALID_COLLECTION_DATE | Not implemented |  |
| INVALID_GEODETICDATUM | Not implemented. Replaced by GEODETIC_DATUM_INVALID. |  |
| INVALID_IMAGE_URL | Not implemented |  |
| INVERTED_COORDINATES | Not implemented |  |
| LOCATION_NOT_SUPPLIED | Active | Keep |
| MIN_MAX_ALTITUDE_REVERSED | Not implemented. Replaced by ELEVATION_MIN_MAX_SWAPPED. |  |
| MIN_MAX_DEPTH_REVERSED | Not implementedReplaced by DEPTH_MIN_MAX_SWAPPED. |  |
| MISSING_BASIS_OF_RECORD | Not implemented |  |
| MISSING_COORDINATEPRECISION | Unused |  |
| MISSING_DATEIDENTIFIED | Not implemented |  |
| NEGATED_LATITUDE | Replaced by PRESUMED_NEGATED_LATITUDE |  |
| NEGATED_LONGITUDE | Replaced by PRESUMED_NEGATED_LATITUDE. |  |
| OCCURRENCE_IS_CULTIVATED_OR_ESCAPEE | Not implemented |  |
| OCCURRENCE_IS_EXTRALIMITAL | Not implemented |  |
| OCCURRENCE_VERIFIED | Not implemented |  |
| POSSIBLY_ON_LOAN | Unused |  |
| PRECISION_RANGE_MISMATCH | Replaced by COORDINATE_PRECISION_INVALID |  |
| RESOURCE_TAXONOMIC_SCOPE_MISMATCH | Not implemented |  |
| SPECIES_OUTSIDE_EXPERT_RANGE | Not implemented |  |
| STATEPROVINCE_COORDINATE_MISMATCH | Replaced by STATE_COORDINATE_MISMATCH |  |
| UNCERTAINTY_RANGE_MISMATCH | Not implemented. This seems to be the same as  COORDINATE_UNCERTAINTY_METERS_INVALID. |  |
| UNKNOWN_COUNTRY_NAME | Replaced by COUNTRY_INVALID |  |
| UNRECOGNISED_COLLECTIONCODE | Not implemented. |  |
| UNRECOGNISED_COLLECTION_CODE | Not implemented. |  |
| UNRECOGNISED_INSTITUTIONCODE | Not implemented. |  |
| UNRECOGNISED_INSTITUTION_CODE | Not implemented. |  |
| UNRECOGNISED_TYPESTATUS | Replaced by TYPE_STATUS_INVALID |  |
| ZERO_COORDINATES | Not implemented |  |
| ZERO_LATITUDE_COORDINATES | Not implemented |  |
| ZERO_LONGITUDE_COORDINATES | Not implemented |  |

## Missing dwc_class (0)

| Assertion | Status | Recommendation |
|-----------|--------|----------------|

## Missing dwc_terms (0)

| Assertion | Status | Recommendation |
|-----------|--------|----------------|

