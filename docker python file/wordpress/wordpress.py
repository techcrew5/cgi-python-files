#!/usr/bin/python3
import cgi
import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()
wordpressvol = mydata.getvalue("mysqlvol")
WORDPRESS_DB_HOST = mydata.getvalue("WORDPRESS_DB_HOST")
WORDPRESS_DB_USER = mydata.getvalue("WORDPRESS_DB_USER")
WORDPRESS_DB_PASSWORD = mydata.getvalue("WORDPRESS_DB_PASSWORD")
WORDPRESS_DB_NAME = mydata.getvalue("WORDPRESS_DB_NAME")
name = mydata.getvalue("name")
image = mydata.getvalue("image")
version = mydata.getvalue("version")
port = mydata.getvalue("port")
#mysqlos = mydata.getvalue("mysqlos")

cmd1 = "sudo docker volume create {}".format(wordpressvol)
output1 = subprocess.getoutput(cmd1)

cmd2 = "sudo docker run -dit -e WORDPRESS_DB_HOST={} -e WORDPRESS_DB_USER={} -e WORDPRESS_DB_PASSWORD={} -e WORDPRESS_DB_NAME={} -v {}:/var/www/html --name {} -p {}:80 --link {} {}:{}".format(WORDPRESS_DB_HOST,WORDPRESS_DB_USER,WORDPRESS_DB_PASSWORD,WORDPRESS_DB_NAME,wordpressvol,name,port,WORDPRESS_DB_HOST,image,version)
output2 = subprocess.getoutput(cmd2)

print(output2)
