num=int(input("Enter the number"))
temp=num
sum=0
while(temp>0):
    r=temp%10
    sum=sum+r*r*r
    temp//=10
if(num==sum):
    print("Armstrong no")
else:
    print("Not armstrong")
