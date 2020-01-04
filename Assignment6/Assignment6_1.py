# 1.Write a program which contains one class named as Demo.
# Demo class contains two instance variables as no1 ,no2.
# That class contains one class variable as Value.
# There are two instance methods of class as Fun and Gun which displays values of instance
# variables.
# Initialise instance variable in init method by accepting the values from user.

# After creating the class create the two objects of Demo class as
# Obj1 = Demo(11,21)
# Obj2 = Demo(51,101)
# Now call the instance methods as
# Obj1.Fun()
# Obj2.Fun()
# Obj1.Gun()
# Obj2.Gun() 



class Demo:

	def __init__(self,no1,no2):
		print("init...")
		self.i=no1
		self.j=no2

	def fun(self):
		print(self.i,self.j)
			
	def gun(self):

		print(self.i,self.j)

Obj1 = Demo(11,21)
Obj1.fun()
Obj1.gun()

Obj2 = Demo(51,101)
Obj2.fun()
Obj2.gun() 



# output-:
# zine@DESKTOP-BU1PSC0 MINGW64 ~/Desktop/python/Assignment/Assignment6
# $ python Assignment6_1.py
# init...
# 11 21
# 11 21
# init...
# 51 101
# 51 101
