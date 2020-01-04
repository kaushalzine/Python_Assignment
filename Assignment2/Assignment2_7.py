# 7. Write a program which accept one number and display below pattern.
# Input : 5
# Output : 1 2 3 4 5
#  1 2 3 4 5
#  1 2 3 4 5
#  1 2 3 4 5
#  1 2 3 4 5 
#  

def fun(num):

	for i in range(1,num+1):
		for j in range(1,num+1):
			print(i ,end=" ")
		print("\r")


print("Enter row");
num=int(input());
fun(num)



# Output-:

# zine@DESKTOP-BU1PSC0 MINGW64 ~/Desktop/python/Assignment/Assignment2
# $ python Assignment2_7.py
# Enter row
# 5
# 1 1 1 1 1
# 2 2 2 2 2
# 3 3 3 3 3
# 4 4 4 4 4
# 5 5 5 5 5
