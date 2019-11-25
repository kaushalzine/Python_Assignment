# 3. Write a program which accept one number from user and return its factorial.
# Input : 5 Output : 120 

print("Enter num");
num=int(input());
factorial=1;
for i in range(1,num + 1):
       factorial = factorial*i;

print("factorial is= ",factorial);

# Output-:
# zine@DESKTOP-BU1PSC0 MINGW64 ~/Desktop/python/Assignment/Assignment2
# $ python Assignment2_3.py
# Enter num
# 5
# factorial is=  120

