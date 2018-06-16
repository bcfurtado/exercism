#!/bin/sh

echo "Testing difference-of-squares-test.el"
emacs -nw -batch -l ert -l difference-of-squares-test.el -f ert-run-tests-batch-and-exit
