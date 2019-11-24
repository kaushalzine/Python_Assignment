# 2. Write a program which contains one function named as ChkNum() which accept one
# parameter as number. If number is even then it should display “Even number” otherwise
# display “Odd number” on console.
# Input : 11 Output : Odd Number
# Input : 8 Output : Even Number 


def chkNum(num) :
	if(num%2==0):
		print("Even Number ");
	else :
		print("Odd Number ");


num=int(input());
chkNum(num)


# output-:

# zine@DESKTOP-BU1PSC0 MINGW64 ~/Desktop/python/Ass1
# $ python even_odd.py
# 11
# Odd Number

# zine@DESKTOP-BU1PSC0 MINGW64 ~/Desktop/python/Ass1
# $ python even_odd.py
# 8
# Even Number

