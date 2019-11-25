# 1.Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub()
# for subtraction, Mult() for multiplication and Div() for division. All functions accepts two
# parameters as number and perform the operation. Write on python program which call all the
# functions from Arithmetic module by accepting the parameters from user. 



from Arithmetic import *;

print("Enter Two Number-:");
num1=int(input());
num2=int(input());

Add(num1,num2);
Sub(num1,num2);
Mult(num1,num2);
Div(num1,num2);


# Output-:

# zine@DESKTOP-BU1PSC0 MINGW64 ~/Desktop/python/Assignment/Assignment2
# $ python Assignment2_1.py
# Enter Two Number-:
# 20
# 10
# Two Num Addition = 30
# Two Num Subtraction = 10
# Two Num Multiplication = 200
# Two Num Division = 2.0
