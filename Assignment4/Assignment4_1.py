# 1.Write a program which contains one lambda function which accepts one parameter and return
# power of two.
# Input : 4 Output : 16
# Input : 6 Output : 64 

fptr=lambda no:(2**no);

no=int(input("Enter Pawer Of Two -:"));
ans=fptr(no);
print("pawer Of Two is-:",ans);


# output-:
# zine@DESKTOP-BU1PSC0 MINGW64 ~/Desktop/python/Assignment/Assignment4
# $ python Assignment4_1.py
# Enter Pawer Of Two -:4
# pawer Of Two is-: 16
