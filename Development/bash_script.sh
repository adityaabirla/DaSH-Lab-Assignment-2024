#!/bin/bash
echo "BASH SSCRIPT STARTING"
chmod +x bash_script.sh
python serv.py
echo "server done"
python clie1.py 
echo "clie 1 done"
python clie2.py 
echo "clie 2 done"
python clie3.py 
echo "clie 3 done"