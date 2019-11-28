# 4.Write a program which accept N numbers from user and store it into List. Accept one another
# number from user and return frequency of that number from List.
# Input : Number of elements : 11
# Input Elements : 13 5 45 7 4 56 5 34 2 5 65
# Element to search : 5
# Output : 3 


def freq(no):
	for i in range (no):
		print("Input Element ",i+1);
		num=int(input());
		user_list.append(num);
	print(user_list);

	find_num=int(input("Element to search :"));
	count=user_list.count(find_num);
	print("Frequency  Is -:",count);


no=int(input("Enter Num-"));
user_list=list();
freq(no)











# Output-:

# zine@DESKTOP-BU1PSC0 MINGW64 ~/Desktop/python/Assignment/Assignment3
# $ python Assignment3_4.py
# Enter Num-5
# Input Element  1
# 10
# Input Element  2
# 20
# Input Element  3
# 10
# Input Element  4
# 10
# Input Element  5
# 30
# [10, 20, 10, 10, 30]
# Element to search :10
# Frequency  Is -: 3

