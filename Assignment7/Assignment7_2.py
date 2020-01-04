# 2. Write a program which contains one class named as BankAccount.
# BankAccount class contains two instance variables as Name & Amount.
# That class contains one class variable as ROI which is initialise to 10.5.
# Inside init method initialise all name and amount variables by accepting the values from user.
# There are Four instance methods inside class as Display(), Deposit(), Withdraw(),
# CalculateIntrest().
# Deposit() method will accept the amount from user and add that value in class instance variable
# Amount.
# Withdraw() method will accept amount to be withdrawn from user and subtract that amount
# from class instance variable Amount.
# CalculateIntrest() method calculate the interest based on Amount by considering rate of interest
# which is Class variable as ROI.
# And Display() method will display value of all the instance variables as Name and Amount.
# After designing the above class call all instance methods by creating multiple objects. 



class BankAccount:
	
	def __init__(self,name,value):
		
		self.name=name
		self.Amount=value

	

	def Deposit(self,value):
		self.Amount=self.Amount+value;
		print("Deposit=",self.Amount)	
	def withdra(self,value):
		self.Amount = self.Amount - value;
		print("Withdra=",self.Amount)

	def CalculateIntrest(self):
		ROI = 10.5;
		Ans=(self.Amount*ROI*1)/100
		print("per year Intrest=",Ans)

	def Display(self):
		print("NAme=",self.name)
		print("Amount=",self.Amount)




obj1 = BankAccount("abc",2000);
obj1.Display()
obj1.Deposit(2000)
obj1.withdra(2000)
obj1.CalculateIntrest()


obj1 = BankAccount("xyz",1000);
obj1.Display()
obj1.Deposit(1000)
obj1.withdra(1000)
obj1.CalculateIntrest()


# output-:

# zine@DESKTOP-BU1PSC0 MINGW64 ~/Desktop/python/Assignment/Assignment7
# $ python Assignment7_2.py
# NAme= abc
# Amount= 2000
# Deposit= 4000
# Withdra= 2000
# per year Intrest= 210.0
# NAme= xyz
# Amount= 1000
# Deposit= 2000
# Withdra= 1000
# per year Intrest= 105.0
