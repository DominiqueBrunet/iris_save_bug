# iris_save_bug
Illustration of bug in iris.save

Needs iris (https://github.com/SciTools/iris)

Tested on Python 2.7 with Ubuntu 12.04.

Usage:
python iris_save_bug.py

Will read 'input.grib2' and overwrite 'output.grib2'.

Expected output to stdout:

time1 2015-08-02 10:30:00

time2 2015-08-02 10:00:00

AssertionError
