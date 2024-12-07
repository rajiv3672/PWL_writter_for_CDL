#Defining constants for the calculation.
f=10**(-15); p=10**(-12); n=10**(-9); u=10**(-6); m=10**(-3); s=1;
F=f; P=p; N=n; U=u; M=m; S=s; V=s; v=s;
result=[]

print("f=femto,\n p=pico,\n n=nano,\n u=micro,\n m=mili,\n s=socond\n The inputs are NOT case sensitive.\n")


def var_assign(X):#This part sets the float values to the string inputs.
    
    if (X=='f' or X=='p' or X=='u' or X=='n' or X=='m' or X=='s' or X=='F' or X=='P' or X=='U' or X=='N' or X=='M' or X=='S'):
        print("Input is valid")
    else:
        print("Input is invalid")
    if (X=='f' or X=='F'):
        X=float(f)
    elif (X=='p' or X=='P'):
        X=float(p)
    elif (X=='n' or X=='N'):
        X=float(n)
    elif (X=='u' or X =='U'):
        X=float(u)
    elif (X=='m' or X =='M'):
        X=float(m)
    elif (X=='s' or X =='S' or X=='V' or X=='v'):
        X=float(s)
    return X

rtu = input("Enter the UNIT for rise time:")
rtu = var_assign(rtu)
rt=float(input("Input the rise time:"))

ftu = input("Enter the UNIT for fall time:")
ftu = var_assign(ftu)
ft=float(input("\nInput the fall time:"))

pw=input("Enter the UNIT for time of the pulse:")
pw = var_assign(pw)

vu=input("Input the UNIT for the voltage.")
hvv=float(input("Input the High level value for the PWL:"))
lvv=float(input("Input the Low level value for the PWL:"))
hvv=hvv*var_assign(vu)
lvv=lvv**var_assign(vu)


td=0
ins=input("Input the instance's name:")
port1=input("Input the +ve port's name:")
port2=input("Input the -ve port's name:")
result.append(ins)
result.append(port1)
result.append(port2)
result.append('PWL')
print("Enter he time pairs for the duration when the signal is high.\nThe code will automatically calculate the low time duration.\n PLEASE COMPLETE THE PAIRS")

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
    lt2.append(lt1[len(lt1)-1])

k=0
while True:
    if (k>=i):
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

if (ht1[0] == 0):#pops out two redundant values
    result.pop(len(result)-1)
    result.pop(len(result)-1)

if (ht1[0] != 0):#APPENDS EXTRA VALUE FOR ENDING THE PWL VALUE IN ZERO AS IT IS PREFFERRED FOR SIMULATION
    result.append(ht2[(len(ht2)-1)]+ftu)
    result.append(0)

result.append('TD=0')

print(' '.join(map(str, result)))
with open("PWL_result.txt", "a") as f:
    print(' '.join(map(str, result)), file=f)
