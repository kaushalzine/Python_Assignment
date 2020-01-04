# 2.Write a program which contains one lambda function which accepts two parameters and return
# its multiplication.
# Input : 4 3 Output : 12
# Input : 6 3 Output : 18 



fptr=lambda no1,no2:no1*no2;

no1=int(input("Enter Fist number-:"));
no2=int(input("Enter Second number-:"));

ans=fptr(no1,no2);
print("Two number multiplication =:",ans);


# Output-:

# zine@DESKTOP-BU1PSC0 MINGW64 ~/Desktop/python/Assignment/Assignment4
# $ python Assignment4_2.py
# Enter Fist number-:4
# Enter Second number-:3
# Two number multiplication =: 12
