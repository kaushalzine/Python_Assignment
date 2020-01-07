# 2. Design automation script which accept directory name and two file extensions from user.
# Rename all files with first file extension with the second file extenntion.
#  Usage : DirectoryRename.py “Demo” “.txt” “.doc” 
#  
from sys import *;
from os import *;



def directary(path,ext,remove_ext):
	print("path name=",path);
	for folders,subfolder,files in walk(path):
		print("Folder name=",folders);
		for file in files:
		
			a=file.split('.')[-1]
			if remove_ext in a:
				base = path.split(file)[0]
				rename(file, base + ".aln")

def main():
	if len(argv)>4:
		print("Argument incorrect")

	path=argv[1]
	ext=argv[2]
	remove_ext=argv[3]
	directary(path,ext,remove_ext)	


if __name__=="__main__":
	main();