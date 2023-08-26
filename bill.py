bill=float(input('Enter your bill: '))
if bill>=20000:
    disc=0.15*bill
elif bill>=15000:
    disc=0.10*bill
elif bill>=10000:
    disc=0.05*bill
else:
    disc=0*bill
print('Your discount is',disc,'and your total bill is',bill-disc)