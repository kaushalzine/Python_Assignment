# 2. Write a program which contains one class named as Circle.
# Circle class contains three instance variables as Radius ,Area, Circumference.
# That class contains one class variable as PI which is initialise to 3.14.
# Inside init method initialise all instance variables to 0.0.
# The re a re th ree in s tan ce me thod s in side cla s s a s A c cep t() , Cal cula teA rea() ,
# CalculateCircumference(), Display().
# Accept method will accept value of Radius from user.
# CalculateArea() method will calculate area of circle and store it into instance variable Area.
# CalculateCircumference() method will calculate circumference of circle and store it into instance
# variable Circumference.
# And Display() method will display value of all the instance variables as Radius , Area,
# Circumference.
# After designing the above class call all instance methods by creating multiple objects. 





class circle:
	
	def __init__(self,Radius):
		self.Radius=Radius
		self.Area=0
		self.Circumference=0
		self.pi=3.14
	
	def CalculateArea(self):
		
		
		self.Area=self.pi*Radius*Radius;
		return self.Area
		# print(self.Area)

	def CalculateCircumference(self):
		self.circumference=2*self.pi*Radius
		return self.circumference

	def display(self,a,b):
		print("Give radius circles Area=",a)
		print("Circle Circumference =",b)

	def  Accept() :
		Radiuss=int(input("Enter Radius="));
		return Radiuss


Radius=circle.Accept()
obj1=circle(Radius);


a=obj1.CalculateArea();
b=obj1.CalculateCircumference();
obj1.display(a,b);

Radius=circle.Accept()
obj2=circle(Radius);

a=obj2.CalculateArea();
b=obj2.CalculateCircumference();
obj2.display(a,b);



# output-
# zine@DESKTOP-BU1PSC0 MINGW64 ~/Desktop/python/Assignment/Assignment6
# $ python Assignment6_2.py
# Enter Radius=3
# Give radius circles Area= 28.259999999999998
# Circle Circumference = 18.84
# Enter Radius=4
# Give radius circles Area= 50.24
# Circle Circumference = 25.12
