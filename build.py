#!/usr/bin/env python
from subprocess import call
from subprocess import check_call
from glob import glob
import os
import datetime

""" Builds a deployment package for AWS Lambda """
if os.path.exists("out"):
    call(["rm", "-r", "out"])

call(["mkdir", "out"])

timestamp = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
check_call(["python", "-m", "zipfile", "-c", "out/lambda-pkg-" + timestamp + ".zip",] +
           glob("venv/lib/python2.7/site-packages/*") +
           ["app.py", "citi.py", "response_util.py"])
