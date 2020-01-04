# 1.Write a program which contains one class named as BookStore.
# BookStore class contains two instance variables as Name ,Author.
# That class contains one class variable as NoOfBooks which is initialise to 0.
# There is one instance methods of class as Display which displays name , Author and number of
# books.
# Initialise instance variable in init method by accepting the values from user as name and author.
# Inside init method increment value of NoOfBooks by one.

# After creating the class create the two objects of BookStore class as
# Obj1 = BookStore(“Linux System Programming”, “Robert Love”)
# Obj1.Display() # Linux System Programming by Robert Love. No of books : 1

# Obj2 = BookStore(“C Programming”, “Dennis Ritchie”)
# Obj2.Display() # C Programming by Dennis Ritchie. No of books : 2 



class BookStore:

	def __init__(self,name,Author):
		
		self.NoOfBooks=0
		self.name=name
		self.Author=Author


	def Display(self,a):
		
		a=a+1
		print("No of Book",a)
		print("Book Name",self.name)
		print("by",self.Author)
		return a;


Obj1 = BookStore("Linux System Programming", "Robert Love")
a=Obj1.Display(0)

Obj2 = BookStore("C Programming", "Dennis Ritchie")
Obj2.Display(a)

# output-:
# zine@DESKTOP-BU1PSC0 MINGW64 ~/Desktop/python/Assignment/Assignment7
# $ python Assignment7_1.py
# No of Book 1
# Book Name Linux System Programming
# by Robert Love
# No of Book 2
# Book Name C Programming
# by Dennis Ritchie

