n1=float(input('Enter first number: '))
n2=float(input('Enter second number: '))
n3=float(input('Enter third number: '))
if n1>n2 and n1>n3:
    print(n1,'is the bigger number.')
elif n2>n1 and n2>n3:
    print(n2,'is the bigger number.')
else:
    print(n3,'is the bigger number.')