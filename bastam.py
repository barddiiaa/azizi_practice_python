x = "1413132355234"
m = []
for i in x:
    m.append(i)
l = len(m)

for i in range(1-3,0,-3):
    print (i)
    m.insert(i,"/")

s ="".join(m)

print(s)
