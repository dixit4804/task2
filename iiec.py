#!/usr/bin/python3

print("content-type: text/html")
print()

import cgi
import subprocess
form=cgi.fieldStorage()
cmd="sudo {}".format(name)
x=subprocess.geoutput("cmd")
print(x)