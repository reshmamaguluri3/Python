ch=input()
n=int(input())
ch=ch.upper()
if(ch=="MON" or ch=="TUE" or ch=="WED" or ch=="THU"):
    if(n>=700 and n<=1000):
        print("successfull")
    else:
        print("unsuccessfull")
elif(ch=="FRI" or ch=="SAT" or ch=="SUN"):
    if(n>=1500):
        print("successfull")
    else:
        print("unsuccessfull")
else:
    print("Invalid Input")
        
