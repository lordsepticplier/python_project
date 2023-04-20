income=float(input("your income"))  # this program will find your tax
if income<=14000:  # this uses else if statements to find what your tax range is
    tax = income*0.105
    print(tax,"is your tax")
elif income<=48000:
    tax = (income-14000)*0.175+1470
    print(tax,"is your tax")
elif income<=70000:
    tax = (income-48000)*0.3+7420
    print(tax,"is your tax")
elif income<=180000:
    tax = (income-70000)*0.33+14020
    print(tax,"is your tax")
elif income>180000:
    tax = (income-180000)*0.39+50320
    print(tax,"is your tax")
else:  # this is used to catch the exceptions
    print("is this within the parapters?")