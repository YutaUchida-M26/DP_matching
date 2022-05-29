a = input("Input 1st str:")
b = input("Input 2nd str:")
c = []
d = []
path = []
print(len(a),len(b))

for i in range(len(a) + 1):
    for j in range(len(b) + 1):
        c.append(0)
    d.append(c)
    c = []
    
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            d[i+1][j+1] = d[i][j] + 1
            print(a[i])
        else:
            d[i+1][j+1] = max(d[i+1][j], d[i][j+1])
            
i = len(a)
j = len(b)
while(i != 0 and j != 0):
    if d[i][j] > d[i-1][j-1] and d[i][j] > d[i][j-1] and d[i][j] > d[i-1][j]:
        path.append([(i-1),(j-1)])
        i -= 1
        j -= 1
    elif d[i][j] > d[i][j-1]:
        i -= 1
    elif d[i][j] > d[i-1][j]:
        j -= 1
    else:
        i -= 1
        j -= 1
for n in d:
    print(n)

print(path)
i = len(path) -1
while(i >= 0):
    print(a[path[i][0]])
    i-=1
#なんじ、ぶんがくとかがくのちからをしんじよ
#じょうほうぶんせきしてかいぜんあくしょん