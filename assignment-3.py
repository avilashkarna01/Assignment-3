print("Question1")
l=[1,1,1]
l[0]=input("enter first element")
l[1]=input("enter second element")
l[2]=input("enter third element")
print(l)
print("\n")

print("Question2")
l=["Google","Apple","facebook","Microsoft","Tesla"]
l1=["Digital marketing","SEO","Google adsense","google adword"]
print(l.extend(l1))
print(l)
print("\n")


print("Question3")
l=[4,4,5,4,8,1,2,3,4]
print(l.count(4))
print("\n")

print("Question4")
x=[6,2,4,5,3,1]
x.sort()
print(x)
print("\n")


print("Question5")
x=[4,5,2,1,3,6]
y=[7,6,9,8,5,4]
z=x+y
print("merge list is",z)
z.sort()
print("sorted list is",z)
print("\n")


print("Question6")
x=[]
x.append(input("enter first value"))
x.append(input("enter second value"))
x.append(input("enter  third value"))
x.append(input("enter fourth value"))
print(x)
x.pop()
print(x)
print("\n")

y=[]
y.insert(0,input("enter first value"))
y.insert(0,input("enter second value"))
y.insert(0,input("enter  third value"))
y.insert(0,input("enter fourth value"))
print(y)
del y[0]
print(y)








