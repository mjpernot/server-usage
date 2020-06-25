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
  * Save the results to a Mongo database collection.


# Prerequisites:
  * List of Linux packages that need to be installed on the server.
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

  * If connecting to a Mongo replica set, otherwise set to None.
    - repset = "REPLICA_SET_NAME"
    - repset_hosts = "HOST_1:PORT, HOST_2:PORT, ..."
    - db_auth = "AUTHENTICATION_DATABASE"

```
vim configuration.py
chmod 600 configuration.py
```


# Program Help Function:

  The program has a -h (Help option) that will show display an usage message.  The help message will usually consist of a description, usage, arugments to the program, example, notes about the program, and any known bugs not yet fixed.  To run the help command:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
{Python_Project}/server-usage/server_usage.py -h
```


# Testing:

# Unit Testing:

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

### Testing:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}/server-usage
test/unit/server_usage/unit_test_run.sh
```

### Code coverage:
```
cd {Python_Project}/server-usage
test/unit/server_usage/code_coverage.sh
```


# Integration Testing:

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

### Testing:
  * These tests must be run as the root account.
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}/server-usage
test/integration/server_usage/integration_test_run.sh
```

### Code coverage:
```
cd {Python_Project}/server-usage
test/integration/server_usage/code_coverage.sh
```


# Blackbox Testing:

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

### Testing:
  * This test must be run as the root account.
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}/server-usage
test/blackbox/server_usage/blackbox_test.sh
```

