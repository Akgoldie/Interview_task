import decimal

def roundItoff(fractionNum,precision):
    print(round(fractionNum,precision))

fractionNum=float(input("Enter the fraction number: "))
precision=int(input("Enter the precision number: "))

str_num=str(fractionNum)
list=str_num.split(".")
#print(list)
digits=len(list[1])
#print(digits)

if(fractionNum>0 and precision>0 and precision<=3 and digits<=5):
    roundItoff(fractionNum,precision)
else:
    print("Error: Invalid Input")


