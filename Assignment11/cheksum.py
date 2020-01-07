from sys import *;
import os
import hashlib
import time

def DeleteFiles(dirt1):
	results=list(filter(lambda x:len(x)>1,dirt1.values()))

	icnt=0;
	if len(results)>0:
		for result in results:
			for subresult in result:
				icnt+=1
				if icnt >=2:
					os.remove(subresult)
			icnt=0;

	else:
		print("No duplicate files found.")



def hashfile(path,blocksize=1024):
	afile=open(path,'rb')
	hasher=hashlib.md5()
	buf=afile.read(blocksize)

	while len(buf)>0:
		hasher.update(buf)
		buf=afile.read(blocksize)
	afile.close()

	return hasher.hexdigest()


def findDup(path):
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


def printResults(dict1):
	results=list(filter(lambda x:len(x)>1,dict1.values()))

	if len(results)>0:
		print("Duplicates Founds:")
		print("The Following files are duplicate")
		for result in results:
			for subresult in result:
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
		startTime=time.time()
		arr=findDup(argv[1])
		printResults(arr)
		DeleteFiles(arr)
		endtime=time.time()

		print('Took %s seconds to evaluate.'%(endtime-startTime))

	except ValueError:
		print("Error:Invalid datatype of input")

	except Exception as E:
		print("Error : Invalid input",E)

if __name__=="__main__":
	main()





# output-:

# zine@DESKTOP-BU1PSC0 MINGW64 ~/Desktop/python/Assignment/Assignment11
# $ python cheksum.py data
# @@@@@@@@@@
# Appcation name:cheksum.py
# Current folder is :C:\Users\zine\Desktop\python\Assignment\Assignment11\data
# No duplicate files found
# No duplicate files found.
# Took 0.0 seconds to evaluate.
