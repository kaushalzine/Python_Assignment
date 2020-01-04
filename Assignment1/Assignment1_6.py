# 6.Write a program which accept number from user and check whether that number is positive or
# negative or zero.
# Input : 11 Output : Positive Number
# Input : -8 Output : Negative Number
# Input : 0 Output : Zero 


print("Enter num");
num=int(input())
if num > 0:
	print ("Positive Number");
elif num == 0:
	print("Zero");
else :
	print ("Negative Number");





# Output-:
# zine@DESKTOP-BU1PSC0 MINGW64 ~/Desktop/python/Ass1
# $ python positivenum.py
# Enter num
# 5
# Positive Number

# zine@DESKTOP-BU1PSC0 MINGW64 ~/Desktop/python/Ass1
# $ python positivenum.py
# Enter num
# -5
# Negative Number

# zine@DESKTOP-BU1PSC0 MINGW64 ~/Desktop/python/Ass1
# $ python positivenum.py
# Enter num
# 0
# Zero
