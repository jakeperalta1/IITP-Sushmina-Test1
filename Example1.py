m = int(input("Enter month:"))
f= int(input("Initial fine:"))
j=0
while(j<12):
        print(f"month{j+1}: {f}")
        f= 1.15*f
        j+=1

#for i in range(user):
    #print("Color {}".format(i+1))
    