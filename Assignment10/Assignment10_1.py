# 1.Design "automation script which accept directory name and file extension from user. Display all
# files with that extension.
#  Usage : DirectoryFileSearch.py “Demo” “.txt” 

from sys import *;
from os import *;

def directory(path,ext):
	
	print(path)

	for folders,subfolder,files in walk(path):
		print("Folder Name-",folders)
		for file in files:
			a=file.split('.')[-1]
			if ext==a:
				print("File Name-",file)
			
			
def main():
	print("PLZ Check help Option -h or -H")
	if len(argv)>3:
		print("Invalied argument");
	if argv[1]=='-h' or argv[1]=="-H":
		print("Help")
		print("python comand ,Filename, Extention")

	path=argv[1]	
	ext=argv[2]
	directory(path,ext)



if __name__=="__main__":
	main();



# output-:
# zine@DESKTOP-BU1PSC0 MINGW64 ~/Desktop/python/Assignment/Assignment10
# $ python Assignment10_1.py a py
# a

# Folder Name- a
# File Name- asd.py
# Folder Name- a\aa

