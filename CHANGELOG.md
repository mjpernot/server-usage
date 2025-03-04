# Changelog
All notable changes to this project will be documented in this file.

The format is based on "Keep a Changelog".  This project adheres to Semantic Versioning.


## [2.0.0] - 2025-03-04
Breaking changes

- Removed support for Python 2.7.
- Removed mongo insert option.
- Updated python-lib==4.0.0

### Changed
- Converted strings to f-strings.
- Documentation changes.


## [1.2.6] - 2024-11-19
- Updated python-lib to v3.0.8
- Updated mongo-lib to v4.3.4

### Fixed
- Set chardet==3.0.4 for Python 3.


## [1.2.5] - 2024-11-11
- Updated chardet==4.0.0 for Python 3
- Updated distro==1.9.0 for Python 3
- Updated psutil==5.9.4 for Python 3
- Updated mongo-lib to v4.3.3
- Update python-lib to v3.0.7

### Deprecated
- Support for Python 2.7

## [1.2.4] - 2024-09-27
- Updated pymongo==4.1.1 for Python 3.6
- Updated simplejson=3.13.2 for Python 3
- Updated mongo-lib to v4.3.2
- Update python-lib to v3.0.5


## [1.2.3] - 2024-09-10

### Changed
- main: Removed parsing from gen_class.ArgParser call and called arg_parse2 as part of "if" statement.


## [1.2.2] - 2024-04-23
- Updated mongo-lib to v4.3.0
- Added TLS capability for Mongo
- Set pymongo to 3.12.3 for Python 2 and Python 3.

### Changed
- Set pymongo to 3.12.3 for Python 2 and Python 3.
- config/configuration.py.TEMPLATE: Added TLS entries.
- Documentation updates.


## [1.2.1] - 2024-03-04
- Updated to work in Red Hat 8
- Updated mongo-lib to v4.2.9
- Updated python-lib to v3.0.3

### Changed
- Set simplejson to 3.12.0 for Python 3.
- Set chardet to 3.0.4 for Python 2.
- Documentation updates.


## [1.2.0] - 2023-10-17
- Replaced the arg_parser code with gen_class.ArgParser code.
- Upgraded python-lib to v2.10.1

### Changed
- main, run_program, post_process: Replaced the arg_parser code with gen_class.ArgParser code.
- main, run_program: Removed gen_libs.get_inst call.
- Documentation updates.


## [1.1.1] - 2022-12-01
- Updated to work in Python 3 too
- Upgraded python-lib to v2.9.4
- Upgraded mongo-lib to v4.2.2
 
### Changed
- Converted imports to use Python 2.7 or Python 3.


## [1.1.0] - 2022-05-13
- Added ability to connect to Mongo with SSL connections.
- Upgrade mongo-lib to v4.2.1

### Changed
- post_process: Added check on Mongo connection status.
- Remove non-required \*\*kwargs from the function parameter list.
- config/configuration.py.TEMPLATE:  Added authenication mechanism and SSL connection entries and removed use_arg and use_uri entries.
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

