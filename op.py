num1=float(input('Enter the first number: '))
num2=float(input('Enter the second number: '))
op=input('Enter the operator: ')
if op=='+':
    result=num1+num2
elif op=='-':
    result=num1-num2
elif op=='*':
    result=num1*num2
elif op=='/':
    result=num1/num2
elif op=='%':
    result=num1%num2
else:
    result='Invalid'
    print('Invalid operator.')
print(num1,op,num2,'=',result)
