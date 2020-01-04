# 3. Write a program which contains one class named as Arithmetic.
# Arithmetic class contains three instance variables as Value1 ,Value2.
# Inside init method initialise all instance variables to 0.
# There are three instance methods inside class as Value2.
# Accept method will accept value of Value1 and Value2 from user.
# Addition() method will perform addition of Value1 ,Value2 and return result.
# Subtraction() method will perform subtraction of Value1 ,Value2 and return result.
# Multiplication() method will perform multiplication of Value1 ,Value2 and return result.
# Division() method will perform division of Value1 ,Value2 and return result.
# After designing the above class call all instance methods by creating multiple objects. 


class Arithmetic:
	

	def __init__(self,no1,no2):
		print("init...")
		self.i=no1
		self.j=no2

	


	def Addition(self):
		Ans=no1+no2;
		print("Addition =",Ans);

	def Subtraction(self):
		Ans=no1-no2;
		print("Sub=",Ans);


	def Multiplication(self):
		Ans=no1*no2;
		print("Division",Ans);
	def Division(self):
		Ans=no1/no2;
		print("Division=",Ans);
	
	

def Accept():
	no1=int(input("Enter Fist num"));
	no2=int(input("Enter Fist num"));
	return no1,no2

no1,no2=Accept()
obj1=Arithmetic(no1,no2)

obj1.Addition()
obj1.Subtraction()
obj1.Multiplication()
obj1.Division()


# output-:
# zine@DESKTOP-BU1PSC0 MINGW64 ~/Desktop/python/Assignment/Assignment6
# $ python Assignment6_3.py
# Enter Fist num10
# Enter Fist num5
# init...
# Addition = 15
# Sub= 5
# Division 50
# Division= 2.0
