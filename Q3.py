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

def outputs(a,b,c,d):
    TotalCents_penny= a*PENNY_VALUE
    TotalCents_nickel= b*NICKEL_VALUE
    TotalCents_dimes= c*DIME_VALUE
   