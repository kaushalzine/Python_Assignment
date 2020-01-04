# 9 Write a program which accept number from user and return number of digits in that number.
# Input : 5187934 Output : 7 


def fun(strr):
	lenn=len(strr)
	return lenn;

print("Enter num");
num=int(input())
strr=str(num)

lenn=fun(strr)
print("Number of Digits=",lenn);


# Output-:
# zine@DESKTOP-BU1PSC0 MINGW64 ~/Desktop/python/Assignment/Assignment2
# $ python Assignment2_9.py
# Enter num
# 123456
# Number of Digits= 6
