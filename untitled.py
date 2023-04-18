print("1. Select 1 Insert product")
print("2. Select 2 for Searching")
print("3. Select 3 to delete product")
print("4. Select 4 to exit")

a={}

while True:
    x=int(input("Enter Option: "))
    if x==1:
        ee= int(input("How many times?"))
        for i in range(ee):
            if len(a)==10:
                 print("Inventory is full.")
            
            
            p=input("Enter book")
            q=input("Enter author")
            a.update({p:q})
            print(a)
        print("book added")
      
        
    
    elif x==2:
        f= input("Enter book:")
        if f==p:
            print("product exist",q)
        else:
            print("no product with this name.")
        
    elif x==3:
        g= input("Enter book name:")
        del a[g]
        print("book deleted")
    
    #(elif x==4:
        #h=input("Enter book:")
        #i=input("Enter author:")
        #a[h] = i
       # a.update({h:i})
        #print(a))
        
        #print("book updated")
       
       
    elif x==4:
        print("Thank you.")
        break
        
    else:
        print("option not available")
    
        
print(a)       
        
        
    
        
            
    
 
    