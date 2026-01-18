name = "Abdul Wahab Khan"
for i in name:
    if i == "a":
        continue
    print(i)

n = int(input("Enter a number:"))
for i in range(1,n+1):
    print("Hello World")

for i in range(1,n+1):
    print(i)

for i in range(n,(n*10)+1,n):
    print(i)

sum = 0
for i in range(1,n+1):
    sum += i
print(sum)

fact = 1
for i in range(1,n+1):
    fact *= i
print(fact)

sum_odd = 0
for i in range(1,n+1,2):
    sum_odd += i
print(sum_odd)

sum_even = 0
for i in range(2,n+1,2):
    sum_even += i
print(sum_even)