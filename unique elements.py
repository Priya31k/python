string=str(input("Enter the string :"))
lstr=list(string.split())
mp={}
y=[]
for i in range(len(lstr)):
     if(lstr[i] not in mp):
         mp[lstr[i]]=0
     mp[lstr[i]]+=1

for x in mp:
    if(mp[x]==1):
        y.append(x)
print(len(y))
print(mp)
