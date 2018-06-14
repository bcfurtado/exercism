#!/bin/sh

echo "Testing bob-test.el"
emacs -nw -batch -l ert -l bob-test.el -f ert-run-tests-batch-and-exit
