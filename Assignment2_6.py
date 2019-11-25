# 6. Write a program which accept one number and display below pattern.
# Input : 5
# Output : * * * * *
#  * * * *
#  * * *
#  * *
#  * 
#  

def fun(num):

	for i in range(num,0,-1):
		# for j in range(0,i+1):
		# 	print(" * " ,end='');
		# print("\r");
		print(" * " *i);

print("Enter num");
num=int(input())
fun(num)


# output-:


# zine@DESKTOP-BU1PSC0 MINGW64 ~/Desktop/python/Assignment/Assignment2
# $ python Assignment2_6.py
# Enter num
# 5
#  *  *  *  *  *
#  *  *  *  *
#  *  *  *
#  *  *
#  *
