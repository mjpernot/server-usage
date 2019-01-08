#!/bin/bash
# Unit testing program for the server_usage.py module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file
#   is located at.

echo ""
echo "Unit test:  help_message"
test/unit/server_usage/help_message.py

echo ""
echo "Unit test:  get_svr_info"
test/unit/server_usage/get_svr_info.py

echo ""
echo "Unit test:  get_svr_mem"
test/unit/server_usage/get_svr_mem.py

echo ""
echo "Unit test:  get_proc_mem"
test/unit/server_usage/get_proc_mem.py

echo ""
echo "Unit test:  post_process"
test/unit/server_usage/post_process.py

echo ""
echo "Unit test:  run_program"
test/unit/server_usage/run_program.py

echo ""
echo "Unit test:  main"
test/unit/server_usage/main.py

