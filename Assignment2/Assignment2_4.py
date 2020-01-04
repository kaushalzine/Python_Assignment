
# 4.Write a program which accept one number form user and return addition of its factors.
# Input : 12 Output : 16 (1+2+3+4+6) 

print("Enter num");
num=int(input());
factorial=1;
for i in range(1,num + 1):
       factorial = factorial+i;


print("factorial is= ",factorial);



# output-:

# zine@DESKTOP-BU1PSC0 MINGW64 ~/Desktop/python/Assignment/Assignment2
# $ python Assignment2_4.py
# Enter num
# 5
# factorial is=  16
