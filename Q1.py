print("Melanie Dental Clinic")
x= input("Enter patient's name:")
q1= input("Was clesning performed? y/n :")
q2= input("Was cavity-filling performed? y/n :")
q3= input("Was X-ray performed? y/n :")

print("1- Cleaning rate: $60")
print("2- Cavity filling rate: $200")
print("3- X-Ray rate: $100")
print("4- Tax rate: 15%")

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

def discount(z):
    q=z-10/100*z
    print(q)
discount(414)


