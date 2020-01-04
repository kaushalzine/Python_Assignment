# 4.Write a program which contains filter(), map() and reduce() in it. Python application which
# contains one list of numbers. List contains the numbers which are accepted from user. Filter
# should filter out all such numbers which are even. Map function will calculate its square.
# Reduce will return addition of all that numbers.
# Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
# List after filter = [2, 4, 4, 2, 8, 10]
# List after map = [4, 16, 16, 4, 64, 100]
# Output of reduce = 204 






from functools import *;


def userdata():
	listnum=int(input("num of data-"));
	userlist=list()
	for i in range(listnum):
		print("Enter num ",i+1);
		num=int(input());
		userlist.append(num);
	return userlist;

def Checknum(no):
	if (no%2==0):
		return True;

	else:
		return False;

def modifydata(no):
	return no**2;

def add(no1,no2):
	return no1+no2;



RawData=userdata();
print(RawData);

filterdata=list(filter(Checknum,RawData));
print("List after filter-")
print(filterdata);

modifydata=list(map(modifydata,filterdata));
print("List after map-");
print(modifydata);

result=reduce(add,modifydata);
print("final result is",result);


# output-:
# zine@DESKTOP-BU1PSC0 MINGW64 ~/Desktop/python/Assignment/Assignment4
# $ python Assignment4_4.py
# num of data-5
# Enter num  1
# 2
# Enter num  2
# 4
# Enter num  3
# 6
# Enter num  4
# 3
# Enter num  5
# 5
# [2, 4, 6, 3, 5]
# List after filter-
# [2, 4, 6]
# List after map-
# [4, 16, 36]
# final result is 56
