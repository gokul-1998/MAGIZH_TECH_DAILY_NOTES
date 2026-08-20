accounts = [[1,5],[7,3],[3,5]]

print(len(accounts))

max=0 # 10
for i in accounts:
    if sum(i)>max:#  8>10
        max=sum(i)
print(max)