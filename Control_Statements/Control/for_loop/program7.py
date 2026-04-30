for a in range(1,5,2):
	print(a);


for a in range(1,5):
	if(a%2==1):
		print(a);

count=0;
for a in range(1,5):
	if(a%2==1):
		count+=1;
print(count);

count=0;
for a in range(1,5):
	if(a%2==0):
		count+=1;
print(count);