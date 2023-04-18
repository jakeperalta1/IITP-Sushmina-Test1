print("1.add")
print("2.search")
print("3.delete")
print("4.update")
print("5.exit")



a={}


while True:
    x=int(input("Enter Option: "))
    if x==1:
        for i in range(3):
            p=input("Enter book")
            q=input("Enter author")
            a.update({p:q})
            print(a)
            print("book added")
            
            print("1.add")
            print("2.search")
            print("3.delete")
            print("4.update")
            print("5.exit")
    
    elif x==2:
        
        f= input("Enter book:")
        print("Author: ",q)
        
    elif x==3:
        g= input("Enter book name:")
        del a[g]
        print("book deleted")
    
    elif x==4:
        h=input("Enter book:")
        i=input("Enter author:")
        #a[h] = i
        a.update({h:i})
        print(a)
        
        print("book updated")
       
       
    elif x==5:
        print("Thank you.")
        break
        
    else:
        print("option not available")
        
print(a)       
        
        
    
        
            
    
 
    