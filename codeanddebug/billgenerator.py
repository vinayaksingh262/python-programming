bill_amount=float(input("Enter the amount :"))

if bill_amount>=50000:
    discount=30
elif bill_amount>=40000 and bill_amount<50000:
    discount=25
elif bill_amount>=30000 and bill_amount<40000:
    discount=20
elif bill_amount>=10000 and bill_amount<30000:
    discount=10
else:
    discount=0
print(f"You got {discount}% discount")

final_bill=bill_amount-(bill_amount*discount/100)
print(f"your final amount is {final_bill} ")