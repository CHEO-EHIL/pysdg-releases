# Changelog

All notable changes to this project are documented in this file.

## [2.0.0b] - 2024-07-24

### Added

- Initial release of pysdg v2 forked from v1.1.14b and based on python 3.10.

### Changed

- The naive_read function is eliminated and incorporated into Generator.load method. Further, unify_na in v2 takes place during loading and not unloading.
- Generator.train method takes a training subset as an option.

## [2.0.1b] - 2024-07-24

### Added

- In Generator.load method, added the option of enforcing user-defined datatype as given in the json to both the soul and its ghosts. The default is to use pandas reading defaults.

## [2.0.2b] - 2024-07-26 (Unreleased)

### Added

- In Generator.load method, allowed the user to input either a path to the csv file or a Pandas dataframe.
- In Generator.load method, allowed the user to input either a path to the json file or a dictionary.

## [2.0.3b] - 2024-07-29

### Fixed

- Fixed Replica encoding issue.

## [2.0.4b] - 2024-07-29 (Unreleased)

### Fixed

- Fixed Replica data type discrepancy between soul and ghosts.

## [2.0.5b] - 2024-07-30

### Fixed

- Fixed Replica data type error in encoded ghosts.
- Updated R installation documentation.

### Added

- Added R usage documentation.

## [2.0.6b] - 2024-07-31 (Unreleased)

### Fixed

- Fixed error when passing a combination of dataframe and json path to Generator.load method.

## [2.0.7b] - 2024-08-02

### Fixed

- Fixed a discrepancy between soul and ghost if special missing value is defined in the json file and Replica generator is used.
- Fixed datetime processing.
- Fixed NaT incompatibility with R.

### Added

- Added suppress_errors attribute to the Generator class. The attribute allows users to deal with erratic entries in numeric variables as missing values.

### Changed

- Suppressed warnings.

## [2.0.8b] - 2024-08-06 (Unreleased)

### Fixed

- Fixed discrepancy in data types between soul and ghosts for Replica.

### Changed

- Set the default for enforcing json types in the Generator.load method to True.

## [2.1.0b] - 2024-08-08

### Added

- Added four more Synthcity generators, namely: "synthcity_nflow","synthcity_rtvae","synthcity_gogle","synthcity_arf".
- Added do_sweep_replica function to allow users to manually delete Replica working folders.
- Added Generator.sweep_replica attribute and set it to True as a default. This will delete replica files automatically once ghosts are unloaded.
- Added Generator.replica_ids attribute to retrieve generated replica jobs.

## [2.1.1b] - 2024-08-09 (Unreleased)

### Added

- Added to the function <get_replica_risk> the option to delete Replica working folder by setting <sweep_replica_jobs> to True (default).

## [2.1.2b] - 2024-08-16 (Unreleased)

### Fixed

- Fixed datetime type discrepancies in soul and ghost.
- Fixed Replica occasional invalid output for categorical variables.
- Fixed logical error in previous erratic release

### Changed

- Dropped json_type option in Generator.load to enforce identical data types in soul and ghosts as per the input json file.

### Known Issues

- Encoded ghosts deformed due to data type conversion.

## [2.1.3b] - 2024-08-16 (Unreleased)

### Fixed

- Fixed the error in the previous version that forced all logical columns to equate to True.
- Fixed incorrect identification of missing values as erratic.

## [2.1.4b] - 2024-08-20 (Unreleased)

### Fixed

- Error loading the .env file for Replica generator.

## [2.1.5b] - 2024-08-20 (Unreleased)

### Fixed

- Mismatch in shape error in synthcity_ctgan for heavily unbalanced categorical variables.
- 'synthcity_goggle' generator is removed since it is not recognized by synthcity anymore.

### Changed

- For all attributes of Generator, replaced the term "soul" by "real" and the term "ghost" by "synth".

## [2.1.6b] - 2024-08-30 (Unreleased)

### Fixed

- Fixed Replica misinterpretation of high cardinality categorical variables.

### Added

- Added inspect_data function to assist json file creator locating any discrepancies.

## [2.1.6rc0] - 2024-09-06

### Added

- Verified the availability of the Replica library.

## [2.2.0b] - 2024-09-26

### Added

- Introduced a standalone function to compute membership disclosure risk.
- Added a function to remove unnecessary global variables.

### Deprecated

The class `MmbrshpRsk` may be **deprecated** in the upcoming release. Please update your code to use `calc_mmbrshp_risk` function instead.

### Changed

- Improved code readability.

## [2.3.0rc0] - 2024-11-23

### Added

- Added Bayesian optimization feature for CTGAN, along with a tutorial.
- Added option to log output to a file.
- Added option to specify the maximum number of cores.
- Added detection of duplicate index entries in the json input file for the Generator.

### Fixed

- Improved performance for handling erratic values in datasets.
- Eliminated unnecessary print statements and redundant logic.

### Changed

- In the `Generator.gen` method, replaced `no_obsvs` with `num_rows` and `no_synths` with `num_synths`. Both `no_obsvs` and `no_synths` are still supported but will be deprecated in future releases.

## [2.3.0] - 2024-12-02

### Added

- Added the `restore_col_names` method to the `Generator` class, allowing users to retrieve the encoded dataframe with the original column names.

## [2.4.0a] - 2025-01-28 (Unreleased)

### Added

- Added Yandex diffusion model `yandex_tabddpm`.
- Added possibility to save selected models, pickle artifacts and retrieve them.
- Added Python and R tutorials for calculating membership disclosure.
- Added dummy generator.
- Added capapbility to log to a file for testing.
- Added tutorial for Hmedian Hellinger distance.

### Changed

- Changed workspace naming by including the  Prrocess ID.

### Fixed

- Cleared log handlers before starting pysdg.

## [2.4.0b] - 2025-01-30 (Unreleased)

### Fixed

- Corrected the membership disclosure algorithm.

## [2.4.2b] - 2025-02-05

### Fixed

- Ensured SDV library is installed.

### Added

- Added the option to pass data info json/dict to membership disclosure function
