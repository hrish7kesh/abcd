x=input("Enter a string : ")
l=x.split()
s={}
for i in l:
    if i not in s.keys():
        s[i]=0
    s[i]+=1
print(s)
