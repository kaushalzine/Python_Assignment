# 5.Write a program which contains filter(), map() and reduce() in it. Python application which
# contains one list of numbers. List contains the numbers which are accepted from user. Filter
# should filter out all prime numbers. Map function will multiply each number by 2. Reduce will
# return Maximum number from that numbers. (You can also use normal functions instead of
# lambda functions).
# Input List = [2, 70 , 11, 10, 17, 23, 31, 77]
# List after filter = [2, 11, 17, 23, 31]
# List after map = [4, 22, 34, 46, 62]
# Output of reduce = 62


from functools import *;


def userdata():
	listnum=int(input("num of data-"))
	userlist=list()
	for i in range(listnum):
		print("Enter num ",i+1);
		num=int(input());
		userlist.append(num);
	return userlist;


RawData=userdata();
print(RawData);

filterd=list(filter(lambda no:((no%2)),RawData));
print(filterd);


modified=list(map(lambda no:(no*2),filterd));
print(modified);

# result=reduce(lambda no:max(no),modified);
# print(result);


a=max(modified);
print(a)
