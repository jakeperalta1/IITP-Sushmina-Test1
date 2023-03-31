#QUESTION 1
#asking for input from user
print("Melanie Dental Clinic")
x= input("Enter patient's name:")
q1= input("Was clesning performed? y/n :")
q2= input("Was cavity-filling performed? y/n :")
q3= input("Was X-ray performed? y/n :")

print("1- Cleaning rate: $60")
print("2- Cavity filling rate: $200")
print("3- X-Ray rate: $100")
print("4- Tax rate: 15%")

#calculating tax amount
print("Tax")
def calculating_tax(a,b,c):
  e=a+b+c
  e=e*.15
  print(e)
t=calculating_tax(60,200,100)

def total(a,b,c,e):
    t=a+b+c+e
    print(t)
z=total(60,200,100,54)

#asking for input to calculate discount according to Total
x=int(input("Grand Total: "))
if (x>200):
  print(x-5/100*x)
elif (x>300):
  print(x-10/100*x)
else:
  print(x)
  


