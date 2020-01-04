# 5.Write a program which accept one number for user and check whether number is prime or not.
# Input : 5 Output : It is Prime Number 
def fun(num):

	if (num%2)==0:
		print("Number Not prime");
	else :
		print("Number prime");


print("Enter Number-:");
num=int(input())
fun(num)



# output-:


# zine@DESKTOP-BU1PSC0 MINGW64 ~/Desktop/python/Assignment/Assignment2
# $ python Assignment2_5.py
# Enter Number-:
# 5
# Number prime

# zine@DESKTOP-BU1PSC0 MINGW64 ~/Desktop/python/Assignment/Assignment2
# $ python Assignment2_5.py
# Enter Number-:
# 6
# Number Not prime

