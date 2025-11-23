n = int(input())
db = {}
for i in range(n):
    name = input().strip()
    if name not in db:
        print("OK")
        db[name]=1
    else:
        k = db[name]
        new_name = name+str(k)
        while new_name in db:
            k+=1
            new_name = name+str(k)

        print(new_name)
        db[name]=k+1
        db[new_name]=1
