# 5. Accept file name and one string from user and return the frequency of that string from file.
# Input : Demo.txt Marvellous
# Search “Marvellous” in Demo.txt



fobj = open("demo.txt")
text = fobj.read().strip().split()
 
#Conditions
while True:
    s = input("Enter a string: ") 
    if s == "": 
        continue
    if s in text:
        print("Matched")
        break
    else: 
        print("No such string found,try again")
        continue
fobj.close()