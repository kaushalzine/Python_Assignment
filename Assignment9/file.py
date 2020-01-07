from sys import *;
from shutil import copyfile

print("Hi")

file=open("a.txt",'r')
print(file.read())


file=open("a.txt",'w')
file.write(" the take ")

file=open("a.txt",'r')
print(file.read())

copyfile('Demo.txt','a.txt')