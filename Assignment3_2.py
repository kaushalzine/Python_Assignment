# 2.Write a program which accept N numbers from user and store it into List. Return Maximum
# number from that List.
# Input : Number of elements : 7
# Input Elements : 13 5 45 7 4 56 34
# Output : 56 


def maxfun(no): 
	for i in range(no):
		print("Enter Number ",i+1);
		num=int(input());
		user_list.append(num);
	print(user_list);
	max_num=max(user_list);
	print(" Maximum Number is=",max_num);


no=int(input("Number of elements :"));
user_list=list();
maxfun(no)


# output-:


# zine@DESKTOP-BU1PSC0 MINGW64 ~/Desktop/python/Assignment/Assignment3
# $ python Assignment3_2.py
# Number of elements :5
# Enter Number  1
# 10
# Enter Number  2
# 5
# Enter Number  3
# 70
# Enter Number  4
# 60
# Enter Number  5
# 40
# [10, 5, 70, 60, 40]
#  Maximum Number is= 70
