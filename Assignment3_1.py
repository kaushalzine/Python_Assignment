# 1.Write a program which accept N numbers from user and store it into List. Return addition of all
# elements from that List.
# Input : Number of elements : 6
# Input Elements : 13 5 45 7 4 56
# Output : 130 


def add(no):
	for i in range(no):
		print("Enter num -",i+1);
		user_number=int(input());
		user_number_list.append(user_number);

	print(user_number_list);


	sum=0;
	for i in user_number_list:
		sum+=i;
	return sum;



no=int(input("Enter Number of elements :"));
user_number_list=list();
# size=len(no);

a=add(no);
print("Addition of user Numbers-",a);



# output-:


# zine@DESKTOP-BU1PSC0 MINGW64 ~/Desktop/python/Assignment/Assignment3
# $ python Assignment3_1.py
# Enter Number of elements :3
# Enter num - 1
# 10
# Enter num - 2
# 20
# Enter num - 3
# 30
# [10, 20, 30]
# Addition of user Numbers- 60
