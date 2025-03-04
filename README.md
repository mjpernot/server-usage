# Python project to monitor the memory usage on a Linux server.
# Classification (U)

# Description:
  Used to monitor and record memory usage on a Linux server.  This can include setting a memory threshold on which processes to monitor and save the results to a Mongo database for further analysis.  The memory usage will be on a per process basis.


###  This README file is broken down into the following sections:
  * Features
  * Prerequisites
  * Installation
  * Configuration
  * Program Help Function
  * Testing
    - Unit
    - Integration
    - Blackbox


# Features:
  * Capture and display any processes that are using memory over the memory threshold setting.


# Prerequisites:

  * List of Linux packages that need to be installed on the server.
    - python3-pip
    - python3-devel
    - gcc


# Installation:

Install the project using git.

```
git clone git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/server-usage.git
```

Install/upgrade system modules.

NOTE: Install as the user that will run the program.

```
python -m pip install --user -r requirements3.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
```


Install supporting local classes and libraries.

```
python -m pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
```


# Configuration:

Make the appropriate changes to the environment.
  * memory_threshold is amount of memory required before the process is recorded.  Value is in Megabytes.
    - memory_threshold = 100

```
cp config/configuration.py.TEMPLATE config/configuration.py
vim config/configuration.py
```


# Program Help Function:

  The program has a -h (Help option) that will show display an usage message.  The help message will usually consist of a description, usage, arugments to the program, example, notes about the program, and any known bugs not yet fixed.  To run the help command:

```
server_usage.py -h
```


# Testing:

# Unit Testing:

### Installation:

Install the project using the procedures in the Installation section.

### Testing:

```
test/unit/server_usage/unit_test_run.sh
test/unit/server_usage/code_coverage.sh
```


# Integration Testing:

### Installation:

Install the project using the procedures in the Installation section.

### Configuration:

Make the appropriate changes to the environment.
  * memory_threshold is amount of memory required before the process is recorded.  Value is in Megabytes.
    - memory_threshold = 100

```
cp config/configuration.py.TEMPLATE test/integration/server_usage/config/configuration.py
vim test/integration/server_usage/config/configuration.py
```

### Testing:
  * These tests must be run as the root account.

```
test/integration/server_usage/integration_test_run.sh
test/integration/server_usage/code_coverage.sh
```


# Blackbox Testing:

### Installation:

Install the project using the procedures in the Installation section.

### Configuration:

Make the appropriate changes to the environment.
  * memory_threshold is amount of memory required before the process is recorded.  Value is in Megabytes.
    - memory_threshold = 100

```
cp config/configuration.py.TEMPLATE test/blackbox/server_usage/config/configuration.py
vim test/blackbox/server_usage/config/configuration.py
```

### Testing:
  * This test must be run as the root account.

```
test/blackbox/server_usage/blackbox_test.sh
```

