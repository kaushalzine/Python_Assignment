def ListPrime(no):
	user_list=list();
	for i in range(no):
		print("Enter element",i+1);
		num=int(input());
		user_list.append(num);
	print(user_list);

	prime=list();
	for j in user_list:
		if (j%2)==0:
			print("");		
		else :	
			prime.append(j);
	print("prime  num =",prime);	
	sum=0;
	
	for k in prime:
		sum+=k;
	print(sum);

