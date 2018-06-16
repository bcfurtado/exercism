#!/bin/sh

echo "Testing gigasecond-test.el"
emacs -nw -batch -l ert -l gigasecond-test.el -f ert-run-tests-batch-and-exit
