#  Write a program which display first 10 even numbers on screen.
# Output : 2 4 6 8 10 12 14 16 18 20 

def fun(num):
	for i in range(2,num*2+2,2):
		print(" ",i);
		
num=int(input())
fun(num)

# Output-:
# zine@DESKTOP-BU1PSC0 MINGW64 ~/Desktop/python/Ass1
# $ python even_num.py
# 10
#   2
#   4
#   6
#   8
#   10
#   12
#   14
#   16
#   18
#   20
