salary=float(input('Enter your salary: '))
if salary<=50000:
    tax=0.05*salary
elif salary<=60000:
    tax=0.07*salary
elif salary<=70000:
    tax=0.08*salary
else:
    tax=0.10*salary
print('Your salary is',salary,'and the tax needed to pay is',tax)