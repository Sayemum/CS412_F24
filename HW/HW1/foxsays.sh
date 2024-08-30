#!/bin/bash

source $HOME/dev/python_venvs/cs412f24/bin/activate

python cs412_fox_says_dict.py < foxsays_t1_in.txt > foxsays_t1_out.txt

diff foxsays_t1_exp.txt foxsays_t1_out.txt > /dev/null 2>&1
DIFFRC=$?
if [ ${DIFFRC} -eq 0 ]
then
    echo Success
else
    echo Test did not succeed
fi

exit 0