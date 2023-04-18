s= int(input("Starting number of organisms:"))
p= int(input("Average daily percentage increase:"))
m = int(input("Enter the number of days to display the final data:"))
j=0
while(j<m):
        print(f"month{j+1}: {s}")
        s=p/100*s
        j+=1