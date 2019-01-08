#!/bin/bash
# Integration testing program for the server_usage.py module.
# This will run all the integration tests for this program.
# Will need to run this from the base directory where the module file
#   is located at.

echo ""
echo "Integration test:  get_svr_info"
test/integration/server_usage/get_svr_info.py

echo ""
echo "Integration test:  get_svr_mem"
test/integration/server_usage/get_svr_mem.py

echo ""
echo "Integration test:  get_proc_mem"
test/integration/server_usage/get_proc_mem.py

echo ""
echo "Integration test:  post_process"
test/integration/server_usage/post_process.py

echo ""
echo "Integration test:  run_program"
test/integration/server_usage/run_program.py

echo ""
echo "Integration test:  main"
test/integration/server_usage/main.py

