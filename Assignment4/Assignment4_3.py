# 3.Write a program which contains filter(), map() and reduce() in it. Python application which
# contains one list of numbers. List contains the numbers which are accepted from user. Filter
# should filter out all such numbers which greater than or equal to 70 and less than or equal to
# 90. Map function will increase each number by 10. Reduce will return product of all that
# numbers.
# Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
# List after filter = [76, 89, 86, 90, 70]
# List after map = [86, 99, 96, 100, 80]
# Output of reduce = 6538752000 

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
	if ((no >=70) and (no<=90)):
		return True;

	else:
		return False;

def modifydata(no):
	return no+10;

def mul(no1,no2):
	return no1*no2;



RawData=userdata();
print(RawData);

filterdata=list(filter(Checknum,RawData));
print("List after filter-")
print(filterdata);

modifydata=list(map(modifydata,filterdata));
print("List after map-");
print(modifydata);

result=reduce(mul,modifydata);
print("final result is",result);


# Output-:


# zine@DESKTOP-BU1PSC0 MINGW64 ~/Desktop/python/Assignment/Assignment4
# $ python Assignment4_3.py
# num of data-12
# Enter num  1
# 4
# Enter num  2
# 34
# Enter num  3
# 36
# Enter num  4
# 76
# Enter num  5
# 68
# Enter num  6
# 24
# Enter num  7
# 89
# Enter num  8
# 23
# Enter num  9
# 86
# Enter num  10
# 90
# Enter num  11
# 45
# Enter num  12
# 70
# [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
# List after filter-
# [76, 89, 86, 90, 70]
# List after map-
# [86, 99, 96, 100, 80]
# final result is 6538752000

