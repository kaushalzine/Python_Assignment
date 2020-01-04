# 1.Design python application which creates two thread named as even and odd. Even
# thread will display first 10 even numbers and odd thread will display first 10 odd
# numbers. 


import threading 

def even(no):
	for i in range(1,no):
		if(i%2==0):
			print("Even",i);

def Odd(no):
	for i in range(1,no):
		if(i%2!=0):
			print("Odd",i);



if __name__ == "__main__": 
	 t1 = threading.Thread(target=even, args=(10,));

	 t2 = threading.Thread(target=Odd, args=(10,));
	 t1.start()
	 t2.start()



# output-:

# zine@DESKTOP-BU1PSC0 MINGW64 ~/Desktop/python/Assignment/Assignment8
# $ python Assignment8_1.py
# Even 2
# Even 4
# Even 6
# Even 8
# Odd 1
# Odd 3
# Odd 5
# Odd 7
# Odd 9
