#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/raphael/gr-misc/python
export GR_CONF_CONTROLPORT_ON=False
export PATH=/home/raphael/gr-misc/build/python:$PATH
export LD_LIBRARY_PATH=/home/raphael/gr-misc/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=/home/raphael/gr-misc/build/swig:$PYTHONPATH
/usr/bin/python2 /home/raphael/gr-misc/python/qa_preamble_detector.py 
