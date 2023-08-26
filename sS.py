PurchaseAmount=float(input('Enter your Purchase Amount: '))
if PurchaseAmount<=5000:
    Discount=400
elif PurchaseAmount >5000 and PurchaseAmount<= 10000:
    Discount=800
elif PurchaseAmount >10000 and PurchaseAmount<= 20000:
    Discount=1000
elif PurchaseAmount >20000:
    Discount=2000
    
NetAmount1=PurchaseAmount-Discount

if PurchaseAmount >20000:
    AdditionalDiscount=NetAmount1*3/100
else:
    AdditionalDiscount=0
    
TotDiscount=Discount+AdditionalDiscount
NetAmount2=PurchaseAmount-TotDiscount

print("Purchase Amount: ",PurchaseAmount)
print("Discount: ",Discount)
print("Additional Discount: ",AdditionalDiscount)
print("Total Discount: ", TotDiscount)
print("Net Total Amount (After Total discount): ",NetAmount2)



