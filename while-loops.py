import random

a=int(input("Enter a number:"))
b = int(input("Enter a number:"))
while a>0:
    digits = a % 10
    a //= 10
    print(digits,end=" ")

reverseNum = 0
while b>0:
    digits = b % 10
    b //= 10
    reverseNum = reverseNum * 10 + digits

print(reverseNum)

c = int(input("Enter a number:"))
reverseNum = 0
originalNumber = c
while c>0:
    digits = c % 10
    c //= 10
    reverseNum = reverseNum * 10 + digits
if reverseNum == originalNumber:
    print("Palindrome")
else:
    print("Not a palindrome")

num = random.randint(1,10)
tries = 0
while True:
    guess = int(input("Guess the number:"))
    tries += 1
    if guess < num:
        print("Too low")
    elif guess > num:
        print("Too high")
    else:
        print("You guessed it right")
        break
print(f"You guessed it right in {tries} tries")