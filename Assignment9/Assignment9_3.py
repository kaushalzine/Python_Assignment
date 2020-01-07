# 3.Write a program which accept file name from user and create new file named as Demo.txt and
# copy all contents from existing file into new file. Accept file name through command line
# arguments.
# Input : ABC.txt
# Create new file as Demo.txt and copy contents of ABC.txt in Demo.txt 

from sys import * ;
from shutil import copyfile

def main():

	if argv[1]=='-h':
		print("...........")
		print(" File_Comand [File Name],[File Name]")
	if len(argv)>2:
		a=argv[1]
		b=argv[2]

		copyfile(a,b)
	else:
		print("Checking Argument")	

if __name__ == '__main__':
	main()




# output-:
# zine@DESKTOP-BU1PSC0 MINGW64 ~/Desktop/python/Assignment/Assignment9
# $ python Assignment9_3.py Demo.txt fileuser.txt

