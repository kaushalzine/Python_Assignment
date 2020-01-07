import psutil
from sys import *
import os ;
import time

def processdisplay(path):

	if not os.path.exists(path):
		os.mkdir(path)
	filename=os.path.join(path,'ProcessDisplay%s.txt'%time.time())


	print("Inside method")
	processlist=[]
	file=open(filename,'w')
	print("Data File print process")
	for proc in psutil.process_iter():

		try:
			
			file.write(str(proc));

		except(Exception):

			pass
	return processlist	


def main():
	print("*"*30)
	
	path=argv[1]
	processdisplay(path)

if __name__=="__main__":
	main()