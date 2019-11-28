# 3.Write a program which accept N numbers from user and store it into List. Return Minimum
# number from that List.
# Input : Number of elements : 4
# Input Elements : 13 5 45 7
# Output : 5 

def minfun(no): 
	for i in range(no):
		print("Enter Number ",i+1);
		num=int(input());
		user_list.append(num);
	print(user_list);
	min_num=min(user_list);
	print(" Minimum Number is=",min_num);


no=int(input("Number of elements :"));
user_list=list();
minfun(no)


# Output-:
# zine@DESKTOP-BU1PSC0 MINGW64 ~/Desktop/python/Assignment/Assignment3
# $ python Assignment3_3.py
# Number of elements :5
# Enter Number  1
# 10
# Enter Number  2
# 20
# Enter Number  3
# 20
# Enter Number  4
# 60
# Enter Number  5
# 30
# [10, 20, 20, 60, 30]
#  Minimum Number is= 10

