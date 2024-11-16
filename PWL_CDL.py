f=10**(-15)
p=10**(-12)
n=10**(-9)
u=10**(-6)
m=10**(-3)
s=1
F=f; P=p; N=n; U=u; M=m; S=s; V=s; v=s;
print("f=femto,\n p=pico,\n n=nano,\n u=micro,\n m=mili,\n s=socond\n The inputs are not case sensitive.\n")

rtu = input("Enter the unit for rise time:")
if (rtu=='f' or rtu=='p' or rtu=='u' or rtu=='n' or rtu=='m' or rtu=='s' or rtu=='F' or rtu=='P' or rtu=='U' or rtu=='N' or rtu=='M' or rtu=='S'):
    print("Input is valid")
else:
    print("Input is invalid")
if (rtu=='f' or rtu=='F'):
    rtu=float(f)
elif (rtu=='p' or rtu=='P'):
    rtu=float(p)
elif (rtu=='n' or rtu=='N'):
    rtu=float(n)
elif (rtu=='u' or rtu =='U'):
    rtu=float(u)
elif (rtu=='m' or rtu =='M'):
    rtu=float(m)
elif (rtu=='s' or rtu =='S'):
    rtu=float(s)

rt=float(input("Input the rise time:"))

ftu = input("Enter the unit for fall time:")
if (ftu=='f' or ftu=='p' or ftu=='u' or ftu=='n' or ftu=='m' or ftu=='s' or ftu=='F' or ftu=='P' or ftu=='U' or ftu=='N' or ftu=='M' or ftu=='S'):
    print("Input is valid")
else:
    print("Input is invalid")
if (ftu=='f' or ftu=='F'):
    ftu=float(f)
elif (ftu=='p' or ftu=='P'):
    ftu=float(p)
elif (ftu=='n' or ftu=='N'):
    ftu=float(n)
elif (ftu=='u' or ftu =='U'):
    ftu=float(u)
elif (ftu=='m' or ftu =='M'):
    ftu=float(m)
elif (ftu=='s' or ftu =='S'):
    ftu=float(s)

ft=float(input("\nInput the fall time:"))
pw=float(input("Enter the unit for time of the pulse:"))

vu=input("Input the umit for the voltage. \n V for volt, m for milivolt.\n")
hvv=float(input("Input the High level value for the PWL:"))
lvv=input("Input the Low level value for the PWL:")

print("Enter he time pairs for the duration when the signal is high.\nThe code will automatically calculate the low time duration.")

ht1=[]
ht2=[]

i=1
while True:
    print("Pair {}, high time 1:\nEner E or e to stop".format(i))
    hx1=input()
    if (hx1 == 'E' or hx1 == 'e'):
        break
    ht1.append(float(hx1))
    print("Pair {}, high time 2:".format(i))
    hx2=input()
    if (hx2 == 'E' or hx2 == 'e'):
        break
    ht2.append(float(hx2))
    i=i+1

    
