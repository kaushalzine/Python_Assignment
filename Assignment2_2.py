# 2. Write a program which accept one number and display below pattern.
# Input : 5
# Output : * * * * *
#  * * * * *
#  * * * * *
#  * * * * *
#  * * * * *
  
def fun(num):

	for i in range(0,num):
		print(" *  " * num);

print("Enter row");
num=int(input());
fun(num)

# Output-:
# zine@DESKTOP-BU1PSC0 MINGW64 ~/Desktop/python/Assignment/Assignment2
# $ python Assignment2_2.py
# Enter row
# 5
#  *   *   *   *   *
#  *   *   *   *   *
#  *   *   *   *   *
#  *   *   *   *   *
#  *   *   *   *   *
