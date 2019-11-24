# 3. Write a program which contains one function named as Add() which accepts two numbers
# from user and return addition of that two numbers.
# Input : 11 5 Output : 16 


def Add(num1,num2):
	result=num1+num2;
	return result;


num1=int(input());
num2=int(input());
result=Add(num1,num2)
print("Addition of two num=",result);



# Output -:

# zine@DESKTOP-BU1PSC0 MINGW64 ~/Desktop/python/Ass1
# $ python add.py
# 11
# 5
# Addition of two num= 16

