income=float(input("your income"))
if income<=14000:
    tax = income*0.105
    print(tax,"is your tax1")
elif income<=48000:
    tax = (income-14000)*0.175+1470
    print(tax,"is your tax2")
elif income<=70000:
    tax = (income-48000)*0.3+7420
    print(tax,"is your tax3")
elif income<=180000:
    tax = (income-70000)*0.33+14020
    print(tax,"is your tax4")
elif income>180000:
    tax = (income-180000)*0.39+50320
    print(tax,"is your tax5")
else:
    print("is this within the parapters?")