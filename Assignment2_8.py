
# 8 Write a program which accept one number and display below pattern.
# Input : 5

# Output : 1
#  1 2
#  1 2 3
#  1 2 3 4
#  1 2 3 4 5 




def fun(num):
	for i in range(1,num+1):
		for  j in range(1,i+1):
			print(j,end=" ")
		print("\r")


print("Enter Num-:");
num=int(input());
fun(num)



# output-:

# zine@DESKTOP-BU1PSC0 MINGW64 ~/Desktop/python/Assignment/Assignment2
# $ python Assignment2_8.py
# Enter Num-:
# 5
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
