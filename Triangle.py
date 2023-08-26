a=float(input('Enter the measurement of side 1: '))
b=float(input('Enter the measurement of side 2: '))
c=float(input('Enter the measurement of side 3: '))

if a==b==c:
    print('This is an Equilateral Triangle')
elif a==b or b==c or a==c:
    print('This is an Isoceles Triangle')
else:
    print('This is a Scalene Triangle ')