#Input values
P = int(input("\n Enter the principal amount: "))
T = int(input("\n Enter the time: "))
R = int(input("\n Enter the rate(as a decimal): ")) 
n =  int(input("\n Enter the compounding time"))

# calculate simple interest and commpound interest
Simpleinterest = P * T * R
Compoundinterest = P * (((1 + R/n)** (n*T)))
Annuityplan =  P * (((1 + R/n)** (n*T) -1) / (R/n))


#Output
print("\n Simple Interest = ",Simpleinterest)
print("\n Compound Interest = ",Compoundinterest)
print("\n Annuity Plan = ",Annuityplan)