//Program to create GCP in python
def gcd(a1,b1):

    small=0

    gd=0

    if a1>b1:

        small==b1

    else:

        small==a1

    for i in range(1, small+1):

        if((a1 % i == 0) and (b1 % i == 0)):

            gd=i

    return gd

a1=int(input("Enter the first number: "))

b1=int(input("Enter second number: "))

t=gcd(a1,b1)

print("GCD is:",t)
