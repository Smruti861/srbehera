n=int(input("enter the value"))
if n>1:
    for i in range(2,n):
        if n%i==0:
            print("it is not a prime number")
            break
    else:
        print("it is a prime number")

