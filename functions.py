def hello_world():
    print("Hello World")

hello_world()

def sum(a,b=20):
    return a+b

print(sum(10))

def palindrome(st):
    rev_str = ""
    for i in range(len(st)-1,-1,-1):
        rev_str += st[i]
    if rev_str == st:
        return True
    else:
        return False

print(palindrome("madam"))