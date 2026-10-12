a=input("enter the name:")
ans=[]
for ch in a:
    if ch not in ans:
        ans.append(ch)
print(ans)     
