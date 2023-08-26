math=float(input('Enter math marks: '))
phy=float(input('Enter physics marks: '))
chem=float(input('Enter chemistry marks: '))
cs=float(input('Enter computer science marks: '))
total=math+phy+chem+cs
avg=total/4
print('Average:',avg)
if avg>=50:
    print('Passed')
else:
    print('Failed')