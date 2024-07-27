#program to check if a number is krishnamurthy number or not
num = int(input("Enter the number:"))
sum = 0
temp = num
while temp>0:
    r = temp%10
    factorial = 1
    for i in range(1, r+1):
        factorial = factorial *i
    sum = sum+factorial
    temp//=10
if num==sum:
    print("krishnamurthy no")
else:
    print("not a Krishnamurthy no")
