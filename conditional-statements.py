a=13

if a > 10:
    print("a is greater than 10")
elif a == 10:
    print("a is equal to 10")
else:
    print("a is less than 10")


num_1 = int(input("Enter number 1:"))
num_2= int(input("Enter number 2:"))

if num_1 > num_2:
    print(f"{num_1} is greater than {num_2}")
elif num_1 == num_2:
    print(f"{num_1} is equal to {num_2}")
else:
    print(f"{num_1} is less than {num_2}")

gender = input("Enter your gender:")
if gender == "male":
    print("Good morning sir")
elif gender == "female":
    print("Good morning maam")
else:
    print("Good morning")


natural_number = int(input("Enter a natural number:"))
if natural_number % 2 == 0:
    print("Natural number is even")
else:
    print("Natural number is odd")

# Taking input in one line, separated by a comma
name, age = input("Enter your name and age (separated by comma): ").split(",")

# Converting age to integer and stripping whitespace from name just in case
if int(age) >= 18:
    print(f"{name.strip()} is eligible for voting")
else:
    print(f"{name.strip()} is not eligible for voting")

year =int(input("Enter your year:"))
if year % 100 == 0 and year % 400==0:
    print("Leap year")
elif year %4 == 0:
    print("Leap year")
else:
    print("Not a leap year")


temperature = int(input("Enter temperature:"))
if temperature >= 30:
    print("It's hot")
elif temperature >= 20:
    print("It's warm")
elif temperature >= 10:
    print("It's cold")
else:
    print("It's very cold")