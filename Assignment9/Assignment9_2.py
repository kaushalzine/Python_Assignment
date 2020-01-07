# 2. Write a program which accept file name from user and open that file and display the contents
# of that file on screen.
# Input : Demo.txt
# Display contents of Demo.txt on console. 



from sys import *;
a=input("Enter File Name=")
file=open(a,'r')
print(file.read())

