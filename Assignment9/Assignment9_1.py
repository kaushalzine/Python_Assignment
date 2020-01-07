# 1.Write a program which accepts file name from user and check whether that file exists in
# current directory or not.
# Input : Demo.txt
# Check whether Demo.txt exists or not.


from sys import *;
from os import *;


filename=argv[1]
print(filename)
a=input("File name=");
for Folder,sub,files in walk(filename):
	for file in files:
		if a==file:
			print("file exist")
		else :
			print("File not exist") 

# output-
# zine@DESKTOP-BU1PSC0 MINGW64 ~/Desktop/python/Assignment/Assignment9
# $ python Assignment9_1.py data
# data
# File name=a.txt
# file exist
# File not exist
