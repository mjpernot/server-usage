# Python project to monitor the memory usage on a Linux server.
# Classification (U)

# Description:
  This program is used to monitor and record memory usage on a Linux server.  This can include setting a memory threshold on which processes to monitor and
  save the results to a Mongo database for further analysis.  The memory usage will be on a per process basis.


###  This README file is broken down into the following sections:
  * Features
  * Prerequisites
  * Installation
  * Configuration
  * Program Description
  * Program Help Function
  * Help Message
  * Testing
    - Unit
    - Integration
    - Blackbox


# Features:
  * Capture and display any processes that are using memory over the memory threshold setting.
  * Save the results to a Mongo database collection.


# Prerequisites:
  * List of Linux packages that need to be installed on the server.
    - python-libs
    - python-devel
    - git
    - python-pip

  * Local class/library dependencies within the program structure. 
    - lib/gen_class
    - lib/arg_parser
    - lib/gen_libs
    - mongo_lib/mongo_libs


# Installation:

Install the project using git.
  * Replace **{Python_Project}** with the baseline path of the python program.

```
umask 022
cd {Python_Project}
git clone git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/server-usage.git
```

Install/upgrade system modules.

```
cd server-usage
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting local classes and libraries.

```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-mongo-lib.txt --target mongo_lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-python-lib.txt --target mongo_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

# Configuration:

Create configuration file.

```
cd config
cp configuration.py.TEMPLATE configuration.py
```

Make the appropriate changes to the environment.
  * memory_threshold is amount of memory required before the process is recorded.  Value is in Megabytes.
    - memory_threshold = 100

  * Make the appropriate changes to connect to a Mongo database.  Only required if saving the results to a Mongo database.
    - user = "USER_NAME"
    - passwd = "USER_PASSWORD"
    - host = "HOST_IP"
    - name = "HOSTNAME"
    - db_auth = "AUTHENTICATION_DATABASE"

  * If connecting to a Mongo replica set, otherwise set to None.
    - repset = "REPLICA_SET_NAME"
    - repset_hosts = "HOST_1:PORT, HOST_2:PORT, ..."

```
vim configuration.py
chmod 600 configuration.py
```


# Program Descriptions:
### Program: server_usage.py
##### Description: Monitor the memory usage for processes on a Linux server.


# Program Help Function:

  The program has a -h (Help option) that will show display an usage message.  The help message will usually consist of a description, usage, arugments to the program, example, notes about the program, and any known bugs not yet fixed.  To run the help command:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
{Python_Project}/server-usage/server_usage.py -h
```


# Help Message:
  Below is the help message for the program.  Recommend running the -h option on the command line to see the latest help message.

    Program:  server_usage.py

    Description:  Monitor the memory usage for processes on a Linux server.

    Usage:
        server_usage.py -c file -d path [-n | -m | -f] [-v | -h]

    Arguments:
        -c configuration => Configuration file.  Required argument.
        -d path => Directory path for "-c" option.  Required argument.
        -f => Format the output to standard out.
        -n => Do not print results to standard out.
        -m => Save results to Mongo database.
        -v => Display version of this program.
        -h => Help and usage message.

        NOTE 1:  -v and -h overrides all other options.

    Notes:
        Configuration file format (configuration.py).  The Mongo database
        section is only required if saving the results to the database.

            # Is amount of memory required before the process is recorded.
            # Value is in Megabytes.
            memory_threshold = 100

            # Mongo database section.
            # User connection information.
            user = "USER_NAME"
            passwd = "USER_PASSWORD"

            # Database host information.
            host = "HOST_IP"
            name = "HOSTNAME"

            # Database to authentication to.
            db_auth = "AUTHENTICATION_DATABASE"

            # Replica Set Mongo configuration settings.
            # Replica set name.  Set to None if not connectin to a replica set.
            repset = "REPLICA_SET_NAME"

            # Replica host listing.  List of mongo databases in replica set.
            # Set to None if not connecting to a Mongo replica set.
            repset_hosts = "HOST1:PORT, HOST2:PORT, [...]"

            # Database and Collection names
            db = "sysmon"
            coll = "mem_usage"

    Example:
        server_usage.py -c configuration -d config


# Testing:

# Unit Testing:

### Description: Testing consists of unit testing for the functions in the server_usage.py program.

### Installation:

Install the project using git.
  * Replace **{Python_Project}** with the baseline path of the python program.
  * Replace **{Branch_Name}** with the name of the Git branch being tested.  See Git Merge Request.

```
umask 022
cd {Python_Project}
git clone --branch {Branch_Name} git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/server-usage.git
```

Install/upgrade system modules.

```
cd server-usage
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting local classes and libraries.

```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-mongo-lib.txt --target mongo_lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-python-lib.txt --target mongo_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

# Unit test runs for server_usage.py:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}/server-usage
```

### Unit:  help_message
```
test/unit/server_usage/help_message.py
```

### Unit:  get_svr_info
```
test/unit/server_usage/get_svr_info.py
```

### Unit:  get_svr_mem
```
test/unit/server_usage/get_svr_mem.py
```

### Unit:  get_proc_mem
```
test/unit/server_usage/get_proc_mem.py
```

### Unit:  post_process
```
test/unit/server_usage/post_process.py
```

### Unit:  run_program
```
test/unit/server_usage/run_program.py
```

### Unit:  main
```
test/unit/server_usage/main.py
```

### All unit testing
```
test/unit/server_usage/unit_test_run.sh
```

### Code coverage program
```
test/unit/server_usage/code_coverage.sh
```


# Integration Testing:

### Description: Testing consists of integration testing of functions in the server_usage.py program.

### Installation:

Install the project using git.
  * Replace **{Python_Project}** with the baseline path of the python program.
  * Replace **{Branch_Name}** with the name of the Git branch being tested.  See Git Merge Request.

```
umask 022
cd {Python_Project}
git clone --branch {Branch_Name} git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/server-usage.git
```

Install/upgrade system modules.

```
cd server-usage
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting local classes and libraries.

```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-mongo-lib.txt --target mongo_lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-python-lib.txt --target mongo_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

### Configuration:

Create configuration file.

```
cd test/integration/server_usage/config
cp ../../../../config/configuration.py.TEMPLATE configuration.py
```

Make the appropriate changes to the environment.
  * memory_threshold is amount of memory required before the process is recorded.  Value is in Megabytes.
    - memory_threshold = 100

  * Make the appropriate changes to connect to a Mongo database.
    - user = "USER_NAME"
    - passwd = "USER_PASSWORD"
    - host = "HOST_IP"
    - name = "HOSTNAME"
    - db = "sysmon" --> Change to "sysmon_server_usage"

  * If connecting to a Mongo replica set, otherwise set to None.
    - db_auth = "AUTHENTICATION_DATABASE"
    - repset = "REPLICA_SET_NAME"
    - repset_hosts = "HOST_1:PORT, HOST_2:PORT, ..."

```
vim configuration.py
chmod 600 configuration.py
```

# Integration test runs for server_usage.py:
  * These tests must be run as the root account.
  * Replace **{Python_Project}** with the baseline path of the python program.

```
sudo bash
cd {Python_Project}/server-usage
```

### Integration:  get_svr_info
```
test/integration/server_usage/get_svr_info.py
```

### Integration:  get_svr_mem
```
test/integration/server_usage/get_svr_mem.py
```

### Integration:  get_proc_mem
```
test/integration/server_usage/get_proc_mem.py
```

### Integration:  post_process
```
test/integration/server_usage/post_process.py
```

### Integration:  run_program
```
test/integration/server_usage/run_program.py
```

### Integration:  main
```
test/integration/server_usage/main.py
```

### All integration testing
```
test/integration/server_usage/integration_test_run.sh
```

### Code coverage program
```
test/integration/server_usage/code_coverage.sh
```


# Blackbox Testing:

### Description: Testing consists of blackbox testing of the server_usage.py program.

### Installation:

Install the project using git.
  * Replace **{Python_Project}** with the baseline path of the python program.
  * Replace **{Branch_Name}** with the name of the Git branch being tested.  See Git Merge Request.

```
umask 022
cd {Python_Project}
git clone --branch {Branch_Name} git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/server-usage.git
```

Install/upgrade system modules.

```
cd server-usage
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting local classes and libraries.

```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-mongo-lib.txt --target mongo_lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-python-lib.txt --target mongo_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

### Configuration:

Create configuration file.

```
cd test/blackbox/server_usage/config
cp ../../../../config/configuration.py.TEMPLATE configuration.py
```

Make the appropriate changes to the environment.
  * memory_threshold is amount of memory required before the process is recorded.  Value is in Megabytes.
    - memory_threshold = 100

  * Make the appropriate changes to connect to a Mongo database.  Only required if saving the results to a Mongo database.
    - user = "USER_NAME"
    - passwd = "USER_PASSWORD"
    - host = "HOST_IP"
    - name = "HOSTNAME"
    - db = "sysmon" --> Change to "sysmon_server_usage"

  * If connecting to a Mongo replica set, otherwise set to None.
    - repset = "REPLICA_SET_NAME"
    - repset_hosts = "HOST_1:PORT, HOST_2:PORT, ..."
    - db_auth = "AUTHENTICATION_DATABASE"

```
vim configuration.py
chmod 600 configuration.py
```

# Blackbox test run for server_usage.py:
  * This test must be run as the root account.
  * Replace **{Python_Project}** with the baseline path of the python program.

```
sudo bash
cd {Python_Project}/server-usage
test/blackbox/server_usage/blackbox_test.sh
```

