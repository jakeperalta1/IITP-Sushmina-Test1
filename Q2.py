def takeInput():
    a= float(input("Please input your first number: "))
    op= input("Input the operation you would like to use: ")
    c = float(input("Please input your second number: "))
    return a,op,c

def display_Result(a,op,c):
    
    if (op=="+"):
        print(a,"+",c,"=",a+c)
    elif(op=="-"):
        print(a,"-",c,"=",a-c)
    elif(op=="*"):
        print(a,"*",c,"=", a*c)
    elif(op=="/"):
        print(a,"/",c,"=",a/c)
    else:
        print("Invalid")

a,op,c = takeInput()
display_Result(a,op,c)