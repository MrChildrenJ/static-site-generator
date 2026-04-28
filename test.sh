# use the standard library's "unittest" module to run all the tests (discover) it can find in the "src" directory
# -m: execute mudule
#   python3 -m unittest = import unittest
#                         unittest.__main__()
# -s: start directory
python3 -m unittest discover -s src
