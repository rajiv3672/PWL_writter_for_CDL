#Defining constants fr the calculation.
f=10**(-15); p=10**(-12); n=10**(-9); u=10**(-6); m=10**(-3); s=1;
F=f; P=p; N=n; U=u; M=m; S=s; V=s; v=s;
result=[]

print("f=femto,\n p=pico,\n n=nano,\n u=micro,\n m=mili,\n s=socond\n The inputs are NOT case sensitive.\n")

rtu = input("Enter the UNIT for rise time:")
#This part sets the float values to the string inputs.
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

ftu = input("Enter the UNIT for fall time:")
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

pw=input("Enter the UNIT for time of the pulse:")
if (pw=='f' or pw=='p' or pw=='u' or pw=='n' or pw=='m' or pw=='s' or pw=='F' or pw=='P' or pw=='U' or pw=='N' or pw=='M' or pw=='S'):
    print("Input is valid")
else:
    print("Input is invalid")
if (pw=='f' or pw=='F'):
    pw=float(f)
elif (pw=='p' or pw=='P'):
    pw=float(p)
elif (pw=='n' or pw=='N'):
    pw=float(n)
elif (pw=='u' or pw =='U'):
    pw=float(u)
elif (pw=='m' or pw =='M'):
    pw=float(m)
elif (pw=='s' or pw =='S'):
    pw=float(s)


vu=input("Input the umit for the voltage. \n V for volt, m for milivolt.\n")
hvv=float(input("Input the High level value for the PWL:"))
lvv=float(input("Input the Low level value for the PWL:"))
if (vu == 'm' or vu== 'M'):
    hvv=hvv*m
    lvv=lvv*m

td=0
ins=input("Input the instance's name:")
port1=input("Input the +ve port's name:")
port2=input("Input the -ve port's name:")
result.append(ins)
result.append(port1)
result.append(port2)
result.append('PWL')
print("Enter he time pairs for the duration when the signal is high.\nThe code will automatically calculate the low time duration.")

ht1=[]
ht2=[]
i=0
while True:
    print("Pair {}, high time 1:\nEner E or e to stop".format(i+1))
    hx1=input()
    if (hx1 == 'E' or hx1 == 'e'):
        break
    ht1.append(float(hx1)*pw)
    print("Pair {}, high time 2:".format(i+1))
    hx2=input()
    if (hx2 == 'E' or hx2 == 'e'):
        break
    ht2.append(float(hx2)*pw)
    i=i+1


lt1=[]
lt2=[]
j=0
if (ht1[0] != 0):
    lt1.append(0)
    lt2.append(ht1[0]-rt*float(rtu))
while j<i:
    lt1.append(ht2[j] + ft*float(ftu))
    if ((j+1)>=i):
        break
    else:
        lt2.append(ht1[j+1] - rt*float(rtu))
    j=j+1

if (ht1[0] != 0):
    lt1.pop(len(lt1)-1)
elif (ht1[0] == 0):
    lt2.append(lt1[len(lt1)])

k=0
while True:
    if ((k+1)>=i):
        break
    if (lt1[0]<ht1[0]):
        result.append(lt1[k])
        result.append(lvv)
        result.append(lt2[k])
        result.append(lvv)
        result.append(ht1[k])
        result.append(hvv)
        result.append(ht2[k])
        result.append(hvv)
    
    elif (lt1[0]>ht1[0]):
        result.append(ht1[k])
        result.append(hvv)
        result.append(ht2[k])
        result.append(hvv)
        result.append(lt1[k])
        result.append(lvv)
        result.append(lt2[k])
        result.append(lvv)
    k=k+1

result.append('TD=0')

print(' '.join(map(str, result)))
with open("PWL_result.txt", "a") as f:
    print(' '.join(map(str, result)), file=f)