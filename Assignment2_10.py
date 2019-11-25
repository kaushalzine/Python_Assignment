# 10. Write a program which accept number from user and return addition of digits in that number.
# Input : 5187934 Output : 37 


print("Enter Nnm")
num=int(input())

sum=0;

while num>0:
	reminder=num%10;
	sum=sum+reminder;
	num=num//10
print("addition of digits=",sum)


# output-:


# zine@DESKTOP-BU1PSC0 MINGW64 ~/Desktop/python/Assignment/Assignment2
# $ python Assignment2_10.py
# Enter Nnm
# 12345
# addition of digits= 15

