#!/bin/bash
# Integration test code coverage for server_usage.py module.
# This will run the Python code coverage module against all integration test modules.
# This will show the amount of code that was tested and which lines of code
#   that was skipped during the test.

coverage erase

echo ""
echo "Running integration test modules in conjunction with coverage"
coverage run -a --source=server_usage test/integration/server_usage/get_svr_info.py
coverage run -a --source=server_usage test/integration/server_usage/get_svr_mem.py
coverage run -a --source=server_usage test/integration/server_usage/get_proc_mem.py
coverage run -a --source=server_usage test/integration/server_usage/post_process.py
coverage run -a --source=server_usage test/integration/server_usage/run_program.py
coverage run -a --source=server_usage test/integration/server_usage/main.py

echo ""
echo "Producing code coverage report"
coverage combine
coverage report -m
