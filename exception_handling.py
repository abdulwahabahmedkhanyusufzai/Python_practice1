a = int(input("Enter a number:"))
b = int(input("Enter a number:"))
try:
    print(a/b)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")
else:
    print("No error")
finally:
    print("This is always executed")