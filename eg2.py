#for i in range(2):
 #       print(f'*' + ' ' *i + '*')
 
a=[1,3,4,2,[0,5,9]]
print(len(a))

print(a[4][1])
a.append('hello')
print(a)

a=[4,5,6]
print(a)
b=[7,8,9]
print(b)
a.extend(b)
print(a)

a=['bmw','toyota','honda','benz']
a.insert(2,'volvo')
print(a)
a.remove('bmw')
#a.clear()
#print(a)
print(a.index("toyota"))
a.index("toyota")

print(a.count("honda"))

a.sort()
a.reverse()
print(a)

a=[3,6,1,2,8,5,9,7]
print(max(a))
print(a[3::])