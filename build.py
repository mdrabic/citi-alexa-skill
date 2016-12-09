#!/usr/bin/env python
from subprocess import call
import os

""" Builds a deployment package for AWS Lambda """
if os.path.exists("out"):
    call(["rm", "-r", "out"])

call(["mkdir", "out"])
call(["python", "-m", "zipfile", "-c", "out/lambda-pkg.zip", "venv/lib/python2.7/site-packages/*", "app.py"])
