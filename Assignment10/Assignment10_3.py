# 3. Design automation script which accept two directory names. Copy all files from first directory
# into second directory. Second directory should be created at run time.
#  Usage : DirectoryCopy.py “Demo” “Temp”
# Demo is name of directory which is existing and contains files in it. We have to create new
# Directory as Temp and copy all files from Demo to Temp

from sys import *;
from os import *;
import shutil 


def directory(path,path2):

	print("Fist Directary name=",path)
	print("Second --//--",path2)

	for folders,subfolders,files in walk(path):
		shutil.copytree(folders,path2)
		# for files


def main():

	if len(argv)>3:
		print("Invalied Arg.");

	path=argv[1];
	path2=argv[2];
	directory(path,path2)

if __name__=="__main__":
	main()