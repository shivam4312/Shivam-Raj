thisislist=["Apple","Orange", "Cherry"]
thisistuple=("Apple","Orange", "Cherry")
thisisset={"Apple","Orange", "Cherry"}
for s in thisislist:
    print(s)
thisisset.add("Grapes")
print(thisisset)
thisislist.append("Grapes")
print(thisislist)
thisislist.remove("Grapes")
print(thisislist)
thisisset.remove("Grapes")
if "Apple" in thisislist:
    print("Yes")
thisislist[1]="Blackcurrent"
print(thisislist)
thisislist.insert(3,"Orange")
print(thisislist)
thisislist.pop()
print(thisislist)
thisisset.clear()
print(thisisset)
del thisislist[2]
print(thisislist)
x=thisislist.count("Apple")
print(x)
y=15,thisislist.copy()
print(y)
thisislist.extend(thisisset)
print(thisislist)
thisislist.sort()
print(thisislist)
