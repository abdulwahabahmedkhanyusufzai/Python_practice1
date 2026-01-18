nums = [1,2,3,4,5,6,7,8,9,10]
print(nums[0:2])

for i in nums:
    print(i)

l=[21,321,584,12,132,122]
largest = l[0]
second_largest = l[0]
for i in range(len(l)):
    if l[i] > largest:
        second_largest = largest
        largest = l[i]
print(largest)
print(second_largest)
    