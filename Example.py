x= int(input("Enter number of years: "))
l= 0
num= int(input("For year:"))
while(l<num):
    
    j= 0
    k=0
    total=0

    while(j<12):
        k= int(input(f"Enter the rainfall amount for {j+1}:"))
        total= total+k
        j+=1
    print("Total rainfall:",total,"")
    average = total/12
    print("Average monthly rainfall:",average)
    l=l+1





   