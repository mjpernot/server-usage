#!/bin/bash
# Unit testing program for the server_usage.py module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file
#   is located at.

echo ""
echo "Unit test:  server_usage.py"
/usr/bin/python test/unit/server_usage/help_message.py
/usr/bin/python test/unit/server_usage/get_svr_info.py
/usr/bin/python test/unit/server_usage/get_svr_mem.py
/usr/bin/python test/unit/server_usage/get_proc_mem.py
/usr/bin/python test/unit/server_usage/post_process.py
/usr/bin/python test/unit/server_usage/run_program.py
/usr/bin/python test/unit/server_usage/main.py

