l=[12,23,1,234,34]
n=len(l)
for i in range (n-1):
    for j in range (n-1-i):
        if (l[j]>l[j+1]):
            l[j],l[j+1]=l[j+1],l[j]
print("Sorted list : ",l)
