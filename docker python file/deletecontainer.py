#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()
deleteos = mydata.getvalue("deleteos")

cmd = "sudo docker rm -f {}".format(deleteos)
output = subprocess.getoutput(cmd)

print(output)
