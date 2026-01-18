class Factory:
    # FIX: Add parameters here so __init__ can receive data
    def __init__(self, name="Factory", price=100, color="Red"):
        self.name = name   # Connect input to memory
        self.price = price
        self.color = color

    def __str__(self):
        return f"Factory: {self.name}, Price: {self.price}, Color: {self.color}"
    
    @classmethod
    def factory(cls, name, price, color):
        # Now this works because __init__ expects these 3 values
        return cls(name, price, color)

    @staticmethod
    def static_method():
        print("This is a static method")
    
    def add(self,*args):
        return sum(args)
    
    def sub(self,**kwargs):
        return kwargs["a"]-kwargs["b"]

    divison = lambda self,a,b: a/b

    l = [x*x for x in range(10)]

    result = filter(lambda x: x%2==0,l)
    print(list(result))

    result2 = map(lambda x: x*x,l)
    print(list(result2))




class KarachiFactory(Factory):
    def __init__(self, name="KarachiFactory", price=100, color="Red"):
        super().__init__(name, price, color)

class LahoreFactory(KarachiFactory):
    def __init__(self, name="LahoreFactory", price=100, color="Red"):
        super().__init__(name, price, color)

class IslamabadFactory(LahoreFactory):
    def __init__(self, name="IslamabadFactory", price=100, color="Red"):
        super().__init__(name, price, color)


# Now this runs perfectly
my_factory = Factory.factory("SuperFactory", 9000, "Blue")
print(my_factory)
print(my_factory.add(10,20,30,40,50))
print(my_factory.sub(a=10,b=20))
print(my_factory.divison(10,20))
print(my_factory.l)
# Now this runs
