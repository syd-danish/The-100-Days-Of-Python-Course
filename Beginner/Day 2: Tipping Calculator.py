print("WELCOME THE TIPPING CALCULATOR")
bill=float(input("What is the total bill ?\n "+ "$"))
prct=int(input("How much tip would you like to give? " +" 10,12 or 15 \n"))
n=int(input("How many people are splitting the bill? "))
tip=(prct/100)*bill
each_pay=(bill+tip)/n
each_pay=round(each_pay,2)
print("Each Person should pay "+ str(each_pay) +" dollarz")
