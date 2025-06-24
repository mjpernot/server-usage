#!/bin/bash
# Blackbox testing program for the server_usage.py program.

# Setup the test files for all blackbox tests.
BASE_PATH=$PWD

echo "Server_usage Blackbox Testing"
echo "Scenario 1:  Write output to standard out"
./server_usage.py -c configuration -d test/blackbox/server_usage/config > test/blackbox/server_usage/out/test.out

test/blackbox/server_usage/blackbox_test.py stdout test/blackbox/server_usage/out/test.out

echo "Scenario 2:  Suppression of output to standard out"
if [ "$(./server_usage.py -c configuration -d test/blackbox/server_usage/config -n | wc -l)" -eq 0 ] ; then
    printf "\n\tTest Successful\n"
else
    printf "\n\tTest Failure\n"
fi

echo "Scenario 3:  Write output to standard out in JSON format"
./server_usage.py -c configuration -d test/blackbox/server_usage/config > test/blackbox/server_usage/out/test.out

test/blackbox/server_usage/blackbox_test.py json test/blackbox/server_usage/out/test.out

echo "Scenario 4:  Write output to standard out in formatted report"
if [ "$(./server_usage.py -c configuration -d test/blackbox/server_usage/config | wc -l)" -eq 1 ] ; then
    printf "\n\tTest Successful\n"
else
    printf "\n\tTest Failure\n"
fi

