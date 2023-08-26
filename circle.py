r=float(input('Enter the radius of a circle: '))
print('1. Area of a circle')
print('2. Perimeter of a circle')
choice=int(input('Enter your choice (1 or 2):'))
if choice==1:
    area=(22/7)*r**2
    print('The area of the circle is',area)
else:
    perimeter=2*(22/7)*r
    print('The perimeter of the circle is',perimeter)
