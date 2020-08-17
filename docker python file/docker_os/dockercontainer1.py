#!/usr/bin/python3
import cgi
import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()
vol = mydata.getvalue("vol")
name = mydata.getvalue("name")
image = mydata.getvalue("image")
version = mydata.getvalue("version")
port = mydata.getvalue("port")
defaultport = mydata.getvalue("defaultport")
networkname = mydata.getvalue("networkname")
mount = mydata.getvalue("mount")

cmd3 = "sudo docker network create --driver bridge {}".format(networkname)
output3 = subprocess.getoutput(cmd3)

cmd1 = "sudo docker volume create {}".format(vol)
output1 = subprocess.getoutput(cmd1)

cmd2 = "sudo docker run -dit -v {0}:{7} --name {1} --network {6} -p {2}:{3} {4}:{5}".format(vol,name,port,defaultport,image,version,networkname,mount)
output2 = subprocess.getoutput(cmd2)

print(output2)
