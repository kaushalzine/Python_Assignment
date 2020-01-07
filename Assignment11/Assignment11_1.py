from sys import *;
import os
import hashlib
import time


def hashfile(path,blocksize=1024):
	fd=open(path,'rb')
	hasher=hashlib.md5()
	buf=fd.read(blocksize)

	while len(buf)>0:
		hasher.update(buf)
		buf=fd.read(blocksize)
	fd.close()

	return hasher.hexdigest()


def FindDuplicate(path):
	flag=os.path.isabs(path)

	if flag==False:
		path=os.path.abspath(path)
	exists=os.path.isdir(path)
	dups={}

	if exists:
		for dirName,subdirs,fileList in os.walk(path):
			print("Current folder is :"+dirName)
			for filen in fileList:
				path=os.path.join(dirName,filen)
				file_hash=hashfile(path)

				if file_hash in dups:
					dups[file_hash].append(path)
				else:
					dups[file_hash]=[path]
		return dups

	else:
		print("Invalid path")

def printDuplicate(dict1):
	results=list(filter(lambda x:len(x)>1,dict1.values()))

	if len(results)>0:
		print("Duplicates Founds:")
		print("The Following files are duplicate")
		icnt=0;
		for result in results:
			for subresult in result:
				icnt+=1
				if icnt>=2:
					print('\t\t%s'%subresult)
	else:
		print("No duplicate files found")



def main():
	print("@"*10);
	print("Appcation name:"+argv[0])

	if(len(argv)!=2):
		print("Error:Invalid number of Argument")
		exit()

	if(argv[1]=="-h") or(argv[1]=="-H"):
		print("This script is used to traverse specific directory and delete duplicate files ")
		esit()

	if(argv[1]=="-u") or(argv[1]=="-U"):
		print("Usage: ApplicationName AbsolutePath_of_Directory extention  ")
		esit()
	try:
		arr={}

		arr=FindDuplicate(argv[1])
		printDuplicate(arr)

	except Exception as E:
		print("Error to : Invalid input",E)



if __name__=="__main__":
	main()




# output-:

# zine@DESKTOP-BU1PSC0 MINGW64 ~/Desktop/python/Assignment/Assignment11
# $ python Assignment11_1.py data
# @@@@@@@@@@
# Appcation name:Assignment11_1.py
# Current folder is :C:\Users\zine\Desktop\python\Assignment\Assignment11\data
# Duplicates Founds:
# The Following files are duplicate
#                 C:\Users\zine\Desktop\python\Assignment\Assignment11\data\a.txt
#                 C:\Users\zine\Desktop\python\Assignment\Assignment11\data\a3.txt
#                 C:\Users\zine\Desktop\python\Assignment\Assignment11\data\a5.txt

