#!/bin/bash
# Integration testing program for the server_usage.py module.
# This will run all the integration tests for this program.
# Will need to run this from the base directory where the module file
#   is located at.

echo ""
echo "Integration test:  server_usage.py"
test/integration/server_usage/get_svr_info.py
test/integration/server_usage/get_svr_mem.py
test/integration/server_usage/get_proc_mem.py
test/integration/server_usage/post_process.py
test/integration/server_usage/run_program.py
test/integration/server_usage/main.py

