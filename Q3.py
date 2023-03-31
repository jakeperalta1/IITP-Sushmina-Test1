#Question3

#global variable
PENNY_VALUE = 1
NICKEL_VALUE = 5
DIME_VALUE = 10
QUARTER_VALUE = 25
PENNIES_IN_DOLLAR = 100

#taking input from user

def inputs():
    a=int(input("Number of pennies: "))
    b=int(input("Number of nickel: "))
    c=int(input("Number of dimes: "))
    d=int(input("Number of quarters "))
    return a,b,c,d

#calculation
def values(a,b,c,d):
    TotalCents_penny= a*PENNY_VALUE
    TotalCents_nickel= b*NICKEL_VALUE
    TotalCents_dimes= c*DIME_VALUE
    TotalCents_Dollars= d*PENNIES_IN_DOLLAR
    TotalCents= (TotalCents_dimes+TotalCents_penny+TotalCents_nickel+TotalCents_Dollars)
     
    print(TotalCents)
    
a,b,c,d= inputs()
values(a,b,c,d)

x= float(input("Enter Total Cents: "))
TotalDollars= x/PENNIES_IN_DOLLAR
print(TotalDollars)

# giving Response
if (x>1.0):
    print("Sorry, the amount you entered was more than one dollar.")
elif(x<1.0):
    print("Sorry, the amount you entered was less than one dollar.")
else:
    print("Congratulations! The amount you entered was exactly one dollar! You win the game!!")
   