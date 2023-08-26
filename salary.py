name=input('Enter your name: ')
num=int(input('Enter your number: '))
salary=float(input('Enter your salary: '))

if salary<=10000:
    da=30 
elif salary<=15000:
    da=40 
elif salary<=20000:
    da=50 
elif salary>20000:
    da=60
    
if salary<=10000:
    hra=10 
elif salary<=15000:
    hra=15 
elif salary<=20000:
    hra=20 
elif salary>20000:
    hra=25

x=salary*da/100
y=salary*hra/100
gross=salary+x+y
print('The Gross salary of',name,'is',gross)
