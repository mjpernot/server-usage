# Changelog
All notable changes to this project will be documented in this file.

The format is based on "Keep a Changelog".  This project adheres to Semantic Versioning.


## [1.1.0]
- Added ability to connect to MIDB with SSL connections.

### Changed
- post_process: Added check on Mongo connection status.
- Remove non-required \*\*kwargs from the function parameter list.
- config/configuration.py.TEMPLATE:  Added authenication mechanism and SSL connection entries.
- Documentation updates.


## [1.0.2] - 2020-06-25
### Fixed
- main, run_program:  Fixed handling command line arguments.

### Changed
- configuration.py.TEMPLATE:  Changed format of configuration file for Mongo connection.
- Documentation updates.


## [1.0.1] - 2019-05-17
### Fixed
- run_program, post_process:  Fixed problem with mutable default arguments issue.


## [1.0.0] - 2019-03-05
- General Release.


## [0.3.0] - 2018-11-16
- Field release.


## [0.2.0] - 2018-11-14
- Beta initial release.


## [0.1.0] - 2017-10-23
- Alpha initial release.


## [0.0.1] - 2017-10-18
- Pre-alpha initial release.

