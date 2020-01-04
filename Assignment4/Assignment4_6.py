
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




def fun(RawData):

	for val in RawData: 
	    
	   if val > 1: 
	       for n in range(2, val): 
	           if (val % n) == 0: 
	               break
	       else: 
	       	a.append(val)
	       	return a 

a=list()
a=fun(RawData)
print(a)


				


# for val in RawData: 
    
#    if val > 1: 
#        for n in range(2, val): 
#            if (val % n) == 0: 
#                break
#        else: 
#            print(val) 



# result=reduce(lambda no:max(no),modified);
# print(result);


# a=max(modified);
# print(a)
