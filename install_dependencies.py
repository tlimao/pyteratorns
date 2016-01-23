#!/usr/bin/python
# -*- coding: utf-8 -from os import environ, remove
import subprocess
import sys
import os

get_bash_response = lambda a: subprocess.check_output(["/bin/bash", "-c", a]).decode("utf-8")
run_bash_command = lambda a: subprocess.call(["/bin/bash", "-c", a])
run_command = lambda c: subprocess.call(c, shell=True)

platform = sys.platform
if platform == 'win32':
    print "windows"
else:
    print "linux"

run_command("pip install --upgrade pip virtualenv setuptools")
run_command("pip install Cython==0.21.2")
run_command("pip install kivy")
run_command("git clone https://github.com/kivy/buildozer.git")
os.chdir("buildozer")
run_command("sudo python setup.py install")
os.chdir("..")