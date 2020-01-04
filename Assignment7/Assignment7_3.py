# 3. Write a program which contains one class named as Numbers.
# Arithmetic class contains one instance variables as Value.
# Inside init method initialise that instance variables to the value which is accepted from user.
# There are four instance methods inside class as ChkPrime(), ChkPerfect(), SumFactors(),
# Factors().
# ChkPrime() method will returns true if number is prime otherwise return false.
# ChkPerfect() method will returns true if number is perfect otherwise return false.
# Factors() method will display all factors of instance variable.
# SumFactors() method will return addition of all factors. Use this method in any another method
# as a helper method if required.
# After designing the above class call all instance methods by creating multiple objects.



class Numbers:
	
	def __init__(self,value):
		
		self.value=value
		

	def ChkPrime(self):
		if self.value > 1:  
		   for i in range(2,self.value):  
		       if (self.value % i) == 0:  
		           print(self.value,"is not a prime number")  
		           
		           break  
		   else:  
		       print(self.value,"is a prime number")  
		         
		else:  
		   print(self.value,"is not a prime number")  






	def ChkPerfect(self):

		Sum = 0
		for i in range(1, self.value):
		    if(self.value % i == 0):
		        Sum = Sum + i
		if (Sum == self.value):
		    print(self.value," is a Perfect Number")
		else:
		    print(self.value,"is not a Perfect Number")








	# def SumFactors(self):

	# def Factors(self):


obj1=Numbers(6)
obj1.ChkPrime();
obj1.ChkPerfect();

obj1=Numbers(9)
obj1.ChkPrime();
obj1.ChkPerfect();



# output-:

# zine@DESKTOP-BU1PSC0 MINGW64 ~/Desktop/python/Assignment/Assignment7
# $ python Assignment7_3.py
# 6 is not a prime number
# 6  is a Perfect Number
# 9 is not a prime number
# 9 is not a Perfect Number