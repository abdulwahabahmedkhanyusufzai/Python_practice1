d={}

for i in range(5):
    key = input("Enter key:")
    value = input("Enter value:")
    d[key] = value

print(d)

d1={10:100,20:200,30:300,20:200,30:300}
d2={12:24,13:26,14:28}
d1.update(d2)
print(d1)

for i in d2:
    if i in d1.keys():
        d1[i] = d1[i] + d2[i]
    else:
        d1[i] = d2[i]
print(d1)