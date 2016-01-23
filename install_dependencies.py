#!/usr/bin/python
# -*- coding: utf-8 -from os import environ, remove
import subprocess
import sys
import os
import urllib2

get_bash_response = lambda a: subprocess.check_output(["/bin/bash", "-c", a]).decode("utf-8")
run_bash_command = lambda a: subprocess.call(["/bin/bash", "-c", a])
run_command = lambda c: subprocess.call(c, shell=True)

def download(link, file):
    url = urllib2.urlopen(link)
    localFile = open(file, 'w')
    localFile.write(url.read())
    localFile.close()


download('https://bootstrap.pypa.io/get-pip.py', 'distribute_setup.py')
run_command("python distribute_setup.py")
download('https://bootstrap.pypa.io/get-pip.py', 'get-pip.py')
run_command("python get-pip.py")
os.remove("distribute_setup.py")
os.remove("get-pip.py")
run_command("pip install --upgrade pip wheel setuptools")


platform = sys.platform
if platform == 'win32':
    print "windows"
    run_command("pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew kivy.deps.gstreamer --extra-index-url https://kivy.org/downloads/packages/simple/")

else:
    print "linux"
    run_command("git clone https://github.com/kivy/buildozer.git")
    os.chdir("buildozer")
    run_command("sudo python setup.py install")
    run_command("PAUSE")
    os.chdir("..")

run_command("pip install Cython==0.21.2")
run_command("pip install kivy")