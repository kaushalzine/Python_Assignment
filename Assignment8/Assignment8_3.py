# 3.Design python application which creates two threads as evenlist and oddlist. Both the
# threads accept list of integers as parameter. Evenlist thread add all even elements
# from input list and display the addition. Oddlist thread add all odd elements from input
# list and display the addition.



import threading 

def evenlist(arr):
	for i in range(1,len(arr)):
		if(i%2==0):
			print("Even",i);

def Oddlist(arr):
	for i in range(1,len(arr)):
		if(i%2!=0):
			print("Odd",i);


if __name__ == "__main__": 

	arr=list[1,2,3,4,5,6,7,8,9];
	
	poold=pool();
	maped=map(evenlist(),arr)


	 t1 = threading.Thread(target=evenlist, args=();

	 t2 = threading.Thread(target=Oddlist, args=();
	 t1.start()
	 t2.start()
