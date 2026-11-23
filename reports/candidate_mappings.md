# Candidate Mappings

Potential ALA Assertion ↔ BDQ Test associations grouped by BDQ class and based on shared Darwin Core terms.

## Record Level

| ALA Assertion | BDQ Test | Connecting Terms | ALA-only Terms | BDQ-only Terms |
|---------------|----------|------------------|----------------|----------------|
| OCCURRENCE_STATUS_INFERRED_FROM_BASIS_OF_RECORD | AMENDMENT_BASISOFRECORD_STANDARDIZED | basisOfRecord | occurrenceStatus |  |
| OCCURRENCE_STATUS_INFERRED_FROM_BASIS_OF_RECORD | VALIDATION_BASISOFRECORD_NOTEMPTY | basisOfRecord | occurrenceStatus |  |
| OCCURRENCE_STATUS_INFERRED_FROM_BASIS_OF_RECORD | VALIDATION_BASISOFRECORD_STANDARD | basisOfRecord | occurrenceStatus |  |

## dcterms:Location

| ALA Assertion | BDQ Test | Connecting Terms | ALA-only Terms | BDQ-only Terms |
|---------------|----------|------------------|----------------|----------------|
| ALTITUDE_IN_FEET | AMENDMENT_MINELEVATIONMAXELEVATION_FROM_VERBATIM | maximumElevationInMeters, minimumElevationInMeters |  |  |
| ALTITUDE_IN_FEET | VALIDATION_MAXELEVATION_INRANGE | maximumElevationInMeters | minimumElevationInMeters |  |
| ALTITUDE_IN_FEET | VALIDATION_MINELEVATION_INRANGE | minimumElevationInMeters | maximumElevationInMeters |  |
| ALTITUDE_IN_FEET | VALIDATION_MINELEVATION_LESSTHAN_MAXELEVATION | maximumElevationInMeters, minimumElevationInMeters |  |  |
| ALTITUDE_NON_NUMERIC | AMENDMENT_MINELEVATIONMAXELEVATION_FROM_VERBATIM | maximumElevationInMeters, minimumElevationInMeters |  |  |
| ALTITUDE_NON_NUMERIC | VALIDATION_MAXELEVATION_INRANGE | maximumElevationInMeters | minimumElevationInMeters |  |
| ALTITUDE_NON_NUMERIC | VALIDATION_MINELEVATION_INRANGE | minimumElevationInMeters | maximumElevationInMeters |  |
| ALTITUDE_NON_NUMERIC | VALIDATION_MINELEVATION_LESSTHAN_MAXELEVATION | maximumElevationInMeters, minimumElevationInMeters |  |  |
| ALTITUDE_OUT_OF_RANGE | AMENDMENT_MINELEVATIONMAXELEVATION_FROM_VERBATIM | maximumElevationInMeters, minimumElevationInMeters |  |  |
| ALTITUDE_OUT_OF_RANGE | VALIDATION_MAXELEVATION_INRANGE | maximumElevationInMeters | minimumElevationInMeters |  |
| ALTITUDE_OUT_OF_RANGE | VALIDATION_MINELEVATION_INRANGE | minimumElevationInMeters | maximumElevationInMeters |  |
| ALTITUDE_OUT_OF_RANGE | VALIDATION_MINELEVATION_LESSTHAN_MAXELEVATION | maximumElevationInMeters, minimumElevationInMeters |  |  |
| CONTINENT_COORDINATE_MISMATCH | AMENDMENT_COORDINATES_FROM_VERBATIM | decimalLatitude, decimalLongitude | continent | geodeticDatum |
| CONTINENT_COORDINATE_MISMATCH | AMENDMENT_COORDINATES_TRANSPOSED | decimalLatitude, decimalLongitude | continent |  |
| CONTINENT_COORDINATE_MISMATCH | ISSUE_COORDINATES_CENTEROFCOUNTRY | decimalLatitude, decimalLongitude | continent | countryCode |
| CONTINENT_COORDINATE_MISMATCH | VALIDATION_COORDINATESCOUNTRYCODE_CONSISTENT | decimalLatitude, decimalLongitude | continent | countryCode |
| CONTINENT_COORDINATE_MISMATCH | VALIDATION_COORDINATESSTATEPROVINCE_CONSISTENT | decimalLatitude, decimalLongitude | continent | stateProvince |
| CONTINENT_COORDINATE_MISMATCH | VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT | decimalLatitude, decimalLongitude | continent |  |
| CONTINENT_COORDINATE_MISMATCH | VALIDATION_COORDINATES_NOTZERO | decimalLatitude, decimalLongitude | continent |  |
| CONTINENT_COORDINATE_MISMATCH | VALIDATION_DECIMALLATITUDE_INRANGE | decimalLatitude | continent, decimalLongitude |  |
| CONTINENT_COORDINATE_MISMATCH | VALIDATION_DECIMALLATITUDE_NOTEMPTY | decimalLatitude | continent, decimalLongitude |  |
| CONTINENT_COORDINATE_MISMATCH | VALIDATION_DECIMALLONGITUDE_INRANGE | decimalLongitude | continent, decimalLatitude |  |
| CONTINENT_COORDINATE_MISMATCH | VALIDATION_DECIMALLONGITUDE_NOTEMPTY | decimalLongitude | continent, decimalLatitude |  |
| CONTINENT_COORDINATE_MISMATCH | VALIDATION_LOCATION_NOTEMPTY | continent, decimalLatitude, decimalLongitude |  | country, countryCode, county, footprintWKT, higherGeography, higherGeographyID, island, islandGroup, locality, locationID, municipality, stateProvince, verbatimCoordinates, verbatimLatitude, verbatimLocality, verbatimLongitude, waterBody |
| CONTINENT_COUNTRY_MISMATCH | VALIDATION_COUNTRYCOUNTRYCODE_CONSISTENT | country | continent | countryCode |
| CONTINENT_COUNTRY_MISMATCH | VALIDATION_COUNTRYSTATEPROVINCE_UNAMBIGUOUS | country | continent | stateProvince |
| CONTINENT_COUNTRY_MISMATCH | VALIDATION_COUNTRY_FOUND | country | continent |  |
| CONTINENT_COUNTRY_MISMATCH | VALIDATION_COUNTRY_NOTEMPTY | country | continent |  |
| CONTINENT_COUNTRY_MISMATCH | VALIDATION_LOCATION_NOTEMPTY | continent, country |  | countryCode, county, decimalLatitude, decimalLongitude, footprintWKT, higherGeography, higherGeographyID, island, islandGroup, locality, locationID, municipality, stateProvince, verbatimCoordinates, verbatimLatitude, verbatimLocality, verbatimLongitude, waterBody |
| CONTINENT_DERIVED_FROM_COORDINATES | AMENDMENT_COORDINATES_FROM_VERBATIM | decimalLatitude, decimalLongitude |  | geodeticDatum |
| CONTINENT_DERIVED_FROM_COORDINATES | AMENDMENT_COORDINATES_TRANSPOSED | decimalLatitude, decimalLongitude |  |  |
| CONTINENT_DERIVED_FROM_COORDINATES | ISSUE_COORDINATES_CENTEROFCOUNTRY | decimalLatitude, decimalLongitude |  | countryCode |
| CONTINENT_DERIVED_FROM_COORDINATES | VALIDATION_COORDINATESCOUNTRYCODE_CONSISTENT | decimalLatitude, decimalLongitude |  | countryCode |
| CONTINENT_DERIVED_FROM_COORDINATES | VALIDATION_COORDINATESSTATEPROVINCE_CONSISTENT | decimalLatitude, decimalLongitude |  | stateProvince |
| CONTINENT_DERIVED_FROM_COORDINATES | VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT | decimalLatitude, decimalLongitude |  |  |
| CONTINENT_DERIVED_FROM_COORDINATES | VALIDATION_COORDINATES_NOTZERO | decimalLatitude, decimalLongitude |  |  |
| CONTINENT_DERIVED_FROM_COORDINATES | VALIDATION_DECIMALLATITUDE_INRANGE | decimalLatitude | decimalLongitude |  |
| CONTINENT_DERIVED_FROM_COORDINATES | VALIDATION_DECIMALLATITUDE_NOTEMPTY | decimalLatitude | decimalLongitude |  |
| CONTINENT_DERIVED_FROM_COORDINATES | VALIDATION_DECIMALLONGITUDE_INRANGE | decimalLongitude | decimalLatitude |  |
| CONTINENT_DERIVED_FROM_COORDINATES | VALIDATION_DECIMALLONGITUDE_NOTEMPTY | decimalLongitude | decimalLatitude |  |
| CONTINENT_DERIVED_FROM_COORDINATES | VALIDATION_LOCATION_NOTEMPTY | decimalLatitude, decimalLongitude |  | continent, country, countryCode, county, footprintWKT, higherGeography, higherGeographyID, island, islandGroup, locality, locationID, municipality, stateProvince, verbatimCoordinates, verbatimLatitude, verbatimLocality, verbatimLongitude, waterBody |
| CONTINENT_DERIVED_FROM_COUNTRY | VALIDATION_COUNTRYCOUNTRYCODE_CONSISTENT | country |  | countryCode |
| CONTINENT_DERIVED_FROM_COUNTRY | VALIDATION_COUNTRYSTATEPROVINCE_UNAMBIGUOUS | country |  | stateProvince |
| CONTINENT_DERIVED_FROM_COUNTRY | VALIDATION_COUNTRY_FOUND | country |  |  |
| CONTINENT_DERIVED_FROM_COUNTRY | VALIDATION_COUNTRY_NOTEMPTY | country |  |  |
| CONTINENT_DERIVED_FROM_COUNTRY | VALIDATION_LOCATION_NOTEMPTY | country |  | continent, countryCode, county, decimalLatitude, decimalLongitude, footprintWKT, higherGeography, higherGeographyID, island, islandGroup, locality, locationID, municipality, stateProvince, verbatimCoordinates, verbatimLatitude, verbatimLocality, verbatimLongitude, waterBody |
| CONTINENT_INVALID | VALIDATION_LOCATION_NOTEMPTY | continent |  | country, countryCode, county, decimalLatitude, decimalLongitude, footprintWKT, higherGeography, higherGeographyID, island, islandGroup, locality, locationID, municipality, stateProvince, verbatimCoordinates, verbatimLatitude, verbatimLocality, verbatimLongitude, waterBody |
| COORDINATES_CENTRE_OF_COUNTRY | AMENDMENT_COORDINATES_FROM_VERBATIM | decimalLatitude, decimalLongitude | country, verbatimLatitude | geodeticDatum |
| COORDINATES_CENTRE_OF_COUNTRY | AMENDMENT_COORDINATES_TRANSPOSED | decimalLatitude, decimalLongitude | country, verbatimLatitude |  |
| COORDINATES_CENTRE_OF_COUNTRY | ISSUE_COORDINATES_CENTEROFCOUNTRY | decimalLatitude, decimalLongitude | country, verbatimLatitude | countryCode |
| COORDINATES_CENTRE_OF_COUNTRY | VALIDATION_COORDINATESCOUNTRYCODE_CONSISTENT | decimalLatitude, decimalLongitude | country, verbatimLatitude | countryCode |
| COORDINATES_CENTRE_OF_COUNTRY | VALIDATION_COORDINATESSTATEPROVINCE_CONSISTENT | decimalLatitude, decimalLongitude | country, verbatimLatitude | stateProvince |
| COORDINATES_CENTRE_OF_COUNTRY | VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT | decimalLatitude, decimalLongitude | country, verbatimLatitude |  |
| COORDINATES_CENTRE_OF_COUNTRY | VALIDATION_COORDINATES_NOTZERO | decimalLatitude, decimalLongitude | country, verbatimLatitude |  |
| COORDINATES_CENTRE_OF_COUNTRY | VALIDATION_COUNTRYCOUNTRYCODE_CONSISTENT | country | decimalLatitude, decimalLongitude, verbatimLatitude | countryCode |
| COORDINATES_CENTRE_OF_COUNTRY | VALIDATION_COUNTRYSTATEPROVINCE_UNAMBIGUOUS | country | decimalLatitude, decimalLongitude, verbatimLatitude | stateProvince |
| COORDINATES_CENTRE_OF_COUNTRY | VALIDATION_COUNTRY_FOUND | country | decimalLatitude, decimalLongitude, verbatimLatitude |  |
| COORDINATES_CENTRE_OF_COUNTRY | VALIDATION_COUNTRY_NOTEMPTY | country | decimalLatitude, decimalLongitude, verbatimLatitude |  |
| COORDINATES_CENTRE_OF_COUNTRY | VALIDATION_DECIMALLATITUDE_INRANGE | decimalLatitude | country, decimalLongitude, verbatimLatitude |  |
| COORDINATES_CENTRE_OF_COUNTRY | VALIDATION_DECIMALLATITUDE_NOTEMPTY | decimalLatitude | country, decimalLongitude, verbatimLatitude |  |
| COORDINATES_CENTRE_OF_COUNTRY | VALIDATION_DECIMALLONGITUDE_INRANGE | decimalLongitude | country, decimalLatitude, verbatimLatitude |  |
| COORDINATES_CENTRE_OF_COUNTRY | VALIDATION_DECIMALLONGITUDE_NOTEMPTY | decimalLongitude | country, decimalLatitude, verbatimLatitude |  |
| COORDINATES_CENTRE_OF_COUNTRY | VALIDATION_LOCATION_NOTEMPTY | country, decimalLatitude, decimalLongitude, verbatimLatitude |  | continent, countryCode, county, footprintWKT, higherGeography, higherGeographyID, island, islandGroup, locality, locationID, municipality, stateProvince, verbatimCoordinates, verbatimLocality, verbatimLongitude, waterBody |
| COORDINATES_CENTRE_OF_STATEPROVINCE | AMENDMENT_COORDINATES_FROM_VERBATIM | decimalLatitude, decimalLongitude | verbatimLatitude, verbatimLongitude | geodeticDatum |
| COORDINATES_CENTRE_OF_STATEPROVINCE | AMENDMENT_COORDINATES_TRANSPOSED | decimalLatitude, decimalLongitude | verbatimLatitude, verbatimLongitude |  |
| COORDINATES_CENTRE_OF_STATEPROVINCE | ISSUE_COORDINATES_CENTEROFCOUNTRY | decimalLatitude, decimalLongitude | verbatimLatitude, verbatimLongitude | countryCode |
| COORDINATES_CENTRE_OF_STATEPROVINCE | VALIDATION_COORDINATESCOUNTRYCODE_CONSISTENT | decimalLatitude, decimalLongitude | verbatimLatitude, verbatimLongitude | countryCode |
| COORDINATES_CENTRE_OF_STATEPROVINCE | VALIDATION_COORDINATESSTATEPROVINCE_CONSISTENT | decimalLatitude, decimalLongitude | verbatimLatitude, verbatimLongitude | stateProvince |
| COORDINATES_CENTRE_OF_STATEPROVINCE | VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT | decimalLatitude, decimalLongitude | verbatimLatitude, verbatimLongitude |  |
| COORDINATES_CENTRE_OF_STATEPROVINCE | VALIDATION_COORDINATES_NOTZERO | decimalLatitude, decimalLongitude | verbatimLatitude, verbatimLongitude |  |
| COORDINATES_CENTRE_OF_STATEPROVINCE | VALIDATION_DECIMALLATITUDE_INRANGE | decimalLatitude | decimalLongitude, verbatimLatitude, verbatimLongitude |  |
| COORDINATES_CENTRE_OF_STATEPROVINCE | VALIDATION_DECIMALLATITUDE_NOTEMPTY | decimalLatitude | decimalLongitude, verbatimLatitude, verbatimLongitude |  |
| COORDINATES_CENTRE_OF_STATEPROVINCE | VALIDATION_DECIMALLONGITUDE_INRANGE | decimalLongitude | decimalLatitude, verbatimLatitude, verbatimLongitude |  |
| COORDINATES_CENTRE_OF_STATEPROVINCE | VALIDATION_DECIMALLONGITUDE_NOTEMPTY | decimalLongitude | decimalLatitude, verbatimLatitude, verbatimLongitude |  |
| COORDINATES_CENTRE_OF_STATEPROVINCE | VALIDATION_LOCATION_NOTEMPTY | decimalLatitude, decimalLongitude, verbatimLatitude, verbatimLongitude |  | continent, country, countryCode, county, footprintWKT, higherGeography, higherGeographyID, island, islandGroup, locality, locationID, municipality, stateProvince, verbatimCoordinates, verbatimLocality, waterBody |
| COORDINATE_INVALID | AMENDMENT_COORDINATES_FROM_VERBATIM | decimalLatitude, decimalLongitude | verbatimLatitude, verbatimLongitude | geodeticDatum |
| COORDINATE_INVALID | AMENDMENT_COORDINATES_TRANSPOSED | decimalLatitude, decimalLongitude | verbatimLatitude, verbatimLongitude |  |
| COORDINATE_INVALID | ISSUE_COORDINATES_CENTEROFCOUNTRY | decimalLatitude, decimalLongitude | verbatimLatitude, verbatimLongitude | countryCode |
| COORDINATE_INVALID | VALIDATION_COORDINATESCOUNTRYCODE_CONSISTENT | decimalLatitude, decimalLongitude | verbatimLatitude, verbatimLongitude | countryCode |
| COORDINATE_INVALID | VALIDATION_COORDINATESSTATEPROVINCE_CONSISTENT | decimalLatitude, decimalLongitude | verbatimLatitude, verbatimLongitude | stateProvince |
| COORDINATE_INVALID | VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT | decimalLatitude, decimalLongitude | verbatimLatitude, verbatimLongitude |  |
| COORDINATE_INVALID | VALIDATION_COORDINATES_NOTZERO | decimalLatitude, decimalLongitude | verbatimLatitude, verbatimLongitude |  |
| COORDINATE_INVALID | VALIDATION_DECIMALLATITUDE_INRANGE | decimalLatitude | decimalLongitude, verbatimLatitude, verbatimLongitude |  |
| COORDINATE_INVALID | VALIDATION_DECIMALLATITUDE_NOTEMPTY | decimalLatitude | decimalLongitude, verbatimLatitude, verbatimLongitude |  |
| COORDINATE_INVALID | VALIDATION_DECIMALLONGITUDE_INRANGE | decimalLongitude | decimalLatitude, verbatimLatitude, verbatimLongitude |  |
| COORDINATE_INVALID | VALIDATION_DECIMALLONGITUDE_NOTEMPTY | decimalLongitude | decimalLatitude, verbatimLatitude, verbatimLongitude |  |
| COORDINATE_INVALID | VALIDATION_LOCATION_NOTEMPTY | decimalLatitude, decimalLongitude, verbatimLatitude, verbatimLongitude |  | continent, country, countryCode, county, footprintWKT, higherGeography, higherGeographyID, island, islandGroup, locality, locationID, municipality, stateProvince, verbatimCoordinates, verbatimLocality, waterBody |
| COORDINATE_OUT_OF_RANGE | AMENDMENT_COORDINATES_FROM_VERBATIM | decimalLatitude, decimalLongitude | verbatimLatitude, verbatimLongitude | geodeticDatum |
| COORDINATE_OUT_OF_RANGE | AMENDMENT_COORDINATES_TRANSPOSED | decimalLatitude, decimalLongitude | verbatimLatitude, verbatimLongitude |  |
| COORDINATE_OUT_OF_RANGE | ISSUE_COORDINATES_CENTEROFCOUNTRY | decimalLatitude, decimalLongitude | verbatimLatitude, verbatimLongitude | countryCode |
| COORDINATE_OUT_OF_RANGE | VALIDATION_COORDINATESCOUNTRYCODE_CONSISTENT | decimalLatitude, decimalLongitude | verbatimLatitude, verbatimLongitude | countryCode |
| COORDINATE_OUT_OF_RANGE | VALIDATION_COORDINATESSTATEPROVINCE_CONSISTENT | decimalLatitude, decimalLongitude | verbatimLatitude, verbatimLongitude | stateProvince |
| COORDINATE_OUT_OF_RANGE | VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT | decimalLatitude, decimalLongitude | verbatimLatitude, verbatimLongitude |  |
| COORDINATE_OUT_OF_RANGE | VALIDATION_COORDINATES_NOTZERO | decimalLatitude, decimalLongitude | verbatimLatitude, verbatimLongitude |  |
| COORDINATE_OUT_OF_RANGE | VALIDATION_DECIMALLATITUDE_INRANGE | decimalLatitude | decimalLongitude, verbatimLatitude, verbatimLongitude |  |
| COORDINATE_OUT_OF_RANGE | VALIDATION_DECIMALLATITUDE_NOTEMPTY | decimalLatitude | decimalLongitude, verbatimLatitude, verbatimLongitude |  |
| COORDINATE_OUT_OF_RANGE | VALIDATION_DECIMALLONGITUDE_INRANGE | decimalLongitude | decimalLatitude, verbatimLatitude, verbatimLongitude |  |
| COORDINATE_OUT_OF_RANGE | VALIDATION_DECIMALLONGITUDE_NOTEMPTY | decimalLongitude | decimalLatitude, verbatimLatitude, verbatimLongitude |  |
| COORDINATE_OUT_OF_RANGE | VALIDATION_LOCATION_NOTEMPTY | decimalLatitude, decimalLongitude, verbatimLatitude, verbatimLongitude |  | continent, country, countryCode, county, footprintWKT, higherGeography, higherGeographyID, island, islandGroup, locality, locationID, municipality, stateProvince, verbatimCoordinates, verbatimLocality, waterBody |
| COORDINATE_REPROJECTED | AMENDMENT_COORDINATES_FROM_VERBATIM | decimalLatitude, decimalLongitude, geodeticDatum |  |  |
| COORDINATE_REPROJECTED | AMENDMENT_COORDINATES_TRANSPOSED | decimalLatitude, decimalLongitude | geodeticDatum |  |
| COORDINATE_REPROJECTED | AMENDMENT_GEODETICDATUM_ASSUMEDDEFAULT | geodeticDatum | decimalLatitude, decimalLongitude | coordinateUncertaintyInMeters |
| COORDINATE_REPROJECTED | AMENDMENT_GEODETICDATUM_STANDARDIZED | geodeticDatum | decimalLatitude, decimalLongitude |  |
| COORDINATE_REPROJECTED | ISSUE_COORDINATES_CENTEROFCOUNTRY | decimalLatitude, decimalLongitude | geodeticDatum | countryCode |
| COORDINATE_REPROJECTED | VALIDATION_COORDINATESCOUNTRYCODE_CONSISTENT | decimalLatitude, decimalLongitude | geodeticDatum | countryCode |
| COORDINATE_REPROJECTED | VALIDATION_COORDINATESSTATEPROVINCE_CONSISTENT | decimalLatitude, decimalLongitude | geodeticDatum | stateProvince |
| COORDINATE_REPROJECTED | VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT | decimalLatitude, decimalLongitude | geodeticDatum |  |
| COORDINATE_REPROJECTED | VALIDATION_COORDINATES_NOTZERO | decimalLatitude, decimalLongitude | geodeticDatum |  |
| COORDINATE_REPROJECTED | VALIDATION_DECIMALLATITUDE_INRANGE | decimalLatitude | decimalLongitude, geodeticDatum |  |
| COORDINATE_REPROJECTED | VALIDATION_DECIMALLATITUDE_NOTEMPTY | decimalLatitude | decimalLongitude, geodeticDatum |  |
| COORDINATE_REPROJECTED | VALIDATION_DECIMALLONGITUDE_INRANGE | decimalLongitude | decimalLatitude, geodeticDatum |  |
| COORDINATE_REPROJECTED | VALIDATION_DECIMALLONGITUDE_NOTEMPTY | decimalLongitude | decimalLatitude, geodeticDatum |  |
| COORDINATE_REPROJECTED | VALIDATION_GEODETICDATUM_NOTEMPTY | geodeticDatum | decimalLatitude, decimalLongitude |  |
| COORDINATE_REPROJECTED | VALIDATION_GEODETICDATUM_STANDARD | geodeticDatum | decimalLatitude, decimalLongitude |  |
| COORDINATE_REPROJECTED | VALIDATION_LOCATION_NOTEMPTY | decimalLatitude, decimalLongitude | geodeticDatum | continent, country, countryCode, county, footprintWKT, higherGeography, higherGeographyID, island, islandGroup, locality, locationID, municipality, stateProvince, verbatimCoordinates, verbatimLatitude, verbatimLocality, verbatimLongitude, waterBody |
| COORDINATE_REPROJECTION_FAILED | AMENDMENT_COORDINATES_FROM_VERBATIM | decimalLatitude, decimalLongitude, geodeticDatum |  |  |
| COORDINATE_REPROJECTION_FAILED | AMENDMENT_COORDINATES_TRANSPOSED | decimalLatitude, decimalLongitude | geodeticDatum |  |
| COORDINATE_REPROJECTION_FAILED | AMENDMENT_GEODETICDATUM_ASSUMEDDEFAULT | geodeticDatum | decimalLatitude, decimalLongitude | coordinateUncertaintyInMeters |
| COORDINATE_REPROJECTION_FAILED | AMENDMENT_GEODETICDATUM_STANDARDIZED | geodeticDatum | decimalLatitude, decimalLongitude |  |
| COORDINATE_REPROJECTION_FAILED | ISSUE_COORDINATES_CENTEROFCOUNTRY | decimalLatitude, decimalLongitude | geodeticDatum | countryCode |
| COORDINATE_REPROJECTION_FAILED | VALIDATION_COORDINATESCOUNTRYCODE_CONSISTENT | decimalLatitude, decimalLongitude | geodeticDatum | countryCode |
| COORDINATE_REPROJECTION_FAILED | VALIDATION_COORDINATESSTATEPROVINCE_CONSISTENT | decimalLatitude, decimalLongitude | geodeticDatum | stateProvince |
| COORDINATE_REPROJECTION_FAILED | VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT | decimalLatitude, decimalLongitude | geodeticDatum |  |
| COORDINATE_REPROJECTION_FAILED | VALIDATION_COORDINATES_NOTZERO | decimalLatitude, decimalLongitude | geodeticDatum |  |
| COORDINATE_REPROJECTION_FAILED | VALIDATION_DECIMALLATITUDE_INRANGE | decimalLatitude | decimalLongitude, geodeticDatum |  |
| COORDINATE_REPROJECTION_FAILED | VALIDATION_DECIMALLATITUDE_NOTEMPTY | decimalLatitude | decimalLongitude, geodeticDatum |  |
| COORDINATE_REPROJECTION_FAILED | VALIDATION_DECIMALLONGITUDE_INRANGE | decimalLongitude | decimalLatitude, geodeticDatum |  |
| COORDINATE_REPROJECTION_FAILED | VALIDATION_DECIMALLONGITUDE_NOTEMPTY | decimalLongitude | decimalLatitude, geodeticDatum |  |
| COORDINATE_REPROJECTION_FAILED | VALIDATION_GEODETICDATUM_NOTEMPTY | geodeticDatum | decimalLatitude, decimalLongitude |  |
| COORDINATE_REPROJECTION_FAILED | VALIDATION_GEODETICDATUM_STANDARD | geodeticDatum | decimalLatitude, decimalLongitude |  |
| COORDINATE_REPROJECTION_FAILED | VALIDATION_LOCATION_NOTEMPTY | decimalLatitude, decimalLongitude | geodeticDatum | continent, country, countryCode, county, footprintWKT, higherGeography, higherGeographyID, island, islandGroup, locality, locationID, municipality, stateProvince, verbatimCoordinates, verbatimLatitude, verbatimLocality, verbatimLongitude, waterBody |
| COORDINATE_UNCERTAINTY_METERS_INVALID | AMENDMENT_GEODETICDATUM_ASSUMEDDEFAULT | coordinateUncertaintyInMeters |  | geodeticDatum |
| COORDINATE_UNCERTAINTY_METERS_INVALID | VALIDATION_COORDINATEUNCERTAINTY_INRANGE | coordinateUncertaintyInMeters |  |  |
| COORDINATE_UNCERTAINTY_PRECISION_MISMATCH | AMENDMENT_GEODETICDATUM_ASSUMEDDEFAULT | coordinateUncertaintyInMeters | coordinatePrecision | geodeticDatum |
| COORDINATE_UNCERTAINTY_PRECISION_MISMATCH | VALIDATION_COORDINATEUNCERTAINTY_INRANGE | coordinateUncertaintyInMeters | coordinatePrecision |  |
| COUNTRY_COORDINATE_MISMATCH | AMENDMENT_COORDINATES_FROM_VERBATIM | decimalLatitude, decimalLongitude | country | geodeticDatum |
| COUNTRY_COORDINATE_MISMATCH | AMENDMENT_COORDINATES_TRANSPOSED | decimalLatitude, decimalLongitude | country |  |
| COUNTRY_COORDINATE_MISMATCH | ISSUE_COORDINATES_CENTEROFCOUNTRY | decimalLatitude, decimalLongitude | country | countryCode |
| COUNTRY_COORDINATE_MISMATCH | VALIDATION_COORDINATESCOUNTRYCODE_CONSISTENT | decimalLatitude, decimalLongitude | country | countryCode |
| COUNTRY_COORDINATE_MISMATCH | VALIDATION_COORDINATESSTATEPROVINCE_CONSISTENT | decimalLatitude, decimalLongitude | country | stateProvince |
| COUNTRY_COORDINATE_MISMATCH | VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT | decimalLatitude, decimalLongitude | country |  |
| COUNTRY_COORDINATE_MISMATCH | VALIDATION_COORDINATES_NOTZERO | decimalLatitude, decimalLongitude | country |  |
| COUNTRY_COORDINATE_MISMATCH | VALIDATION_COUNTRYCOUNTRYCODE_CONSISTENT | country | decimalLatitude, decimalLongitude | countryCode |
| COUNTRY_COORDINATE_MISMATCH | VALIDATION_COUNTRYSTATEPROVINCE_UNAMBIGUOUS | country | decimalLatitude, decimalLongitude | stateProvince |
| COUNTRY_COORDINATE_MISMATCH | VALIDATION_COUNTRY_FOUND | country | decimalLatitude, decimalLongitude |  |
| COUNTRY_COORDINATE_MISMATCH | VALIDATION_COUNTRY_NOTEMPTY | country | decimalLatitude, decimalLongitude |  |
| COUNTRY_COORDINATE_MISMATCH | VALIDATION_DECIMALLATITUDE_INRANGE | decimalLatitude | country, decimalLongitude |  |
| COUNTRY_COORDINATE_MISMATCH | VALIDATION_DECIMALLATITUDE_NOTEMPTY | decimalLatitude | country, decimalLongitude |  |
| COUNTRY_COORDINATE_MISMATCH | VALIDATION_DECIMALLONGITUDE_INRANGE | decimalLongitude | country, decimalLatitude |  |
| COUNTRY_COORDINATE_MISMATCH | VALIDATION_DECIMALLONGITUDE_NOTEMPTY | decimalLongitude | country, decimalLatitude |  |
| COUNTRY_COORDINATE_MISMATCH | VALIDATION_LOCATION_NOTEMPTY | country, decimalLatitude, decimalLongitude |  | continent, countryCode, county, footprintWKT, higherGeography, higherGeographyID, island, islandGroup, locality, locationID, municipality, stateProvince, verbatimCoordinates, verbatimLatitude, verbatimLocality, verbatimLongitude, waterBody |
| COUNTRY_DERIVED_FROM_COORDINATES | AMENDMENT_COORDINATES_FROM_VERBATIM | decimalLatitude, decimalLongitude |  | geodeticDatum |
| COUNTRY_DERIVED_FROM_COORDINATES | AMENDMENT_COORDINATES_TRANSPOSED | decimalLatitude, decimalLongitude |  |  |
| COUNTRY_DERIVED_FROM_COORDINATES | ISSUE_COORDINATES_CENTEROFCOUNTRY | decimalLatitude, decimalLongitude |  | countryCode |
| COUNTRY_DERIVED_FROM_COORDINATES | VALIDATION_COORDINATESCOUNTRYCODE_CONSISTENT | decimalLatitude, decimalLongitude |  | countryCode |
| COUNTRY_DERIVED_FROM_COORDINATES | VALIDATION_COORDINATESSTATEPROVINCE_CONSISTENT | decimalLatitude, decimalLongitude |  | stateProvince |
| COUNTRY_DERIVED_FROM_COORDINATES | VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT | decimalLatitude, decimalLongitude |  |  |
| COUNTRY_DERIVED_FROM_COORDINATES | VALIDATION_COORDINATES_NOTZERO | decimalLatitude, decimalLongitude |  |  |
| COUNTRY_DERIVED_FROM_COORDINATES | VALIDATION_DECIMALLATITUDE_INRANGE | decimalLatitude | decimalLongitude |  |
| COUNTRY_DERIVED_FROM_COORDINATES | VALIDATION_DECIMALLATITUDE_NOTEMPTY | decimalLatitude | decimalLongitude |  |
| COUNTRY_DERIVED_FROM_COORDINATES | VALIDATION_DECIMALLONGITUDE_INRANGE | decimalLongitude | decimalLatitude |  |
| COUNTRY_DERIVED_FROM_COORDINATES | VALIDATION_DECIMALLONGITUDE_NOTEMPTY | decimalLongitude | decimalLatitude |  |
| COUNTRY_DERIVED_FROM_COORDINATES | VALIDATION_LOCATION_NOTEMPTY | decimalLatitude, decimalLongitude |  | continent, country, countryCode, county, footprintWKT, higherGeography, higherGeographyID, island, islandGroup, locality, locationID, municipality, stateProvince, verbatimCoordinates, verbatimLatitude, verbatimLocality, verbatimLongitude, waterBody |
| COUNTRY_INFERRED_FROM_COORDINATES | AMENDMENT_COORDINATES_FROM_VERBATIM | decimalLatitude, decimalLongitude |  | geodeticDatum |
| COUNTRY_INFERRED_FROM_COORDINATES | AMENDMENT_COORDINATES_TRANSPOSED | decimalLatitude, decimalLongitude |  |  |
| COUNTRY_INFERRED_FROM_COORDINATES | ISSUE_COORDINATES_CENTEROFCOUNTRY | decimalLatitude, decimalLongitude |  | countryCode |
| COUNTRY_INFERRED_FROM_COORDINATES | VALIDATION_COORDINATESCOUNTRYCODE_CONSISTENT | decimalLatitude, decimalLongitude |  | countryCode |
| COUNTRY_INFERRED_FROM_COORDINATES | VALIDATION_COORDINATESSTATEPROVINCE_CONSISTENT | decimalLatitude, decimalLongitude |  | stateProvince |
| COUNTRY_INFERRED_FROM_COORDINATES | VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT | decimalLatitude, decimalLongitude |  |  |
| COUNTRY_INFERRED_FROM_COORDINATES | VALIDATION_COORDINATES_NOTZERO | decimalLatitude, decimalLongitude |  |  |
| COUNTRY_INFERRED_FROM_COORDINATES | VALIDATION_DECIMALLATITUDE_INRANGE | decimalLatitude | decimalLongitude |  |
| COUNTRY_INFERRED_FROM_COORDINATES | VALIDATION_DECIMALLATITUDE_NOTEMPTY | decimalLatitude | decimalLongitude |  |
| COUNTRY_INFERRED_FROM_COORDINATES | VALIDATION_DECIMALLONGITUDE_INRANGE | decimalLongitude | decimalLatitude |  |
| COUNTRY_INFERRED_FROM_COORDINATES | VALIDATION_DECIMALLONGITUDE_NOTEMPTY | decimalLongitude | decimalLatitude |  |
| COUNTRY_INFERRED_FROM_COORDINATES | VALIDATION_LOCATION_NOTEMPTY | decimalLatitude, decimalLongitude |  | continent, country, countryCode, county, footprintWKT, higherGeography, higherGeographyID, island, islandGroup, locality, locationID, municipality, stateProvince, verbatimCoordinates, verbatimLatitude, verbatimLocality, verbatimLongitude, waterBody |
| COUNTRY_INVALID | VALIDATION_COUNTRYCOUNTRYCODE_CONSISTENT | country |  | countryCode |
| COUNTRY_INVALID | VALIDATION_COUNTRYSTATEPROVINCE_UNAMBIGUOUS | country |  | stateProvince |
| COUNTRY_INVALID | VALIDATION_COUNTRY_FOUND | country |  |  |
| COUNTRY_INVALID | VALIDATION_COUNTRY_NOTEMPTY | country |  |  |
| COUNTRY_INVALID | VALIDATION_LOCATION_NOTEMPTY | country |  | continent, countryCode, county, decimalLatitude, decimalLongitude, footprintWKT, higherGeography, higherGeographyID, island, islandGroup, locality, locationID, municipality, stateProvince, verbatimCoordinates, verbatimLatitude, verbatimLocality, verbatimLongitude, waterBody |
| COUNTRY_MISMATCH | AMENDMENT_COORDINATES_FROM_VERBATIM | decimalLatitude, decimalLongitude | countryCode | geodeticDatum |
| COUNTRY_MISMATCH | AMENDMENT_COORDINATES_TRANSPOSED | decimalLatitude, decimalLongitude | countryCode |  |
| COUNTRY_MISMATCH | AMENDMENT_COUNTRYCODE_FROM_COORDINATES | countryCode | decimalLatitude, decimalLongitude |  |
| COUNTRY_MISMATCH | AMENDMENT_COUNTRYCODE_STANDARDIZED | countryCode | decimalLatitude, decimalLongitude |  |
| COUNTRY_MISMATCH | ISSUE_COORDINATES_CENTEROFCOUNTRY | countryCode, decimalLatitude, decimalLongitude |  |  |
| COUNTRY_MISMATCH | VALIDATION_COORDINATESCOUNTRYCODE_CONSISTENT | countryCode, decimalLatitude, decimalLongitude |  |  |
| COUNTRY_MISMATCH | VALIDATION_COORDINATESSTATEPROVINCE_CONSISTENT | decimalLatitude, decimalLongitude | countryCode | stateProvince |
| COUNTRY_MISMATCH | VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT | decimalLatitude, decimalLongitude | countryCode |  |
| COUNTRY_MISMATCH | VALIDATION_COORDINATES_NOTZERO | decimalLatitude, decimalLongitude | countryCode |  |
| COUNTRY_MISMATCH | VALIDATION_COUNTRYCODE_NOTEMPTY | countryCode | decimalLatitude, decimalLongitude |  |
| COUNTRY_MISMATCH | VALIDATION_COUNTRYCODE_STANDARD | countryCode | decimalLatitude, decimalLongitude |  |
| COUNTRY_MISMATCH | VALIDATION_COUNTRYCOUNTRYCODE_CONSISTENT | countryCode | decimalLatitude, decimalLongitude | country |
| COUNTRY_MISMATCH | VALIDATION_DECIMALLATITUDE_INRANGE | decimalLatitude | countryCode, decimalLongitude |  |
| COUNTRY_MISMATCH | VALIDATION_DECIMALLATITUDE_NOTEMPTY | decimalLatitude | countryCode, decimalLongitude |  |
| COUNTRY_MISMATCH | VALIDATION_DECIMALLONGITUDE_INRANGE | decimalLongitude | countryCode, decimalLatitude |  |
| COUNTRY_MISMATCH | VALIDATION_DECIMALLONGITUDE_NOTEMPTY | decimalLongitude | countryCode, decimalLatitude |  |
| COUNTRY_MISMATCH | VALIDATION_LOCATION_NOTEMPTY | countryCode, decimalLatitude, decimalLongitude |  | continent, country, county, footprintWKT, higherGeography, higherGeographyID, island, islandGroup, locality, locationID, municipality, stateProvince, verbatimCoordinates, verbatimLatitude, verbatimLocality, verbatimLongitude, waterBody |
| DEPTH_IN_FEET | AMENDMENT_MINDEPTHMAXDEPTH_FROM_VERBATIM | maximumDepthInMeters, minimumDepthInMeters |  |  |
| DEPTH_IN_FEET | VALIDATION_MAXDEPTH_INRANGE | maximumDepthInMeters | minimumDepthInMeters |  |
| DEPTH_IN_FEET | VALIDATION_MINDEPTH_INRANGE | minimumDepthInMeters | maximumDepthInMeters |  |
| DEPTH_IN_FEET | VALIDATION_MINDEPTH_LESSTHAN_MAXDEPTH | maximumDepthInMeters, minimumDepthInMeters |  |  |
| DEPTH_MIN_MAX_SWAPPED | AMENDMENT_MINDEPTHMAXDEPTH_FROM_VERBATIM | maximumDepthInMeters, minimumDepthInMeters |  |  |
| DEPTH_MIN_MAX_SWAPPED | VALIDATION_MAXDEPTH_INRANGE | maximumDepthInMeters | minimumDepthInMeters |  |
| DEPTH_MIN_MAX_SWAPPED | VALIDATION_MINDEPTH_INRANGE | minimumDepthInMeters | maximumDepthInMeters |  |
| DEPTH_MIN_MAX_SWAPPED | VALIDATION_MINDEPTH_LESSTHAN_MAXDEPTH | maximumDepthInMeters, minimumDepthInMeters |  |  |
| DEPTH_NON_NUMERIC | AMENDMENT_MINDEPTHMAXDEPTH_FROM_VERBATIM | maximumDepthInMeters, minimumDepthInMeters |  |  |
| DEPTH_NON_NUMERIC | VALIDATION_MAXDEPTH_INRANGE | maximumDepthInMeters | minimumDepthInMeters |  |
| DEPTH_NON_NUMERIC | VALIDATION_MINDEPTH_INRANGE | minimumDepthInMeters | maximumDepthInMeters |  |
| DEPTH_NON_NUMERIC | VALIDATION_MINDEPTH_LESSTHAN_MAXDEPTH | maximumDepthInMeters, minimumDepthInMeters |  |  |
| DEPTH_NOT_METRIC | AMENDMENT_MINDEPTHMAXDEPTH_FROM_VERBATIM | maximumDepthInMeters, minimumDepthInMeters |  |  |
| DEPTH_NOT_METRIC | VALIDATION_MAXDEPTH_INRANGE | maximumDepthInMeters | minimumDepthInMeters |  |
| DEPTH_NOT_METRIC | VALIDATION_MINDEPTH_INRANGE | minimumDepthInMeters | maximumDepthInMeters |  |
| DEPTH_NOT_METRIC | VALIDATION_MINDEPTH_LESSTHAN_MAXDEPTH | maximumDepthInMeters, minimumDepthInMeters |  |  |
| DEPTH_UNLIKELY | AMENDMENT_MINDEPTHMAXDEPTH_FROM_VERBATIM | maximumDepthInMeters, minimumDepthInMeters |  |  |
| DEPTH_UNLIKELY | VALIDATION_MAXDEPTH_INRANGE | maximumDepthInMeters | minimumDepthInMeters |  |
| DEPTH_UNLIKELY | VALIDATION_MINDEPTH_INRANGE | minimumDepthInMeters | maximumDepthInMeters |  |
| DEPTH_UNLIKELY | VALIDATION_MINDEPTH_LESSTHAN_MAXDEPTH | maximumDepthInMeters, minimumDepthInMeters |  |  |
| ELEVATION_MIN_MAX_SWAPPED | AMENDMENT_MINELEVATIONMAXELEVATION_FROM_VERBATIM | maximumElevationInMeters, minimumElevationInMeters |  |  |
| ELEVATION_MIN_MAX_SWAPPED | VALIDATION_MAXELEVATION_INRANGE | maximumElevationInMeters | minimumElevationInMeters |  |
| ELEVATION_MIN_MAX_SWAPPED | VALIDATION_MINELEVATION_INRANGE | minimumElevationInMeters | maximumElevationInMeters |  |
| ELEVATION_MIN_MAX_SWAPPED | VALIDATION_MINELEVATION_LESSTHAN_MAXELEVATION | maximumElevationInMeters, minimumElevationInMeters |  |  |
| ELEVATION_NON_NUMERIC | AMENDMENT_MINELEVATIONMAXELEVATION_FROM_VERBATIM | maximumElevationInMeters, minimumElevationInMeters |  |  |
| ELEVATION_NON_NUMERIC | VALIDATION_MAXELEVATION_INRANGE | maximumElevationInMeters | minimumElevationInMeters |  |
| ELEVATION_NON_NUMERIC | VALIDATION_MINELEVATION_INRANGE | minimumElevationInMeters | maximumElevationInMeters |  |
| ELEVATION_NON_NUMERIC | VALIDATION_MINELEVATION_LESSTHAN_MAXELEVATION | maximumElevationInMeters, minimumElevationInMeters |  |  |
| ELEVATION_NOT_METRIC | AMENDMENT_MINELEVATIONMAXELEVATION_FROM_VERBATIM | maximumElevationInMeters, minimumElevationInMeters |  |  |
| ELEVATION_NOT_METRIC | VALIDATION_MAXELEVATION_INRANGE | maximumElevationInMeters | minimumElevationInMeters |  |
| ELEVATION_NOT_METRIC | VALIDATION_MINELEVATION_INRANGE | minimumElevationInMeters | maximumElevationInMeters |  |
| ELEVATION_NOT_METRIC | VALIDATION_MINELEVATION_LESSTHAN_MAXELEVATION | maximumElevationInMeters, minimumElevationInMeters |  |  |
| ELEVATION_UNLIKELY | AMENDMENT_MINELEVATIONMAXELEVATION_FROM_VERBATIM | maximumElevationInMeters, minimumElevationInMeters |  |  |
| ELEVATION_UNLIKELY | VALIDATION_MAXELEVATION_INRANGE | maximumElevationInMeters | minimumElevationInMeters |  |
| ELEVATION_UNLIKELY | VALIDATION_MINELEVATION_INRANGE | minimumElevationInMeters | maximumElevationInMeters |  |
| ELEVATION_UNLIKELY | VALIDATION_MINELEVATION_LESSTHAN_MAXELEVATION | maximumElevationInMeters, minimumElevationInMeters |  |  |
| FOOTPRINT_WKT_INVALID | VALIDATION_LOCATION_NOTEMPTY | footprintWKT |  | continent, country, countryCode, county, decimalLatitude, decimalLongitude, higherGeography, higherGeographyID, island, islandGroup, locality, locationID, municipality, stateProvince, verbatimCoordinates, verbatimLatitude, verbatimLocality, verbatimLongitude, waterBody |
| FOOTPRINT_WKT_MISMATCH | AMENDMENT_COORDINATES_FROM_VERBATIM | decimalLatitude, decimalLongitude | footprintWKT | geodeticDatum |
| FOOTPRINT_WKT_MISMATCH | AMENDMENT_COORDINATES_TRANSPOSED | decimalLatitude, decimalLongitude | footprintWKT |  |
| FOOTPRINT_WKT_MISMATCH | ISSUE_COORDINATES_CENTEROFCOUNTRY | decimalLatitude, decimalLongitude | footprintWKT | countryCode |
| FOOTPRINT_WKT_MISMATCH | VALIDATION_COORDINATESCOUNTRYCODE_CONSISTENT | decimalLatitude, decimalLongitude | footprintWKT | countryCode |
| FOOTPRINT_WKT_MISMATCH | VALIDATION_COORDINATESSTATEPROVINCE_CONSISTENT | decimalLatitude, decimalLongitude | footprintWKT | stateProvince |
| FOOTPRINT_WKT_MISMATCH | VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT | decimalLatitude, decimalLongitude | footprintWKT |  |
| FOOTPRINT_WKT_MISMATCH | VALIDATION_COORDINATES_NOTZERO | decimalLatitude, decimalLongitude | footprintWKT |  |
| FOOTPRINT_WKT_MISMATCH | VALIDATION_DECIMALLATITUDE_INRANGE | decimalLatitude | decimalLongitude, footprintWKT |  |
| FOOTPRINT_WKT_MISMATCH | VALIDATION_DECIMALLATITUDE_NOTEMPTY | decimalLatitude | decimalLongitude, footprintWKT |  |
| FOOTPRINT_WKT_MISMATCH | VALIDATION_DECIMALLONGITUDE_INRANGE | decimalLongitude | decimalLatitude, footprintWKT |  |
| FOOTPRINT_WKT_MISMATCH | VALIDATION_DECIMALLONGITUDE_NOTEMPTY | decimalLongitude | decimalLatitude, footprintWKT |  |
| FOOTPRINT_WKT_MISMATCH | VALIDATION_LOCATION_NOTEMPTY | decimalLatitude, decimalLongitude, footprintWKT |  | continent, country, countryCode, county, higherGeography, higherGeographyID, island, islandGroup, locality, locationID, municipality, stateProvince, verbatimCoordinates, verbatimLatitude, verbatimLocality, verbatimLongitude, waterBody |
| GEODETIC_DATUM_INVALID | AMENDMENT_COORDINATES_FROM_VERBATIM | geodeticDatum |  | decimalLatitude, decimalLongitude |
| GEODETIC_DATUM_INVALID | AMENDMENT_GEODETICDATUM_ASSUMEDDEFAULT | geodeticDatum |  | coordinateUncertaintyInMeters |
| GEODETIC_DATUM_INVALID | AMENDMENT_GEODETICDATUM_STANDARDIZED | geodeticDatum |  |  |
| GEODETIC_DATUM_INVALID | VALIDATION_GEODETICDATUM_NOTEMPTY | geodeticDatum |  |  |
| GEODETIC_DATUM_INVALID | VALIDATION_GEODETICDATUM_STANDARD | geodeticDatum |  |  |
| MISSING_GEODETICDATUM | AMENDMENT_COORDINATES_FROM_VERBATIM | geodeticDatum |  | decimalLatitude, decimalLongitude |
| MISSING_GEODETICDATUM | AMENDMENT_GEODETICDATUM_ASSUMEDDEFAULT | geodeticDatum |  | coordinateUncertaintyInMeters |
| MISSING_GEODETICDATUM | AMENDMENT_GEODETICDATUM_STANDARDIZED | geodeticDatum |  |  |
| MISSING_GEODETICDATUM | VALIDATION_GEODETICDATUM_NOTEMPTY | geodeticDatum |  |  |
| MISSING_GEODETICDATUM | VALIDATION_GEODETICDATUM_STANDARD | geodeticDatum |  |  |
| PRESUMED_NEGATED_LATITUDE | AMENDMENT_COORDINATES_FROM_VERBATIM | decimalLatitude |  | decimalLongitude, geodeticDatum |
| PRESUMED_NEGATED_LATITUDE | AMENDMENT_COORDINATES_TRANSPOSED | decimalLatitude |  | decimalLongitude |
| PRESUMED_NEGATED_LATITUDE | ISSUE_COORDINATES_CENTEROFCOUNTRY | decimalLatitude |  | countryCode, decimalLongitude |
| PRESUMED_NEGATED_LATITUDE | VALIDATION_COORDINATESCOUNTRYCODE_CONSISTENT | decimalLatitude |  | countryCode, decimalLongitude |
| PRESUMED_NEGATED_LATITUDE | VALIDATION_COORDINATESSTATEPROVINCE_CONSISTENT | decimalLatitude |  | decimalLongitude, stateProvince |
| PRESUMED_NEGATED_LATITUDE | VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT | decimalLatitude |  | decimalLongitude |
| PRESUMED_NEGATED_LATITUDE | VALIDATION_COORDINATES_NOTZERO | decimalLatitude |  | decimalLongitude |
| PRESUMED_NEGATED_LATITUDE | VALIDATION_DECIMALLATITUDE_INRANGE | decimalLatitude |  |  |
| PRESUMED_NEGATED_LATITUDE | VALIDATION_DECIMALLATITUDE_NOTEMPTY | decimalLatitude |  |  |
| PRESUMED_NEGATED_LATITUDE | VALIDATION_LOCATION_NOTEMPTY | decimalLatitude |  | continent, country, countryCode, county, decimalLongitude, footprintWKT, higherGeography, higherGeographyID, island, islandGroup, locality, locationID, municipality, stateProvince, verbatimCoordinates, verbatimLatitude, verbatimLocality, verbatimLongitude, waterBody |
| PRESUMED_NEGATED_LONGITUDE | AMENDMENT_COORDINATES_FROM_VERBATIM | decimalLongitude |  | decimalLatitude, geodeticDatum |
| PRESUMED_NEGATED_LONGITUDE | AMENDMENT_COORDINATES_TRANSPOSED | decimalLongitude |  | decimalLatitude |
| PRESUMED_NEGATED_LONGITUDE | ISSUE_COORDINATES_CENTEROFCOUNTRY | decimalLongitude |  | countryCode, decimalLatitude |
| PRESUMED_NEGATED_LONGITUDE | VALIDATION_COORDINATESCOUNTRYCODE_CONSISTENT | decimalLongitude |  | countryCode, decimalLatitude |
| PRESUMED_NEGATED_LONGITUDE | VALIDATION_COORDINATESSTATEPROVINCE_CONSISTENT | decimalLongitude |  | decimalLatitude, stateProvince |
| PRESUMED_NEGATED_LONGITUDE | VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT | decimalLongitude |  | decimalLatitude |
| PRESUMED_NEGATED_LONGITUDE | VALIDATION_COORDINATES_NOTZERO | decimalLongitude |  | decimalLatitude |
| PRESUMED_NEGATED_LONGITUDE | VALIDATION_DECIMALLONGITUDE_INRANGE | decimalLongitude |  |  |
| PRESUMED_NEGATED_LONGITUDE | VALIDATION_DECIMALLONGITUDE_NOTEMPTY | decimalLongitude |  |  |
| PRESUMED_NEGATED_LONGITUDE | VALIDATION_LOCATION_NOTEMPTY | decimalLongitude |  | continent, country, countryCode, county, decimalLatitude, footprintWKT, higherGeography, higherGeographyID, island, islandGroup, locality, locationID, municipality, stateProvince, verbatimCoordinates, verbatimLatitude, verbatimLocality, verbatimLongitude, waterBody |
| PRESUMED_SWAPPED_COORDINATE | AMENDMENT_COORDINATES_FROM_VERBATIM | decimalLatitude, decimalLongitude |  | geodeticDatum |
| PRESUMED_SWAPPED_COORDINATE | AMENDMENT_COORDINATES_TRANSPOSED | decimalLatitude, decimalLongitude |  |  |
| PRESUMED_SWAPPED_COORDINATE | ISSUE_COORDINATES_CENTEROFCOUNTRY | decimalLatitude, decimalLongitude |  | countryCode |
| PRESUMED_SWAPPED_COORDINATE | VALIDATION_COORDINATESCOUNTRYCODE_CONSISTENT | decimalLatitude, decimalLongitude |  | countryCode |
| PRESUMED_SWAPPED_COORDINATE | VALIDATION_COORDINATESSTATEPROVINCE_CONSISTENT | decimalLatitude, decimalLongitude |  | stateProvince |
| PRESUMED_SWAPPED_COORDINATE | VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT | decimalLatitude, decimalLongitude |  |  |
| PRESUMED_SWAPPED_COORDINATE | VALIDATION_COORDINATES_NOTZERO | decimalLatitude, decimalLongitude |  |  |
| PRESUMED_SWAPPED_COORDINATE | VALIDATION_DECIMALLATITUDE_INRANGE | decimalLatitude | decimalLongitude |  |
| PRESUMED_SWAPPED_COORDINATE | VALIDATION_DECIMALLATITUDE_NOTEMPTY | decimalLatitude | decimalLongitude |  |
| PRESUMED_SWAPPED_COORDINATE | VALIDATION_DECIMALLONGITUDE_INRANGE | decimalLongitude | decimalLatitude |  |
| PRESUMED_SWAPPED_COORDINATE | VALIDATION_DECIMALLONGITUDE_NOTEMPTY | decimalLongitude | decimalLatitude |  |
| PRESUMED_SWAPPED_COORDINATE | VALIDATION_LOCATION_NOTEMPTY | decimalLatitude, decimalLongitude |  | continent, country, countryCode, county, footprintWKT, higherGeography, higherGeographyID, island, islandGroup, locality, locationID, municipality, stateProvince, verbatimCoordinates, verbatimLatitude, verbatimLocality, verbatimLongitude, waterBody |
| SENSITIVITY_REPORT_INVALID | VALIDATION_COORDINATESSTATEPROVINCE_CONSISTENT | stateProvince | scientificName | decimalLatitude, decimalLongitude |
| SENSITIVITY_REPORT_INVALID | VALIDATION_COUNTRYSTATEPROVINCE_UNAMBIGUOUS | stateProvince | scientificName | country |
| SENSITIVITY_REPORT_INVALID | VALIDATION_LOCATION_NOTEMPTY | stateProvince | scientificName | continent, country, countryCode, county, decimalLatitude, decimalLongitude, footprintWKT, higherGeography, higherGeographyID, island, islandGroup, locality, locationID, municipality, verbatimCoordinates, verbatimLatitude, verbatimLocality, verbatimLongitude, waterBody |
| SENSITIVITY_REPORT_INVALID | VALIDATION_STATEPROVINCE_FOUND | stateProvince | scientificName |  |
| SENSITIVITY_REPORT_NOT_LOADABLE | VALIDATION_COORDINATESSTATEPROVINCE_CONSISTENT | stateProvince | scientificName | decimalLatitude, decimalLongitude |
| SENSITIVITY_REPORT_NOT_LOADABLE | VALIDATION_COUNTRYSTATEPROVINCE_UNAMBIGUOUS | stateProvince | scientificName | country |
| SENSITIVITY_REPORT_NOT_LOADABLE | VALIDATION_LOCATION_NOTEMPTY | stateProvince | scientificName | continent, country, countryCode, county, decimalLatitude, decimalLongitude, footprintWKT, higherGeography, higherGeographyID, island, islandGroup, locality, locationID, municipality, verbatimCoordinates, verbatimLatitude, verbatimLocality, verbatimLongitude, waterBody |
| SENSITIVITY_REPORT_NOT_LOADABLE | VALIDATION_STATEPROVINCE_FOUND | stateProvince | scientificName |  |
| STATE_COORDINATE_MISMATCH | AMENDMENT_COORDINATES_FROM_VERBATIM | decimalLatitude, decimalLongitude | stateProvince, verbatimCoordinates, verbatimLatitude, verbatimLongitude | geodeticDatum |
| STATE_COORDINATE_MISMATCH | AMENDMENT_COORDINATES_TRANSPOSED | decimalLatitude, decimalLongitude | stateProvince, verbatimCoordinates, verbatimLatitude, verbatimLongitude |  |
| STATE_COORDINATE_MISMATCH | ISSUE_COORDINATES_CENTEROFCOUNTRY | decimalLatitude, decimalLongitude | stateProvince, verbatimCoordinates, verbatimLatitude, verbatimLongitude | countryCode |
| STATE_COORDINATE_MISMATCH | VALIDATION_COORDINATESCOUNTRYCODE_CONSISTENT | decimalLatitude, decimalLongitude | stateProvince, verbatimCoordinates, verbatimLatitude, verbatimLongitude | countryCode |
| STATE_COORDINATE_MISMATCH | VALIDATION_COORDINATESSTATEPROVINCE_CONSISTENT | decimalLatitude, decimalLongitude, stateProvince | verbatimCoordinates, verbatimLatitude, verbatimLongitude |  |
| STATE_COORDINATE_MISMATCH | VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT | decimalLatitude, decimalLongitude | stateProvince, verbatimCoordinates, verbatimLatitude, verbatimLongitude |  |
| STATE_COORDINATE_MISMATCH | VALIDATION_COORDINATES_NOTZERO | decimalLatitude, decimalLongitude | stateProvince, verbatimCoordinates, verbatimLatitude, verbatimLongitude |  |
| STATE_COORDINATE_MISMATCH | VALIDATION_COUNTRYSTATEPROVINCE_UNAMBIGUOUS | stateProvince | decimalLatitude, decimalLongitude, verbatimCoordinates, verbatimLatitude, verbatimLongitude | country |
| STATE_COORDINATE_MISMATCH | VALIDATION_DECIMALLATITUDE_INRANGE | decimalLatitude | decimalLongitude, stateProvince, verbatimCoordinates, verbatimLatitude, verbatimLongitude |  |
| STATE_COORDINATE_MISMATCH | VALIDATION_DECIMALLATITUDE_NOTEMPTY | decimalLatitude | decimalLongitude, stateProvince, verbatimCoordinates, verbatimLatitude, verbatimLongitude |  |
| STATE_COORDINATE_MISMATCH | VALIDATION_DECIMALLONGITUDE_INRANGE | decimalLongitude | decimalLatitude, stateProvince, verbatimCoordinates, verbatimLatitude, verbatimLongitude |  |
| STATE_COORDINATE_MISMATCH | VALIDATION_DECIMALLONGITUDE_NOTEMPTY | decimalLongitude | decimalLatitude, stateProvince, verbatimCoordinates, verbatimLatitude, verbatimLongitude |  |
| STATE_COORDINATE_MISMATCH | VALIDATION_LOCATION_NOTEMPTY | decimalLatitude, decimalLongitude, stateProvince, verbatimCoordinates, verbatimLatitude, verbatimLongitude |  | continent, country, countryCode, county, footprintWKT, higherGeography, higherGeographyID, island, islandGroup, locality, locationID, municipality, verbatimLocality, waterBody |
| STATE_COORDINATE_MISMATCH | VALIDATION_STATEPROVINCE_FOUND | stateProvince | decimalLatitude, decimalLongitude, verbatimCoordinates, verbatimLatitude, verbatimLongitude |  |
| UNCERTAINTY_NOT_SPECIFIED | AMENDMENT_GEODETICDATUM_ASSUMEDDEFAULT | coordinateUncertaintyInMeters |  | geodeticDatum |
| UNCERTAINTY_NOT_SPECIFIED | VALIDATION_COORDINATEUNCERTAINTY_INRANGE | coordinateUncertaintyInMeters |  |  |
| ZERO_COORDINATE | AMENDMENT_COORDINATES_FROM_VERBATIM | decimalLatitude, decimalLongitude | verbatimCoordinates, verbatimLatitude, verbatimLongitude | geodeticDatum |
| ZERO_COORDINATE | AMENDMENT_COORDINATES_TRANSPOSED | decimalLatitude, decimalLongitude | verbatimCoordinates, verbatimLatitude, verbatimLongitude |  |
| ZERO_COORDINATE | ISSUE_COORDINATES_CENTEROFCOUNTRY | decimalLatitude, decimalLongitude | verbatimCoordinates, verbatimLatitude, verbatimLongitude | countryCode |
| ZERO_COORDINATE | VALIDATION_COORDINATESCOUNTRYCODE_CONSISTENT | decimalLatitude, decimalLongitude | verbatimCoordinates, verbatimLatitude, verbatimLongitude | countryCode |
| ZERO_COORDINATE | VALIDATION_COORDINATESSTATEPROVINCE_CONSISTENT | decimalLatitude, decimalLongitude | verbatimCoordinates, verbatimLatitude, verbatimLongitude | stateProvince |
| ZERO_COORDINATE | VALIDATION_COORDINATESTERRESTRIALMARINE_CONSISTENT | decimalLatitude, decimalLongitude | verbatimCoordinates, verbatimLatitude, verbatimLongitude |  |
| ZERO_COORDINATE | VALIDATION_COORDINATES_NOTZERO | decimalLatitude, decimalLongitude | verbatimCoordinates, verbatimLatitude, verbatimLongitude |  |
| ZERO_COORDINATE | VALIDATION_DECIMALLATITUDE_INRANGE | decimalLatitude | decimalLongitude, verbatimCoordinates, verbatimLatitude, verbatimLongitude |  |
| ZERO_COORDINATE | VALIDATION_DECIMALLATITUDE_NOTEMPTY | decimalLatitude | decimalLongitude, verbatimCoordinates, verbatimLatitude, verbatimLongitude |  |
| ZERO_COORDINATE | VALIDATION_DECIMALLONGITUDE_INRANGE | decimalLongitude | decimalLatitude, verbatimCoordinates, verbatimLatitude, verbatimLongitude |  |
| ZERO_COORDINATE | VALIDATION_DECIMALLONGITUDE_NOTEMPTY | decimalLongitude | decimalLatitude, verbatimCoordinates, verbatimLatitude, verbatimLongitude |  |
| ZERO_COORDINATE | VALIDATION_LOCATION_NOTEMPTY | decimalLatitude, decimalLongitude, verbatimCoordinates, verbatimLatitude, verbatimLongitude |  | continent, country, countryCode, county, footprintWKT, higherGeography, higherGeographyID, island, islandGroup, locality, locationID, municipality, stateProvince, verbatimLocality, waterBody |

## dwc:Event

| ALA Assertion | BDQ Test | Connecting Terms | ALA-only Terms | BDQ-only Terms |
|---------------|----------|------------------|----------------|----------------|
| FIRST_OF_CENTURY | AMENDMENT_DAY_STANDARDIZED | day | eventDate, month, year |  |
| FIRST_OF_CENTURY | AMENDMENT_EVENTDATE_FROM_VERBATIM | eventDate | day, month, year |  |
| FIRST_OF_CENTURY | AMENDMENT_EVENTDATE_FROM_YEARMONTHDAY | eventDate | day, month, year |  |
| FIRST_OF_CENTURY | AMENDMENT_EVENTDATE_FROM_YEARSTARTDAYOFYEARENDDAYOFYEAR | eventDate | day, month, year |  |
| FIRST_OF_CENTURY | AMENDMENT_EVENTDATE_STANDARDIZED | eventDate | day, month, year |  |
| FIRST_OF_CENTURY | AMENDMENT_EVENT_FROM_EVENTDATE | day, month, year | eventDate | endDayOfYear, startDayOfYear |
| FIRST_OF_CENTURY | AMENDMENT_MONTH_STANDARDIZED | month | day, eventDate, year |  |
| FIRST_OF_CENTURY | MEASURE_EVENTDATE_DURATIONINSECONDS | eventDate | day, month, year |  |
| FIRST_OF_CENTURY | VALIDATION_DAY_INRANGE | day, month, year | eventDate |  |
| FIRST_OF_CENTURY | VALIDATION_DAY_STANDARD | day | eventDate, month, year |  |
| FIRST_OF_CENTURY | VALIDATION_EVENTDATE_INRANGE | eventDate | day, month, year |  |
| FIRST_OF_CENTURY | VALIDATION_EVENTDATE_NOTEMPTY | eventDate | day, month, year |  |
| FIRST_OF_CENTURY | VALIDATION_EVENTDATE_STANDARD | eventDate | day, month, year |  |
| FIRST_OF_CENTURY | VALIDATION_EVENTTEMPORAL_NOTEMPTY | day, eventDate, month, year |  | endDayOfYear, startDayOfYear, verbatimEventDate |
| FIRST_OF_CENTURY | VALIDATION_EVENT_CONSISTENT | day, eventDate, month, year |  | endDayOfYear, startDayOfYear |
| FIRST_OF_CENTURY | VALIDATION_MONTH_STANDARD | month | day, eventDate, year |  |
| FIRST_OF_CENTURY | VALIDATION_YEAR_INRANGE | year | day, eventDate, month |  |
| FIRST_OF_CENTURY | VALIDATION_YEAR_NOTEMPTY | year | day, eventDate, month |  |
| FIRST_OF_MONTH | AMENDMENT_DAY_STANDARDIZED | day | eventDate, month, year |  |
| FIRST_OF_MONTH | AMENDMENT_EVENTDATE_FROM_VERBATIM | eventDate | day, month, year |  |
| FIRST_OF_MONTH | AMENDMENT_EVENTDATE_FROM_YEARMONTHDAY | eventDate | day, month, year |  |
| FIRST_OF_MONTH | AMENDMENT_EVENTDATE_FROM_YEARSTARTDAYOFYEARENDDAYOFYEAR | eventDate | day, month, year |  |
| FIRST_OF_MONTH | AMENDMENT_EVENTDATE_STANDARDIZED | eventDate | day, month, year |  |
| FIRST_OF_MONTH | AMENDMENT_EVENT_FROM_EVENTDATE | day, month, year | eventDate | endDayOfYear, startDayOfYear |
| FIRST_OF_MONTH | AMENDMENT_MONTH_STANDARDIZED | month | day, eventDate, year |  |
| FIRST_OF_MONTH | MEASURE_EVENTDATE_DURATIONINSECONDS | eventDate | day, month, year |  |
| FIRST_OF_MONTH | VALIDATION_DAY_INRANGE | day, month, year | eventDate |  |
| FIRST_OF_MONTH | VALIDATION_DAY_STANDARD | day | eventDate, month, year |  |
| FIRST_OF_MONTH | VALIDATION_EVENTDATE_INRANGE | eventDate | day, month, year |  |
| FIRST_OF_MONTH | VALIDATION_EVENTDATE_NOTEMPTY | eventDate | day, month, year |  |
| FIRST_OF_MONTH | VALIDATION_EVENTDATE_STANDARD | eventDate | day, month, year |  |
| FIRST_OF_MONTH | VALIDATION_EVENTTEMPORAL_NOTEMPTY | day, eventDate, month, year |  | endDayOfYear, startDayOfYear, verbatimEventDate |
| FIRST_OF_MONTH | VALIDATION_EVENT_CONSISTENT | day, eventDate, month, year |  | endDayOfYear, startDayOfYear |
| FIRST_OF_MONTH | VALIDATION_MONTH_STANDARD | month | day, eventDate, year |  |
| FIRST_OF_MONTH | VALIDATION_YEAR_INRANGE | year | day, eventDate, month |  |
| FIRST_OF_MONTH | VALIDATION_YEAR_NOTEMPTY | year | day, eventDate, month |  |
| FIRST_OF_YEAR | AMENDMENT_DAY_STANDARDIZED | day | eventDate, month, year |  |
| FIRST_OF_YEAR | AMENDMENT_EVENTDATE_FROM_VERBATIM | eventDate | day, month, year |  |
| FIRST_OF_YEAR | AMENDMENT_EVENTDATE_FROM_YEARMONTHDAY | eventDate | day, month, year |  |
| FIRST_OF_YEAR | AMENDMENT_EVENTDATE_FROM_YEARSTARTDAYOFYEARENDDAYOFYEAR | eventDate | day, month, year |  |
| FIRST_OF_YEAR | AMENDMENT_EVENTDATE_STANDARDIZED | eventDate | day, month, year |  |
| FIRST_OF_YEAR | AMENDMENT_EVENT_FROM_EVENTDATE | day, month, year | eventDate | endDayOfYear, startDayOfYear |
| FIRST_OF_YEAR | AMENDMENT_MONTH_STANDARDIZED | month | day, eventDate, year |  |
| FIRST_OF_YEAR | MEASURE_EVENTDATE_DURATIONINSECONDS | eventDate | day, month, year |  |
| FIRST_OF_YEAR | VALIDATION_DAY_INRANGE | day, month, year | eventDate |  |
| FIRST_OF_YEAR | VALIDATION_DAY_STANDARD | day | eventDate, month, year |  |
| FIRST_OF_YEAR | VALIDATION_EVENTDATE_INRANGE | eventDate | day, month, year |  |
| FIRST_OF_YEAR | VALIDATION_EVENTDATE_NOTEMPTY | eventDate | day, month, year |  |
| FIRST_OF_YEAR | VALIDATION_EVENTDATE_STANDARD | eventDate | day, month, year |  |
| FIRST_OF_YEAR | VALIDATION_EVENTTEMPORAL_NOTEMPTY | day, eventDate, month, year |  | endDayOfYear, startDayOfYear, verbatimEventDate |
| FIRST_OF_YEAR | VALIDATION_EVENT_CONSISTENT | day, eventDate, month, year |  | endDayOfYear, startDayOfYear |
| FIRST_OF_YEAR | VALIDATION_MONTH_STANDARD | month | day, eventDate, year |  |
| FIRST_OF_YEAR | VALIDATION_YEAR_INRANGE | year | day, eventDate, month |  |
| FIRST_OF_YEAR | VALIDATION_YEAR_NOTEMPTY | year | day, eventDate, month |  |
| MISSING_COLLECTION_DATE | AMENDMENT_DAY_STANDARDIZED | day | eventDate, month, year |  |
| MISSING_COLLECTION_DATE | AMENDMENT_EVENTDATE_FROM_VERBATIM | eventDate | day, month, year |  |
| MISSING_COLLECTION_DATE | AMENDMENT_EVENTDATE_FROM_YEARMONTHDAY | eventDate | day, month, year |  |
| MISSING_COLLECTION_DATE | AMENDMENT_EVENTDATE_FROM_YEARSTARTDAYOFYEARENDDAYOFYEAR | eventDate | day, month, year |  |
| MISSING_COLLECTION_DATE | AMENDMENT_EVENTDATE_STANDARDIZED | eventDate | day, month, year |  |
| MISSING_COLLECTION_DATE | AMENDMENT_EVENT_FROM_EVENTDATE | day, month, year | eventDate | endDayOfYear, startDayOfYear |
| MISSING_COLLECTION_DATE | AMENDMENT_MONTH_STANDARDIZED | month | day, eventDate, year |  |
| MISSING_COLLECTION_DATE | MEASURE_EVENTDATE_DURATIONINSECONDS | eventDate | day, month, year |  |
| MISSING_COLLECTION_DATE | VALIDATION_DAY_INRANGE | day, month, year | eventDate |  |
| MISSING_COLLECTION_DATE | VALIDATION_DAY_STANDARD | day | eventDate, month, year |  |
| MISSING_COLLECTION_DATE | VALIDATION_EVENTDATE_INRANGE | eventDate | day, month, year |  |
| MISSING_COLLECTION_DATE | VALIDATION_EVENTDATE_NOTEMPTY | eventDate | day, month, year |  |
| MISSING_COLLECTION_DATE | VALIDATION_EVENTDATE_STANDARD | eventDate | day, month, year |  |
| MISSING_COLLECTION_DATE | VALIDATION_EVENTTEMPORAL_NOTEMPTY | day, eventDate, month, year |  | endDayOfYear, startDayOfYear, verbatimEventDate |
| MISSING_COLLECTION_DATE | VALIDATION_EVENT_CONSISTENT | day, eventDate, month, year |  | endDayOfYear, startDayOfYear |
| MISSING_COLLECTION_DATE | VALIDATION_MONTH_STANDARD | month | day, eventDate, year |  |
| MISSING_COLLECTION_DATE | VALIDATION_YEAR_INRANGE | year | day, eventDate, month |  |
| MISSING_COLLECTION_DATE | VALIDATION_YEAR_NOTEMPTY | year | day, eventDate, month |  |
| RECORDED_DATE_INVALID | AMENDMENT_DAY_STANDARDIZED | day | endDayOfYear, eventDate, month, startDayOfYear, year |  |
| RECORDED_DATE_INVALID | AMENDMENT_EVENTDATE_FROM_VERBATIM | eventDate | day, endDayOfYear, month, startDayOfYear, year |  |
| RECORDED_DATE_INVALID | AMENDMENT_EVENTDATE_FROM_YEARMONTHDAY | eventDate | day, endDayOfYear, month, startDayOfYear, year |  |
| RECORDED_DATE_INVALID | AMENDMENT_EVENTDATE_FROM_YEARSTARTDAYOFYEARENDDAYOFYEAR | eventDate | day, endDayOfYear, month, startDayOfYear, year |  |
| RECORDED_DATE_INVALID | AMENDMENT_EVENTDATE_STANDARDIZED | eventDate | day, endDayOfYear, month, startDayOfYear, year |  |
| RECORDED_DATE_INVALID | AMENDMENT_EVENT_FROM_EVENTDATE | day, endDayOfYear, month, startDayOfYear, year | eventDate |  |
| RECORDED_DATE_INVALID | AMENDMENT_MONTH_STANDARDIZED | month | day, endDayOfYear, eventDate, startDayOfYear, year |  |
| RECORDED_DATE_INVALID | MEASURE_EVENTDATE_DURATIONINSECONDS | eventDate | day, endDayOfYear, month, startDayOfYear, year |  |
| RECORDED_DATE_INVALID | VALIDATION_DAY_INRANGE | day, month, year | endDayOfYear, eventDate, startDayOfYear |  |
| RECORDED_DATE_INVALID | VALIDATION_DAY_STANDARD | day | endDayOfYear, eventDate, month, startDayOfYear, year |  |
| RECORDED_DATE_INVALID | VALIDATION_ENDDAYOFYEAR_INRANGE | endDayOfYear | day, eventDate, month, startDayOfYear, year |  |
| RECORDED_DATE_INVALID | VALIDATION_EVENTDATE_INRANGE | eventDate | day, endDayOfYear, month, startDayOfYear, year |  |
| RECORDED_DATE_INVALID | VALIDATION_EVENTDATE_NOTEMPTY | eventDate | day, endDayOfYear, month, startDayOfYear, year |  |
| RECORDED_DATE_INVALID | VALIDATION_EVENTDATE_STANDARD | eventDate | day, endDayOfYear, month, startDayOfYear, year |  |
| RECORDED_DATE_INVALID | VALIDATION_EVENTTEMPORAL_NOTEMPTY | day, endDayOfYear, eventDate, month, startDayOfYear, year |  | verbatimEventDate |
| RECORDED_DATE_INVALID | VALIDATION_EVENT_CONSISTENT | day, endDayOfYear, eventDate, month, startDayOfYear, year |  |  |
| RECORDED_DATE_INVALID | VALIDATION_MONTH_STANDARD | month | day, endDayOfYear, eventDate, startDayOfYear, year |  |
| RECORDED_DATE_INVALID | VALIDATION_STARTDAYOFYEAR_INRANGE | startDayOfYear | day, endDayOfYear, eventDate, month, year |  |
| RECORDED_DATE_INVALID | VALIDATION_YEAR_INRANGE | year | day, endDayOfYear, eventDate, month, startDayOfYear |  |
| RECORDED_DATE_INVALID | VALIDATION_YEAR_NOTEMPTY | year | day, endDayOfYear, eventDate, month, startDayOfYear |  |
| RECORDED_DATE_MISMATCH | AMENDMENT_DAY_STANDARDIZED | day | endDayOfYear, eventDate, month, startDayOfYear, year |  |
| RECORDED_DATE_MISMATCH | AMENDMENT_EVENTDATE_FROM_VERBATIM | eventDate | day, endDayOfYear, month, startDayOfYear, year |  |
| RECORDED_DATE_MISMATCH | AMENDMENT_EVENTDATE_FROM_YEARMONTHDAY | eventDate | day, endDayOfYear, month, startDayOfYear, year |  |
| RECORDED_DATE_MISMATCH | AMENDMENT_EVENTDATE_FROM_YEARSTARTDAYOFYEARENDDAYOFYEAR | eventDate | day, endDayOfYear, month, startDayOfYear, year |  |
| RECORDED_DATE_MISMATCH | AMENDMENT_EVENTDATE_STANDARDIZED | eventDate | day, endDayOfYear, month, startDayOfYear, year |  |
| RECORDED_DATE_MISMATCH | AMENDMENT_EVENT_FROM_EVENTDATE | day, endDayOfYear, month, startDayOfYear, year | eventDate |  |
| RECORDED_DATE_MISMATCH | AMENDMENT_MONTH_STANDARDIZED | month | day, endDayOfYear, eventDate, startDayOfYear, year |  |
| RECORDED_DATE_MISMATCH | MEASURE_EVENTDATE_DURATIONINSECONDS | eventDate | day, endDayOfYear, month, startDayOfYear, year |  |
| RECORDED_DATE_MISMATCH | VALIDATION_DAY_INRANGE | day, month, year | endDayOfYear, eventDate, startDayOfYear |  |
| RECORDED_DATE_MISMATCH | VALIDATION_DAY_STANDARD | day | endDayOfYear, eventDate, month, startDayOfYear, year |  |
| RECORDED_DATE_MISMATCH | VALIDATION_ENDDAYOFYEAR_INRANGE | endDayOfYear | day, eventDate, month, startDayOfYear, year |  |
| RECORDED_DATE_MISMATCH | VALIDATION_EVENTDATE_INRANGE | eventDate | day, endDayOfYear, month, startDayOfYear, year |  |
| RECORDED_DATE_MISMATCH | VALIDATION_EVENTDATE_NOTEMPTY | eventDate | day, endDayOfYear, month, startDayOfYear, year |  |
| RECORDED_DATE_MISMATCH | VALIDATION_EVENTDATE_STANDARD | eventDate | day, endDayOfYear, month, startDayOfYear, year |  |
| RECORDED_DATE_MISMATCH | VALIDATION_EVENTTEMPORAL_NOTEMPTY | day, endDayOfYear, eventDate, month, startDayOfYear, year |  | verbatimEventDate |
| RECORDED_DATE_MISMATCH | VALIDATION_EVENT_CONSISTENT | day, endDayOfYear, eventDate, month, startDayOfYear, year |  |  |
| RECORDED_DATE_MISMATCH | VALIDATION_MONTH_STANDARD | month | day, endDayOfYear, eventDate, startDayOfYear, year |  |
| RECORDED_DATE_MISMATCH | VALIDATION_STARTDAYOFYEAR_INRANGE | startDayOfYear | day, endDayOfYear, eventDate, month, year |  |
| RECORDED_DATE_MISMATCH | VALIDATION_YEAR_INRANGE | year | day, endDayOfYear, eventDate, month, startDayOfYear |  |
| RECORDED_DATE_MISMATCH | VALIDATION_YEAR_NOTEMPTY | year | day, endDayOfYear, eventDate, month, startDayOfYear |  |
| RECORDED_DATE_UNLIKELY | AMENDMENT_DAY_STANDARDIZED | day | endDayOfYear, eventDate, month, startDayOfYear, year |  |
| RECORDED_DATE_UNLIKELY | AMENDMENT_EVENTDATE_FROM_VERBATIM | eventDate | day, endDayOfYear, month, startDayOfYear, year |  |
| RECORDED_DATE_UNLIKELY | AMENDMENT_EVENTDATE_FROM_YEARMONTHDAY | eventDate | day, endDayOfYear, month, startDayOfYear, year |  |
| RECORDED_DATE_UNLIKELY | AMENDMENT_EVENTDATE_FROM_YEARSTARTDAYOFYEARENDDAYOFYEAR | eventDate | day, endDayOfYear, month, startDayOfYear, year |  |
| RECORDED_DATE_UNLIKELY | AMENDMENT_EVENTDATE_STANDARDIZED | eventDate | day, endDayOfYear, month, startDayOfYear, year |  |
| RECORDED_DATE_UNLIKELY | AMENDMENT_EVENT_FROM_EVENTDATE | day, endDayOfYear, month, startDayOfYear, year | eventDate |  |
| RECORDED_DATE_UNLIKELY | AMENDMENT_MONTH_STANDARDIZED | month | day, endDayOfYear, eventDate, startDayOfYear, year |  |
| RECORDED_DATE_UNLIKELY | MEASURE_EVENTDATE_DURATIONINSECONDS | eventDate | day, endDayOfYear, month, startDayOfYear, year |  |
| RECORDED_DATE_UNLIKELY | VALIDATION_DAY_INRANGE | day, month, year | endDayOfYear, eventDate, startDayOfYear |  |
| RECORDED_DATE_UNLIKELY | VALIDATION_DAY_STANDARD | day | endDayOfYear, eventDate, month, startDayOfYear, year |  |
| RECORDED_DATE_UNLIKELY | VALIDATION_ENDDAYOFYEAR_INRANGE | endDayOfYear | day, eventDate, month, startDayOfYear, year |  |
| RECORDED_DATE_UNLIKELY | VALIDATION_EVENTDATE_INRANGE | eventDate | day, endDayOfYear, month, startDayOfYear, year |  |
| RECORDED_DATE_UNLIKELY | VALIDATION_EVENTDATE_NOTEMPTY | eventDate | day, endDayOfYear, month, startDayOfYear, year |  |
| RECORDED_DATE_UNLIKELY | VALIDATION_EVENTDATE_STANDARD | eventDate | day, endDayOfYear, month, startDayOfYear, year |  |
| RECORDED_DATE_UNLIKELY | VALIDATION_EVENTTEMPORAL_NOTEMPTY | day, endDayOfYear, eventDate, month, startDayOfYear, year |  | verbatimEventDate |
| RECORDED_DATE_UNLIKELY | VALIDATION_EVENT_CONSISTENT | day, endDayOfYear, eventDate, month, startDayOfYear, year |  |  |
| RECORDED_DATE_UNLIKELY | VALIDATION_MONTH_STANDARD | month | day, endDayOfYear, eventDate, startDayOfYear, year |  |
| RECORDED_DATE_UNLIKELY | VALIDATION_STARTDAYOFYEAR_INRANGE | startDayOfYear | day, endDayOfYear, eventDate, month, year |  |
| RECORDED_DATE_UNLIKELY | VALIDATION_YEAR_INRANGE | year | day, endDayOfYear, eventDate, month, startDayOfYear |  |
| RECORDED_DATE_UNLIKELY | VALIDATION_YEAR_NOTEMPTY | year | day, endDayOfYear, eventDate, month, startDayOfYear |  |

## dwc:Identification

| ALA Assertion | BDQ Test | Connecting Terms | ALA-only Terms | BDQ-only Terms |
|---------------|----------|------------------|----------------|----------------|
| IDENTIFIED_DATE_INVALID | AMENDMENT_DATEIDENTIFIED_STANDARDIZED | dateIdentified |  |  |
| IDENTIFIED_DATE_INVALID | VALIDATION_DATEIDENTIFIED_INRANGE | dateIdentified |  |  |
| IDENTIFIED_DATE_INVALID | VALIDATION_DATEIDENTIFIED_STANDARD | dateIdentified |  |  |
| IDENTIFIED_DATE_UNLIKELY | AMENDMENT_DATEIDENTIFIED_STANDARDIZED | dateIdentified |  |  |
| IDENTIFIED_DATE_UNLIKELY | VALIDATION_DATEIDENTIFIED_INRANGE | dateIdentified |  |  |
| IDENTIFIED_DATE_UNLIKELY | VALIDATION_DATEIDENTIFIED_STANDARD | dateIdentified |  |  |
| INCOMPLETE_COLLECTION_DATE | AMENDMENT_DATEIDENTIFIED_STANDARDIZED | dateIdentified |  |  |
| INCOMPLETE_COLLECTION_DATE | VALIDATION_DATEIDENTIFIED_INRANGE | dateIdentified |  |  |
| INCOMPLETE_COLLECTION_DATE | VALIDATION_DATEIDENTIFIED_STANDARD | dateIdentified |  |  |

## dwc:Occurrence

| ALA Assertion | BDQ Test | Connecting Terms | ALA-only Terms | BDQ-only Terms |
|---------------|----------|------------------|----------------|----------------|
| INDIVIDUAL_COUNT_CONFLICTS_WITH_OCCURRENCE_STATUS | AMENDMENT_OCCURRENCESTATUS_ASSUMEDDEFAULT | occurrenceStatus | individualCount |  |
| INDIVIDUAL_COUNT_CONFLICTS_WITH_OCCURRENCE_STATUS | AMENDMENT_OCCURRENCESTATUS_STANDARDIZED | occurrenceStatus | individualCount |  |
| INDIVIDUAL_COUNT_CONFLICTS_WITH_OCCURRENCE_STATUS | VALIDATION_OCCURRENCESTATUS_NOTEMPTY | occurrenceStatus | individualCount |  |
| INDIVIDUAL_COUNT_CONFLICTS_WITH_OCCURRENCE_STATUS | VALIDATION_OCCURRENCESTATUS_STANDARD | occurrenceStatus | individualCount |  |
| INDIVIDUAL_COUNT_INVALID | AMENDMENT_OCCURRENCESTATUS_ASSUMEDDEFAULT | occurrenceStatus | individualCount |  |
| INDIVIDUAL_COUNT_INVALID | AMENDMENT_OCCURRENCESTATUS_STANDARDIZED | occurrenceStatus | individualCount |  |
| INDIVIDUAL_COUNT_INVALID | VALIDATION_OCCURRENCESTATUS_NOTEMPTY | occurrenceStatus | individualCount |  |
| INDIVIDUAL_COUNT_INVALID | VALIDATION_OCCURRENCESTATUS_STANDARD | occurrenceStatus | individualCount |  |
| OCCURRENCE_STATUS_INFERRED_FROM_BASIS_OF_RECORD | AMENDMENT_OCCURRENCESTATUS_ASSUMEDDEFAULT | occurrenceStatus | basisOfRecord |  |
| OCCURRENCE_STATUS_INFERRED_FROM_BASIS_OF_RECORD | AMENDMENT_OCCURRENCESTATUS_STANDARDIZED | occurrenceStatus | basisOfRecord |  |
| OCCURRENCE_STATUS_INFERRED_FROM_BASIS_OF_RECORD | VALIDATION_OCCURRENCESTATUS_NOTEMPTY | occurrenceStatus | basisOfRecord |  |
| OCCURRENCE_STATUS_INFERRED_FROM_BASIS_OF_RECORD | VALIDATION_OCCURRENCESTATUS_STANDARD | occurrenceStatus | basisOfRecord |  |
| OCCURRENCE_STATUS_INFERRED_FROM_INDIVIDUAL_COUNT | AMENDMENT_OCCURRENCESTATUS_ASSUMEDDEFAULT | occurrenceStatus | individualCount |  |
| OCCURRENCE_STATUS_INFERRED_FROM_INDIVIDUAL_COUNT | AMENDMENT_OCCURRENCESTATUS_STANDARDIZED | occurrenceStatus | individualCount |  |
| OCCURRENCE_STATUS_INFERRED_FROM_INDIVIDUAL_COUNT | VALIDATION_OCCURRENCESTATUS_NOTEMPTY | occurrenceStatus | individualCount |  |
| OCCURRENCE_STATUS_INFERRED_FROM_INDIVIDUAL_COUNT | VALIDATION_OCCURRENCESTATUS_STANDARD | occurrenceStatus | individualCount |  |
| OCCURRENCE_STATUS_UNPARSABLE | AMENDMENT_OCCURRENCESTATUS_ASSUMEDDEFAULT | occurrenceStatus |  |  |
| OCCURRENCE_STATUS_UNPARSABLE | AMENDMENT_OCCURRENCESTATUS_STANDARDIZED | occurrenceStatus |  |  |
| OCCURRENCE_STATUS_UNPARSABLE | VALIDATION_OCCURRENCESTATUS_NOTEMPTY | occurrenceStatus |  |  |
| OCCURRENCE_STATUS_UNPARSABLE | VALIDATION_OCCURRENCESTATUS_STANDARD | occurrenceStatus |  |  |

## dwc:Taxon

| ALA Assertion | BDQ Test | Connecting Terms | ALA-only Terms | BDQ-only Terms |
|---------------|----------|------------------|----------------|----------------|
| INVALID_SCIENTIFIC_NAME | AMENDMENT_SCIENTIFICNAME_FROM_SCIENTIFICNAMEID | scientificName |  |  |
| INVALID_SCIENTIFIC_NAME | VALIDATION_POLYNOMIAL_CONSISTENT | scientificName |  | genericName, infraspecificEpithet, specificEpithet |
| INVALID_SCIENTIFIC_NAME | VALIDATION_SCIENTIFICNAME_FOUND | scientificName |  |  |
| INVALID_SCIENTIFIC_NAME | VALIDATION_SCIENTIFICNAME_NOTEMPTY | scientificName |  |  |
| INVALID_SCIENTIFIC_NAME | VALIDATION_TAXON_NOTEMPTY | scientificName |  | acceptedNameUsageID, class, cultivarEpithet, family, genericName, genus, higherClassification, infragenericEpithet, infraspecificEpithet, kingdom, order, originalNameUsageID, parentNameUsageID, phylum, scientificNameID, specificEpithet, subfamily, subgenus, subtribe, superfamily, taxonConceptID, taxonID, tribe, vernacularName |
| INVALID_SCIENTIFIC_NAME | VALIDATION_TAXON_UNAMBIGUOUS | scientificName |  | scientificNameID |
| MISSING_TAXONRANK | AMENDMENT_TAXONRANK_STANDARDIZED | taxonRank |  |  |
| MISSING_TAXONRANK | VALIDATION_TAXONRANK_NOTEMPTY | taxonRank |  |  |
| MISSING_TAXONRANK | VALIDATION_TAXONRANK_STANDARD | taxonRank |  |  |
| NAME_NOT_IN_NATIONAL_CHECKLISTS | AMENDMENT_SCIENTIFICNAME_FROM_SCIENTIFICNAMEID | scientificName |  |  |
| NAME_NOT_IN_NATIONAL_CHECKLISTS | VALIDATION_POLYNOMIAL_CONSISTENT | scientificName |  | genericName, infraspecificEpithet, specificEpithet |
| NAME_NOT_IN_NATIONAL_CHECKLISTS | VALIDATION_SCIENTIFICNAME_FOUND | scientificName |  |  |
| NAME_NOT_IN_NATIONAL_CHECKLISTS | VALIDATION_SCIENTIFICNAME_NOTEMPTY | scientificName |  |  |
| NAME_NOT_IN_NATIONAL_CHECKLISTS | VALIDATION_TAXON_NOTEMPTY | scientificName |  | acceptedNameUsageID, class, cultivarEpithet, family, genericName, genus, higherClassification, infragenericEpithet, infraspecificEpithet, kingdom, order, originalNameUsageID, parentNameUsageID, phylum, scientificNameID, specificEpithet, subfamily, subgenus, subtribe, superfamily, taxonConceptID, taxonID, tribe, vernacularName |
| NAME_NOT_IN_NATIONAL_CHECKLISTS | VALIDATION_TAXON_UNAMBIGUOUS | scientificName |  | scientificNameID |
| NAME_NOT_RECOGNISED | AMENDMENT_SCIENTIFICNAME_FROM_SCIENTIFICNAMEID | scientificName |  |  |
| NAME_NOT_RECOGNISED | VALIDATION_POLYNOMIAL_CONSISTENT | scientificName |  | genericName, infraspecificEpithet, specificEpithet |
| NAME_NOT_RECOGNISED | VALIDATION_SCIENTIFICNAME_FOUND | scientificName |  |  |
| NAME_NOT_RECOGNISED | VALIDATION_SCIENTIFICNAME_NOTEMPTY | scientificName |  |  |
| NAME_NOT_RECOGNISED | VALIDATION_TAXON_NOTEMPTY | scientificName |  | acceptedNameUsageID, class, cultivarEpithet, family, genericName, genus, higherClassification, infragenericEpithet, infraspecificEpithet, kingdom, order, originalNameUsageID, parentNameUsageID, phylum, scientificNameID, specificEpithet, subfamily, subgenus, subtribe, superfamily, taxonConceptID, taxonID, tribe, vernacularName |
| NAME_NOT_RECOGNISED | VALIDATION_TAXON_UNAMBIGUOUS | scientificName |  | scientificNameID |
| NAME_NOT_SUPPLIED | AMENDMENT_SCIENTIFICNAME_FROM_SCIENTIFICNAMEID | scientificName |  |  |
| NAME_NOT_SUPPLIED | VALIDATION_POLYNOMIAL_CONSISTENT | scientificName |  | genericName, infraspecificEpithet, specificEpithet |
| NAME_NOT_SUPPLIED | VALIDATION_SCIENTIFICNAME_FOUND | scientificName |  |  |
| NAME_NOT_SUPPLIED | VALIDATION_SCIENTIFICNAME_NOTEMPTY | scientificName |  |  |
| NAME_NOT_SUPPLIED | VALIDATION_TAXON_NOTEMPTY | scientificName |  | acceptedNameUsageID, class, cultivarEpithet, family, genericName, genus, higherClassification, infragenericEpithet, infraspecificEpithet, kingdom, order, originalNameUsageID, parentNameUsageID, phylum, scientificNameID, specificEpithet, subfamily, subgenus, subtribe, superfamily, taxonConceptID, taxonID, tribe, vernacularName |
| NAME_NOT_SUPPLIED | VALIDATION_TAXON_UNAMBIGUOUS | scientificName |  | scientificNameID |
| SENSITIVITY_REPORT_INVALID | AMENDMENT_SCIENTIFICNAME_FROM_SCIENTIFICNAMEID | scientificName | stateProvince |  |
| SENSITIVITY_REPORT_INVALID | VALIDATION_POLYNOMIAL_CONSISTENT | scientificName | stateProvince | genericName, infraspecificEpithet, specificEpithet |
| SENSITIVITY_REPORT_INVALID | VALIDATION_SCIENTIFICNAME_FOUND | scientificName | stateProvince |  |
| SENSITIVITY_REPORT_INVALID | VALIDATION_SCIENTIFICNAME_NOTEMPTY | scientificName | stateProvince |  |
| SENSITIVITY_REPORT_INVALID | VALIDATION_TAXON_NOTEMPTY | scientificName | stateProvince | acceptedNameUsageID, class, cultivarEpithet, family, genericName, genus, higherClassification, infragenericEpithet, infraspecificEpithet, kingdom, order, originalNameUsageID, parentNameUsageID, phylum, scientificNameID, specificEpithet, subfamily, subgenus, subtribe, superfamily, taxonConceptID, taxonID, tribe, vernacularName |
| SENSITIVITY_REPORT_INVALID | VALIDATION_TAXON_UNAMBIGUOUS | scientificName | stateProvince | scientificNameID |
| SENSITIVITY_REPORT_NOT_LOADABLE | AMENDMENT_SCIENTIFICNAME_FROM_SCIENTIFICNAMEID | scientificName | stateProvince |  |
| SENSITIVITY_REPORT_NOT_LOADABLE | VALIDATION_POLYNOMIAL_CONSISTENT | scientificName | stateProvince | genericName, infraspecificEpithet, specificEpithet |
| SENSITIVITY_REPORT_NOT_LOADABLE | VALIDATION_SCIENTIFICNAME_FOUND | scientificName | stateProvince |  |
| SENSITIVITY_REPORT_NOT_LOADABLE | VALIDATION_SCIENTIFICNAME_NOTEMPTY | scientificName | stateProvince |  |
| SENSITIVITY_REPORT_NOT_LOADABLE | VALIDATION_TAXON_NOTEMPTY | scientificName | stateProvince | acceptedNameUsageID, class, cultivarEpithet, family, genericName, genus, higherClassification, infragenericEpithet, infraspecificEpithet, kingdom, order, originalNameUsageID, parentNameUsageID, phylum, scientificNameID, specificEpithet, subfamily, subgenus, subtribe, superfamily, taxonConceptID, taxonID, tribe, vernacularName |
| SENSITIVITY_REPORT_NOT_LOADABLE | VALIDATION_TAXON_UNAMBIGUOUS | scientificName | stateProvince | scientificNameID |
| TAXON_AFFINITY_SPECIES | AMENDMENT_SCIENTIFICNAME_FROM_SCIENTIFICNAMEID | scientificName |  |  |
| TAXON_AFFINITY_SPECIES | VALIDATION_POLYNOMIAL_CONSISTENT | scientificName |  | genericName, infraspecificEpithet, specificEpithet |
| TAXON_AFFINITY_SPECIES | VALIDATION_SCIENTIFICNAME_FOUND | scientificName |  |  |
| TAXON_AFFINITY_SPECIES | VALIDATION_SCIENTIFICNAME_NOTEMPTY | scientificName |  |  |
| TAXON_AFFINITY_SPECIES | VALIDATION_TAXON_NOTEMPTY | scientificName |  | acceptedNameUsageID, class, cultivarEpithet, family, genericName, genus, higherClassification, infragenericEpithet, infraspecificEpithet, kingdom, order, originalNameUsageID, parentNameUsageID, phylum, scientificNameID, specificEpithet, subfamily, subgenus, subtribe, superfamily, taxonConceptID, taxonID, tribe, vernacularName |
| TAXON_AFFINITY_SPECIES | VALIDATION_TAXON_UNAMBIGUOUS | scientificName |  | scientificNameID |
| TAXON_CONFER_SPECIES | AMENDMENT_SCIENTIFICNAME_FROM_SCIENTIFICNAMEID | scientificName |  |  |
| TAXON_CONFER_SPECIES | VALIDATION_POLYNOMIAL_CONSISTENT | scientificName |  | genericName, infraspecificEpithet, specificEpithet |
| TAXON_CONFER_SPECIES | VALIDATION_SCIENTIFICNAME_FOUND | scientificName |  |  |
| TAXON_CONFER_SPECIES | VALIDATION_SCIENTIFICNAME_NOTEMPTY | scientificName |  |  |
| TAXON_CONFER_SPECIES | VALIDATION_TAXON_NOTEMPTY | scientificName |  | acceptedNameUsageID, class, cultivarEpithet, family, genericName, genus, higherClassification, infragenericEpithet, infraspecificEpithet, kingdom, order, originalNameUsageID, parentNameUsageID, phylum, scientificNameID, specificEpithet, subfamily, subgenus, subtribe, superfamily, taxonConceptID, taxonID, tribe, vernacularName |
| TAXON_CONFER_SPECIES | VALIDATION_TAXON_UNAMBIGUOUS | scientificName |  | scientificNameID |
| TAXON_DEFAULT_MATCH | AMENDMENT_SCIENTIFICNAME_FROM_SCIENTIFICNAMEID | scientificName |  |  |
| TAXON_DEFAULT_MATCH | VALIDATION_POLYNOMIAL_CONSISTENT | scientificName |  | genericName, infraspecificEpithet, specificEpithet |
| TAXON_DEFAULT_MATCH | VALIDATION_SCIENTIFICNAME_FOUND | scientificName |  |  |
| TAXON_DEFAULT_MATCH | VALIDATION_SCIENTIFICNAME_NOTEMPTY | scientificName |  |  |
| TAXON_DEFAULT_MATCH | VALIDATION_TAXON_NOTEMPTY | scientificName |  | acceptedNameUsageID, class, cultivarEpithet, family, genericName, genus, higherClassification, infragenericEpithet, infraspecificEpithet, kingdom, order, originalNameUsageID, parentNameUsageID, phylum, scientificNameID, specificEpithet, subfamily, subgenus, subtribe, superfamily, taxonConceptID, taxonID, tribe, vernacularName |
| TAXON_DEFAULT_MATCH | VALIDATION_TAXON_UNAMBIGUOUS | scientificName |  | scientificNameID |
| TAXON_ERROR | AMENDMENT_SCIENTIFICNAME_FROM_SCIENTIFICNAMEID | scientificName |  |  |
| TAXON_ERROR | VALIDATION_POLYNOMIAL_CONSISTENT | scientificName |  | genericName, infraspecificEpithet, specificEpithet |
| TAXON_ERROR | VALIDATION_SCIENTIFICNAME_FOUND | scientificName |  |  |
| TAXON_ERROR | VALIDATION_SCIENTIFICNAME_NOTEMPTY | scientificName |  |  |
| TAXON_ERROR | VALIDATION_TAXON_NOTEMPTY | scientificName |  | acceptedNameUsageID, class, cultivarEpithet, family, genericName, genus, higherClassification, infragenericEpithet, infraspecificEpithet, kingdom, order, originalNameUsageID, parentNameUsageID, phylum, scientificNameID, specificEpithet, subfamily, subgenus, subtribe, superfamily, taxonConceptID, taxonID, tribe, vernacularName |
| TAXON_ERROR | VALIDATION_TAXON_UNAMBIGUOUS | scientificName |  | scientificNameID |
| TAXON_EXCLUDED | AMENDMENT_SCIENTIFICNAME_FROM_SCIENTIFICNAMEID | scientificName |  |  |
| TAXON_EXCLUDED | VALIDATION_POLYNOMIAL_CONSISTENT | scientificName |  | genericName, infraspecificEpithet, specificEpithet |
| TAXON_EXCLUDED | VALIDATION_SCIENTIFICNAME_FOUND | scientificName |  |  |
| TAXON_EXCLUDED | VALIDATION_SCIENTIFICNAME_NOTEMPTY | scientificName |  |  |
| TAXON_EXCLUDED | VALIDATION_TAXON_NOTEMPTY | scientificName |  | acceptedNameUsageID, class, cultivarEpithet, family, genericName, genus, higherClassification, infragenericEpithet, infraspecificEpithet, kingdom, order, originalNameUsageID, parentNameUsageID, phylum, scientificNameID, specificEpithet, subfamily, subgenus, subtribe, superfamily, taxonConceptID, taxonID, tribe, vernacularName |
| TAXON_EXCLUDED | VALIDATION_TAXON_UNAMBIGUOUS | scientificName |  | scientificNameID |
| TAXON_EXCLUDED_ASSOCIATED | AMENDMENT_SCIENTIFICNAME_FROM_SCIENTIFICNAMEID | scientificName |  |  |
| TAXON_EXCLUDED_ASSOCIATED | VALIDATION_POLYNOMIAL_CONSISTENT | scientificName |  | genericName, infraspecificEpithet, specificEpithet |
| TAXON_EXCLUDED_ASSOCIATED | VALIDATION_SCIENTIFICNAME_FOUND | scientificName |  |  |
| TAXON_EXCLUDED_ASSOCIATED | VALIDATION_SCIENTIFICNAME_NOTEMPTY | scientificName |  |  |
| TAXON_EXCLUDED_ASSOCIATED | VALIDATION_TAXON_NOTEMPTY | scientificName |  | acceptedNameUsageID, class, cultivarEpithet, family, genericName, genus, higherClassification, infragenericEpithet, infraspecificEpithet, kingdom, order, originalNameUsageID, parentNameUsageID, phylum, scientificNameID, specificEpithet, subfamily, subgenus, subtribe, superfamily, taxonConceptID, taxonID, tribe, vernacularName |
| TAXON_EXCLUDED_ASSOCIATED | VALIDATION_TAXON_UNAMBIGUOUS | scientificName |  | scientificNameID |
| TAXON_HOMONYM | AMENDMENT_SCIENTIFICNAME_FROM_SCIENTIFICNAMEID | scientificName |  |  |
| TAXON_HOMONYM | VALIDATION_POLYNOMIAL_CONSISTENT | scientificName |  | genericName, infraspecificEpithet, specificEpithet |
| TAXON_HOMONYM | VALIDATION_SCIENTIFICNAME_FOUND | scientificName |  |  |
| TAXON_HOMONYM | VALIDATION_SCIENTIFICNAME_NOTEMPTY | scientificName |  |  |
| TAXON_HOMONYM | VALIDATION_TAXON_NOTEMPTY | scientificName |  | acceptedNameUsageID, class, cultivarEpithet, family, genericName, genus, higherClassification, infragenericEpithet, infraspecificEpithet, kingdom, order, originalNameUsageID, parentNameUsageID, phylum, scientificNameID, specificEpithet, subfamily, subgenus, subtribe, superfamily, taxonConceptID, taxonID, tribe, vernacularName |
| TAXON_HOMONYM | VALIDATION_TAXON_UNAMBIGUOUS | scientificName |  | scientificNameID |
| TAXON_INDETERMINATE_SPECIES | AMENDMENT_SCIENTIFICNAME_FROM_SCIENTIFICNAMEID | scientificName |  |  |
| TAXON_INDETERMINATE_SPECIES | VALIDATION_POLYNOMIAL_CONSISTENT | scientificName |  | genericName, infraspecificEpithet, specificEpithet |
| TAXON_INDETERMINATE_SPECIES | VALIDATION_SCIENTIFICNAME_FOUND | scientificName |  |  |
| TAXON_INDETERMINATE_SPECIES | VALIDATION_SCIENTIFICNAME_NOTEMPTY | scientificName |  |  |
| TAXON_INDETERMINATE_SPECIES | VALIDATION_TAXON_NOTEMPTY | scientificName |  | acceptedNameUsageID, class, cultivarEpithet, family, genericName, genus, higherClassification, infragenericEpithet, infraspecificEpithet, kingdom, order, originalNameUsageID, parentNameUsageID, phylum, scientificNameID, specificEpithet, subfamily, subgenus, subtribe, superfamily, taxonConceptID, taxonID, tribe, vernacularName |
| TAXON_INDETERMINATE_SPECIES | VALIDATION_TAXON_UNAMBIGUOUS | scientificName |  | scientificNameID |
| TAXON_MATCH_AGGREGATE | AMENDMENT_SCIENTIFICNAME_FROM_SCIENTIFICNAMEID | scientificName |  |  |
| TAXON_MATCH_AGGREGATE | VALIDATION_POLYNOMIAL_CONSISTENT | scientificName |  | genericName, infraspecificEpithet, specificEpithet |
| TAXON_MATCH_AGGREGATE | VALIDATION_SCIENTIFICNAME_FOUND | scientificName |  |  |
| TAXON_MATCH_AGGREGATE | VALIDATION_SCIENTIFICNAME_NOTEMPTY | scientificName |  |  |
| TAXON_MATCH_AGGREGATE | VALIDATION_TAXON_NOTEMPTY | scientificName |  | acceptedNameUsageID, class, cultivarEpithet, family, genericName, genus, higherClassification, infragenericEpithet, infraspecificEpithet, kingdom, order, originalNameUsageID, parentNameUsageID, phylum, scientificNameID, specificEpithet, subfamily, subgenus, subtribe, superfamily, taxonConceptID, taxonID, tribe, vernacularName |
| TAXON_MATCH_AGGREGATE | VALIDATION_TAXON_UNAMBIGUOUS | scientificName |  | scientificNameID |
| TAXON_MATCH_FUZZY | AMENDMENT_SCIENTIFICNAME_FROM_SCIENTIFICNAMEID | scientificName |  |  |
| TAXON_MATCH_FUZZY | VALIDATION_POLYNOMIAL_CONSISTENT | scientificName |  | genericName, infraspecificEpithet, specificEpithet |
| TAXON_MATCH_FUZZY | VALIDATION_SCIENTIFICNAME_FOUND | scientificName |  |  |
| TAXON_MATCH_FUZZY | VALIDATION_SCIENTIFICNAME_NOTEMPTY | scientificName |  |  |
| TAXON_MATCH_FUZZY | VALIDATION_TAXON_NOTEMPTY | scientificName |  | acceptedNameUsageID, class, cultivarEpithet, family, genericName, genus, higherClassification, infragenericEpithet, infraspecificEpithet, kingdom, order, originalNameUsageID, parentNameUsageID, phylum, scientificNameID, specificEpithet, subfamily, subgenus, subtribe, superfamily, taxonConceptID, taxonID, tribe, vernacularName |
| TAXON_MATCH_FUZZY | VALIDATION_TAXON_UNAMBIGUOUS | scientificName |  | scientificNameID |
| TAXON_MATCH_HIGHERRANK | AMENDMENT_SCIENTIFICNAME_FROM_SCIENTIFICNAMEID | scientificName | class, family, genus, kingdom, order, phylum |  |
| TAXON_MATCH_HIGHERRANK | VALIDATION_CLASSIFICATION_CONSISTENT | class, family, genus, kingdom, order, phylum | scientificName | subfamily, subtribe, superfamily, tribe |
| TAXON_MATCH_HIGHERRANK | VALIDATION_CLASS_FOUND | class | family, genus, kingdom, order, phylum, scientificName |  |
| TAXON_MATCH_HIGHERRANK | VALIDATION_FAMILY_FOUND | family | class, genus, kingdom, order, phylum, scientificName |  |
| TAXON_MATCH_HIGHERRANK | VALIDATION_GENUS_FOUND | genus | class, family, kingdom, order, phylum, scientificName |  |
| TAXON_MATCH_HIGHERRANK | VALIDATION_KINGDOM_FOUND | kingdom | class, family, genus, order, phylum, scientificName |  |
| TAXON_MATCH_HIGHERRANK | VALIDATION_KINGDOM_NOTEMPTY | kingdom | class, family, genus, order, phylum, scientificName |  |
| TAXON_MATCH_HIGHERRANK | VALIDATION_ORDER_FOUND | order | class, family, genus, kingdom, phylum, scientificName |  |
| TAXON_MATCH_HIGHERRANK | VALIDATION_PHYLUM_FOUND | phylum | class, family, genus, kingdom, order, scientificName |  |
| TAXON_MATCH_HIGHERRANK | VALIDATION_POLYNOMIAL_CONSISTENT | scientificName | class, family, genus, kingdom, order, phylum | genericName, infraspecificEpithet, specificEpithet |
| TAXON_MATCH_HIGHERRANK | VALIDATION_SCIENTIFICNAME_FOUND | scientificName | class, family, genus, kingdom, order, phylum |  |
| TAXON_MATCH_HIGHERRANK | VALIDATION_SCIENTIFICNAME_NOTEMPTY | scientificName | class, family, genus, kingdom, order, phylum |  |
| TAXON_MATCH_HIGHERRANK | VALIDATION_TAXON_NOTEMPTY | class, family, genus, kingdom, order, phylum, scientificName |  | acceptedNameUsageID, cultivarEpithet, genericName, higherClassification, infragenericEpithet, infraspecificEpithet, originalNameUsageID, parentNameUsageID, scientificNameID, specificEpithet, subfamily, subgenus, subtribe, superfamily, taxonConceptID, taxonID, tribe, vernacularName |
| TAXON_MATCH_HIGHERRANK | VALIDATION_TAXON_UNAMBIGUOUS | scientificName | class, family, genus, kingdom, order, phylum | scientificNameID |
| TAXON_MATCH_NONE | AMENDMENT_SCIENTIFICNAME_FROM_SCIENTIFICNAMEID | scientificName | class, family, genus, kingdom, order, phylum |  |
| TAXON_MATCH_NONE | VALIDATION_CLASSIFICATION_CONSISTENT | class, family, genus, kingdom, order, phylum | scientificName | subfamily, subtribe, superfamily, tribe |
| TAXON_MATCH_NONE | VALIDATION_CLASS_FOUND | class | family, genus, kingdom, order, phylum, scientificName |  |
| TAXON_MATCH_NONE | VALIDATION_FAMILY_FOUND | family | class, genus, kingdom, order, phylum, scientificName |  |
| TAXON_MATCH_NONE | VALIDATION_GENUS_FOUND | genus | class, family, kingdom, order, phylum, scientificName |  |
| TAXON_MATCH_NONE | VALIDATION_KINGDOM_FOUND | kingdom | class, family, genus, order, phylum, scientificName |  |
| TAXON_MATCH_NONE | VALIDATION_KINGDOM_NOTEMPTY | kingdom | class, family, genus, order, phylum, scientificName |  |
| TAXON_MATCH_NONE | VALIDATION_ORDER_FOUND | order | class, family, genus, kingdom, phylum, scientificName |  |
| TAXON_MATCH_NONE | VALIDATION_PHYLUM_FOUND | phylum | class, family, genus, kingdom, order, scientificName |  |
| TAXON_MATCH_NONE | VALIDATION_POLYNOMIAL_CONSISTENT | scientificName | class, family, genus, kingdom, order, phylum | genericName, infraspecificEpithet, specificEpithet |
| TAXON_MATCH_NONE | VALIDATION_SCIENTIFICNAME_FOUND | scientificName | class, family, genus, kingdom, order, phylum |  |
| TAXON_MATCH_NONE | VALIDATION_SCIENTIFICNAME_NOTEMPTY | scientificName | class, family, genus, kingdom, order, phylum |  |
| TAXON_MATCH_NONE | VALIDATION_TAXON_NOTEMPTY | class, family, genus, kingdom, order, phylum, scientificName |  | acceptedNameUsageID, cultivarEpithet, genericName, higherClassification, infragenericEpithet, infraspecificEpithet, originalNameUsageID, parentNameUsageID, scientificNameID, specificEpithet, subfamily, subgenus, subtribe, superfamily, taxonConceptID, taxonID, tribe, vernacularName |
| TAXON_MATCH_NONE | VALIDATION_TAXON_UNAMBIGUOUS | scientificName | class, family, genus, kingdom, order, phylum | scientificNameID |
| TAXON_MISAPPLIED | AMENDMENT_SCIENTIFICNAME_FROM_SCIENTIFICNAMEID | scientificName |  |  |
| TAXON_MISAPPLIED | VALIDATION_POLYNOMIAL_CONSISTENT | scientificName |  | genericName, infraspecificEpithet, specificEpithet |
| TAXON_MISAPPLIED | VALIDATION_SCIENTIFICNAME_FOUND | scientificName |  |  |
| TAXON_MISAPPLIED | VALIDATION_SCIENTIFICNAME_NOTEMPTY | scientificName |  |  |
| TAXON_MISAPPLIED | VALIDATION_TAXON_NOTEMPTY | scientificName |  | acceptedNameUsageID, class, cultivarEpithet, family, genericName, genus, higherClassification, infragenericEpithet, infraspecificEpithet, kingdom, order, originalNameUsageID, parentNameUsageID, phylum, scientificNameID, specificEpithet, subfamily, subgenus, subtribe, superfamily, taxonConceptID, taxonID, tribe, vernacularName |
| TAXON_MISAPPLIED | VALIDATION_TAXON_UNAMBIGUOUS | scientificName |  | scientificNameID |
| TAXON_MISAPPLIED_MATCHED | AMENDMENT_SCIENTIFICNAME_FROM_SCIENTIFICNAMEID | scientificName |  |  |
| TAXON_MISAPPLIED_MATCHED | VALIDATION_POLYNOMIAL_CONSISTENT | scientificName |  | genericName, infraspecificEpithet, specificEpithet |
| TAXON_MISAPPLIED_MATCHED | VALIDATION_SCIENTIFICNAME_FOUND | scientificName |  |  |
| TAXON_MISAPPLIED_MATCHED | VALIDATION_SCIENTIFICNAME_NOTEMPTY | scientificName |  |  |
| TAXON_MISAPPLIED_MATCHED | VALIDATION_TAXON_NOTEMPTY | scientificName |  | acceptedNameUsageID, class, cultivarEpithet, family, genericName, genus, higherClassification, infragenericEpithet, infraspecificEpithet, kingdom, order, originalNameUsageID, parentNameUsageID, phylum, scientificNameID, specificEpithet, subfamily, subgenus, subtribe, superfamily, taxonConceptID, taxonID, tribe, vernacularName |
| TAXON_MISAPPLIED_MATCHED | VALIDATION_TAXON_UNAMBIGUOUS | scientificName |  | scientificNameID |
| TAXON_PARENT_CHILD_SYNONYM | AMENDMENT_SCIENTIFICNAME_FROM_SCIENTIFICNAMEID | scientificName |  |  |
| TAXON_PARENT_CHILD_SYNONYM | VALIDATION_POLYNOMIAL_CONSISTENT | scientificName |  | genericName, infraspecificEpithet, specificEpithet |
| TAXON_PARENT_CHILD_SYNONYM | VALIDATION_SCIENTIFICNAME_FOUND | scientificName |  |  |
| TAXON_PARENT_CHILD_SYNONYM | VALIDATION_SCIENTIFICNAME_NOTEMPTY | scientificName |  |  |
| TAXON_PARENT_CHILD_SYNONYM | VALIDATION_TAXON_NOTEMPTY | scientificName |  | acceptedNameUsageID, class, cultivarEpithet, family, genericName, genus, higherClassification, infragenericEpithet, infraspecificEpithet, kingdom, order, originalNameUsageID, parentNameUsageID, phylum, scientificNameID, specificEpithet, subfamily, subgenus, subtribe, superfamily, taxonConceptID, taxonID, tribe, vernacularName |
| TAXON_PARENT_CHILD_SYNONYM | VALIDATION_TAXON_UNAMBIGUOUS | scientificName |  | scientificNameID |
| TAXON_QUESTION_SPECIES | AMENDMENT_SCIENTIFICNAME_FROM_SCIENTIFICNAMEID | scientificName |  |  |
| TAXON_QUESTION_SPECIES | VALIDATION_POLYNOMIAL_CONSISTENT | scientificName |  | genericName, infraspecificEpithet, specificEpithet |
| TAXON_QUESTION_SPECIES | VALIDATION_SCIENTIFICNAME_FOUND | scientificName |  |  |
| TAXON_QUESTION_SPECIES | VALIDATION_SCIENTIFICNAME_NOTEMPTY | scientificName |  |  |
| TAXON_QUESTION_SPECIES | VALIDATION_TAXON_NOTEMPTY | scientificName |  | acceptedNameUsageID, class, cultivarEpithet, family, genericName, genus, higherClassification, infragenericEpithet, infraspecificEpithet, kingdom, order, originalNameUsageID, parentNameUsageID, phylum, scientificNameID, specificEpithet, subfamily, subgenus, subtribe, superfamily, taxonConceptID, taxonID, tribe, vernacularName |
| TAXON_QUESTION_SPECIES | VALIDATION_TAXON_UNAMBIGUOUS | scientificName |  | scientificNameID |
| TAXON_SCOPE_MISMATCH | AMENDMENT_SCIENTIFICNAME_FROM_SCIENTIFICNAMEID | scientificName | class, family, genus, kingdom, order, phylum |  |
| TAXON_SCOPE_MISMATCH | VALIDATION_CLASSIFICATION_CONSISTENT | class, family, genus, kingdom, order, phylum | scientificName | subfamily, subtribe, superfamily, tribe |
| TAXON_SCOPE_MISMATCH | VALIDATION_CLASS_FOUND | class | family, genus, kingdom, order, phylum, scientificName |  |
| TAXON_SCOPE_MISMATCH | VALIDATION_FAMILY_FOUND | family | class, genus, kingdom, order, phylum, scientificName |  |
| TAXON_SCOPE_MISMATCH | VALIDATION_GENUS_FOUND | genus | class, family, kingdom, order, phylum, scientificName |  |
| TAXON_SCOPE_MISMATCH | VALIDATION_KINGDOM_FOUND | kingdom | class, family, genus, order, phylum, scientificName |  |
| TAXON_SCOPE_MISMATCH | VALIDATION_KINGDOM_NOTEMPTY | kingdom | class, family, genus, order, phylum, scientificName |  |
| TAXON_SCOPE_MISMATCH | VALIDATION_ORDER_FOUND | order | class, family, genus, kingdom, phylum, scientificName |  |
| TAXON_SCOPE_MISMATCH | VALIDATION_PHYLUM_FOUND | phylum | class, family, genus, kingdom, order, scientificName |  |
| TAXON_SCOPE_MISMATCH | VALIDATION_POLYNOMIAL_CONSISTENT | scientificName | class, family, genus, kingdom, order, phylum | genericName, infraspecificEpithet, specificEpithet |
| TAXON_SCOPE_MISMATCH | VALIDATION_SCIENTIFICNAME_FOUND | scientificName | class, family, genus, kingdom, order, phylum |  |
| TAXON_SCOPE_MISMATCH | VALIDATION_SCIENTIFICNAME_NOTEMPTY | scientificName | class, family, genus, kingdom, order, phylum |  |
| TAXON_SCOPE_MISMATCH | VALIDATION_TAXON_NOTEMPTY | class, family, genus, kingdom, order, phylum, scientificName |  | acceptedNameUsageID, cultivarEpithet, genericName, higherClassification, infragenericEpithet, infraspecificEpithet, originalNameUsageID, parentNameUsageID, scientificNameID, specificEpithet, subfamily, subgenus, subtribe, superfamily, taxonConceptID, taxonID, tribe, vernacularName |
| TAXON_SCOPE_MISMATCH | VALIDATION_TAXON_UNAMBIGUOUS | scientificName | class, family, genus, kingdom, order, phylum | scientificNameID |
| TAXON_SPECIES_PLURAL | AMENDMENT_SCIENTIFICNAME_FROM_SCIENTIFICNAMEID | scientificName |  |  |
| TAXON_SPECIES_PLURAL | VALIDATION_POLYNOMIAL_CONSISTENT | scientificName |  | genericName, infraspecificEpithet, specificEpithet |
| TAXON_SPECIES_PLURAL | VALIDATION_SCIENTIFICNAME_FOUND | scientificName |  |  |
| TAXON_SPECIES_PLURAL | VALIDATION_SCIENTIFICNAME_NOTEMPTY | scientificName |  |  |
| TAXON_SPECIES_PLURAL | VALIDATION_TAXON_NOTEMPTY | scientificName |  | acceptedNameUsageID, class, cultivarEpithet, family, genericName, genus, higherClassification, infragenericEpithet, infraspecificEpithet, kingdom, order, originalNameUsageID, parentNameUsageID, phylum, scientificNameID, specificEpithet, subfamily, subgenus, subtribe, superfamily, taxonConceptID, taxonID, tribe, vernacularName |
| TAXON_SPECIES_PLURAL | VALIDATION_TAXON_UNAMBIGUOUS | scientificName |  | scientificNameID |
| UNKNOWN_KINGDOM | VALIDATION_CLASSIFICATION_CONSISTENT | kingdom |  | class, family, genus, order, phylum, subfamily, subtribe, superfamily, tribe |
| UNKNOWN_KINGDOM | VALIDATION_KINGDOM_FOUND | kingdom |  |  |
| UNKNOWN_KINGDOM | VALIDATION_KINGDOM_NOTEMPTY | kingdom |  |  |
| UNKNOWN_KINGDOM | VALIDATION_TAXON_NOTEMPTY | kingdom |  | acceptedNameUsageID, class, cultivarEpithet, family, genericName, genus, higherClassification, infragenericEpithet, infraspecificEpithet, order, originalNameUsageID, parentNameUsageID, phylum, scientificName, scientificNameID, specificEpithet, subfamily, subgenus, subtribe, superfamily, taxonConceptID, taxonID, tribe, vernacularName |

