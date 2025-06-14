# Changelog
This file documents the notable changes to this project. Only selected versions are released.

## [2.7.2] - 2025-06-12
- **Fixed** Automatic deletion of  user's work directory if the model is not saved.
- **Fixed** Incorrect location of temporary folder for `yandex/tabddpm` when generating from a saved model.

## [2.7.1] - 2025-05-21
- **Fixed** Error thrown if `quasi_idxs` key is missing from the input `json` info file.
- **Fixed** Incorrect number of rows generated in `yandex/tabddpm` (#71).
- **Changed** Eliminated dependency on `tomli_i`
- **Fixed** `pysdg_vault_path` does not work in `gen.gen()` for `yandex/tabddpm` (#70)


## [2.7.0] - 2025-05-12
- **Warning:** This release is **NOT** compatible with previous versions due to module restructuring and function renaming.
- **Changed** Removed all metrics.
- **Changed** Restructured package. 

## [2.6.0b0] - 2025-05-06
- **Added:** Amazon Tabsyn transformer/diffusion-based generator `amazon/tabsyn`.
- **Corrected:** Checking by `bool` in `Generator.gen` method is replaced by checking by column name if `_missing` is included.

## [2.5.0rc1] - 2025-04-02
- **Fixed:** Hamming distance between NaNs in `calc_membership_vuln`.
- **Added:** A boolean argument `na_is_match` in `calc_membership_vuln` to treat compared NAs as match to mismatch when calculating the Hamming distance.

## [2.5.0rc0] - 2025-04-02
- **Warning:** This release is **NOT** compatible with previous versions due to module restructuring and function renaming.
- **Changed:** Module names have been updated to align with the new naming conventions.
- **Deprecated:** `calc_membership_risk`. Use `calc_membership_vuln`.
- **Deprecated:** `calc_attribution_risk`. Use `calc_attribute_vuln_replica`.
- **Deprecated:** `calc_inference_risk`. Use `calc_attribution_vuln`.
- **Fixed:** Bug in copula metadata generation.
- **Changed:** Improved documentation and added references.

## [2.4.4b4] - 2025-03-27 (**RELEASED - BETA**)
- **Fixed:** Error thrown by `calc_univar_hellinger_distance` when encoded columns of real and synth data do not match.
- **Fixed:** Median calculation in `calc_univar_hellinger_distance` when NA is encountered.
- **Fixed:** Multivariate Hellinger distance datatime handling.
- **Added:** Inference risk privacy metric.
- **Added:** Vulnerability-utility metric.

## [2.4.4b3] - 2025-03-06
- **Added:** Default option to infer datatypes in addition to explicitly passing the JSON file for the input dataset in the `Generator` class.
- **Added:** Function to calculate multivariate Hellinger distance `calc_multivar_hellinger_distance`.
- **Deprecated:** Renamed the function `calc_mmbrshp_risk` to `calc_membership_risk`.
- **Deprecated:** Renamed the function `calc_univariate_hlngr_distance` to `calc_univar_hellinger_distance`.
- **Fixed:** Issue with "Failed to remove 'None'" in the `unload` method.
- **Added:** Support for specifying generator names in the format `source/generator` (e.g., `synthcity/ctgan`). The old format remains functional.
- **Added:** Introduced the `gen_params` attribute in `Generator` to allow users to define generator hyperparameters in the format used by the generator's source, replacing the `synthcity_params` attribute, which will eventually be deprecated.
- **Changed:** Redefined estimate agreement to indicate whether the synthetic data estimate falls within the confidence interval (CI) of the real data.

## [2.4.4b2] - 2025-02-07 (**RELEASED - BETA**)
- **Fixed:** The calculation of directional decision agreement.
- **Deprecated:** The `compare_estimates` function no longer returns an array. It now returns a dictionary instead. The array return is deprecated.

## [2.4.3b0] - 2025-02-07 (**RELEASED - BETA**)
- **Fixed:** Handling incorrect `quasi_vars` in the membership disclosure function.

## [2.4.2b] - 2025-02-05
- **Added:** Option to pass data info as `json/dict` to membership disclosure function.
- **Fixed:** Ensured SDV library is installed as a dependency for the diffusion model.

## [2.4.0b] - 2025-01-30
- **Fixed:** Corrected membership disclosure algorithm. **Note: The previous implementation resulted in inflated membership disclosure numbers, which means that if the disclosure value was low then the true value was definitely low.**

## [2.4.0a] - 2025-01-28
- **Added:**
  - Yandex diffusion model `yandex_tabddpm`.
  - Possibility to save selected models, pickle artifacts, and retrieve them.
  - Python and R tutorials for calculating membership disclosure.
  - Dummy generator.
  - Capability to log to a file for testing.
  - Tutorial for Median Hellinger distance.
- **Changed:** Changed workspace naming by including the Process ID.
- **Fixed:** Cleared log handlers before starting pysdg.

## [2.3.0] - 2024-12-02 (**RELEASED - STABLE**)
- **Added:** `restore_col_names` method in `Generator` class to retrieve the encoded dataframe with original column names.

## [2.3.0rc0] - 2024-11-23
- **Added:**
  - Bayesian optimization feature for CTGAN, along with a tutorial.
  - Option to log output to a file.
  - Option to specify the maximum number of cores.
  - Detection of duplicate index entries in the json input file for the Generator.
- **Fixed:** Improved performance for handling erratic values in datasets.
- **Changed:** Replaced `no_obsvs` with `num_rows` and `no_synths` with `num_synths` in `Generator.gen` method.

## [2.2.0b] - 2024-09-26
- **Added:**
  - Standalone function to compute membership disclosure risk.
  - Function to remove unnecessary global variables.
- **Deprecated:** The class `MmbrshpRsk` may be deprecated in upcoming release.
- **Changed:** Improved code readability.

## [2.1.6rc0] - 2024-09-06
- **Added:** Verified availability of the Replica library.

## [2.1.6b] - 2024-08-30
- **Added:** `inspect_data` function to assist json file creator in locating discrepancies.
- **Fixed:** Misinterpretation of high cardinality categorical variables in Replica.

## [2.1.5b] - 2024-08-20
- **Fixed:**
  - Mismatch in shape error in synthcity_ctgan for unbalanced categorical variables.
  - Removed 'synthcity_goggle' generator.
- **Changed:** Replaced "soul" by "real" and "ghost" by "synth" in all Generator attributes.

## [2.1.4b] - 2024-08-20
- **Fixed:** Error loading the .env file for Replica generator.

## [2.1.3b] - 2024-08-16
- **Fixed:**
  - Error that forced all logical columns to equate to True.
  - Incorrect identification of missing values as erratic.

## [2.1.2b] - 2024-08-16
- **Fixed:**
  - Datetime type discrepancies in soul and ghost.
  - Occasional invalid output for categorical variables in Replica.
  - Logical error in previous erratic release.
- **Changed:** Dropped json_type option in Generator.load to enforce identical data types.

## [2.1.1b] - 2024-08-09
- **Added:** Option to delete Replica working folder by setting `sweep_replica_jobs` to True in `get_replica_risk`.

## [2.1.0b] - 2024-08-08
- **Added:**
  - Four more Synthcity generators: "synthcity_nflow", "synthcity_rtvae", "synthcity_gogle", "synthcity_arf".
  - `do_sweep_replica` function to delete Replica working folders.
  - `Generator.sweep_replica` attribute set to True by default.
  - `Generator.replica_ids` attribute to retrieve generated replica jobs.

## [2.0.8b] - 2024-08-06
- **Fixed:** Fixed data type discrepancies between soul and ghosts for Replica.
- **Changed:** Set the default for enforcing json types in Generator.load method to True.

## [2.0.7b] - 2024-08-02
- **Fixed:**
  - Fixed a discrepancy between soul and ghost if a special missing value is defined in the json file and Replica generator is used.
  - Fixed datetime processing.
  - Fixed NaT incompatibility with R.
- **Added:** Added suppress_errors attribute to the Generator class to deal with erratic entries in numeric variables as missing values.
- **Changed:** Suppressed warnings.

## [2.0.6b] - 2024-07-31
- **Fixed:** Fixed error when passing a combination of dataframe and json path to Generator.load method.

## [2.0.5b] - 2024-07-30
- **Fixed:**
  - Fixed Replica data type error in encoded ghosts.
  - Updated R installation documentation.
- **Added:** Added R usage documentation.

## [2.0.4b] - 2024-07-29
- **Fixed:** Fixed Replica data type discrepancy between soul and ghosts.

## [2.0.3b] - 2024-07-29
- **Fixed:** Fixed Replica encoding issue.

## [2.0.2b] - 2024-07-26
- **Added:**
  - Allowed user to input either a path to the csv file or a Pandas dataframe in Generator.load method.
  - Allowed user to input either a path to the json file or a dictionary in Generator.load method.

## [2.0.1b] - 2024-07-24
- **Added:** In Generator.load method, added the option of enforcing user-defined datatype as given in the json to both the soul and its ghosts. The default is to use pandas reading defaults.

## [2.0.0b] - 2024-07-24
- **Added:** Initial release of pysdg v2 forked from v1.1.14b and based on python 3.10.
- **Changed:**
  - Eliminated the naive_read function and incorporated it into Generator.load method.
  - Unify_na in v2 takes place during loading and not unloading.
  - Generator.train method takes a training subset as an option.
