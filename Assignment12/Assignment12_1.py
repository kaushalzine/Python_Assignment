import psutil


def displayprocess():
	print("inside method")
	processlist=[]
	file=open('process.txt','w')
	print("Data File print process")
	for proc in psutil.process_iter():

		try:
			
			file.write(str(proc));

		except(Exception):

			pass
	return processlist	


def main():
	print("*"*30)
	list=displayprocess()
	
	for proc in list:
		print(proc)

if __name__=="__main__":
	main()