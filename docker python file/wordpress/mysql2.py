#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()
mysqlvol = mydata.getvalue("mysqlvol")
MYSQL_ROOT_PASSWORD = mydata.getvalue("MYSQL_ROOT_PASSWORD")
MYSQL_USER = mydata.getvalue("MYSQL_USER")
MYSQL_PASSWORD = mydata.getvalue("MYSQL_PASSWORD")
MYSQL_DATABASE = mydata.getvalue("MYSQL_DATABASE")
name = mydata.getvalue("name")
image = mydata.getvalue("image")
version = mydata.getvalue("version")

#cmd = "sudo docker run -dit --name {} {}:{}".format(name,image,version)
cmd1 = "sudo docker volume create {}".format(mysqlvol)
output1 = subprocess.getoutput(cmd1)

cmd2 = "sudo docker run -dit -e MYSQL_ROOT_PASSWORD={} -e MYSQL_USER={} -e MYSQL_PASSWORD={} -e MYSQL_DATABASE={} -v {}:/var/lib/mysql --name {}  {}:{}".format(MYSQL_ROOT_PASSWORD,MYSQL_USER,MYSQL_PASSWORD,MYSQL_DATABASE,mysqlvol,name,image,version)
output2 = subprocess.getoutput(cmd2)

#output = subprocess.getoutput("cal")
#output = subprocess.getoutput("sudo " + myx)

print(output2)
