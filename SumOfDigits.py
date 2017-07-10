num =int(input("Enter a Number : "))
sum=0
while(num!=0):
    rem=num%10
    sum=sum+rem
    num=num//10
print("The Sum of Your number is : ",sum)
