#sum of all digit

sum=0;
for a in range(1,6):
	sum=sum+a;
print(sum);

#prime number
num=11;
count=0;
for a in range(1,num+1):
	if(num%a==0):
		count+=1;
if(count==2):
	print("Prime Number");
else:
	print("Not Prime Number");


num=496;
sum=0;
for a in range(1,num):
	if(num%a==0):
		print(a);
		sum=sum+a;		
if(num==sum):
	print("It is perfect Square");
else:
	print("In is not perfect Square");
