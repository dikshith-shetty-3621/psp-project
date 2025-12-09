a = input().lower()



abl = 'abcdefghijklmnopqrstuvwxyz'
alphabet = []
for i in abl:
    alphabet.append(i)

ans = [" "]* len(abl)

for i in a:

    inde=abl.find(i)
    ans[inde] = a.count(i)


    
for i in range(len(abl)):
    if ans[i] != " ":
        
    
        print(abl[i], "#"*ans[i])
    else:
        print(abl[i], 0)
