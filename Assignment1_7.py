#  Write a program which contains one function that accept one number from user and returns
# true if number is divisible by 5 otherwise return false.
# Input : 8 Output : False
# Input : 25 Output : True

def fun(num) :
	if num%5==0 :
		return True
	else :
		return False


num=int(input())
ans=fun(num) 
print(ans);





# Output-:

# zine@DESKTOP-BU1PSC0 MINGW64 ~/Desktop/python/Ass1
# $ python true_false.py
# 25
# True

# zine@DESKTOP-BU1PSC0 MINGW64 ~/Desktop/python/Ass1
# $ python true_false.py
# 8
# False
