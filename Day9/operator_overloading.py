'''
-- Operator Overloading: It is a phenomenon of making the operators to work on user-defined data types
by invoking respective magic methods.

-- Magic Method/Dundar: It is a special type of method in which double underscores will be there at the starting & ending 
of the method's name. 
-- Example:
    1. __add__
    2. __sub__
    3. __mul__
    4. __floordiv__
    5. __truediv__
    6. __mod__

-- If we don't use operator overloading then what will happen?
    For using the operators inside user-defined data types we have to use operator overloading.

-- Syntax:
    class ClassName:
    def __init__(self, val):
        self.val = val

    def __add__(self, ano_obj):
        return self.val + ano_obj.val

    obj1 = ClassName(val1)
    obj2 = ClassName(val2)
    print(obj1 + obj2)  ## obj1.__add__(obj2)
'''

class MyDT:
    def __init__(self, val):
        self.val = val
    
    # def __add__(self, *ano_obj):
    #     return self.val + ano_obj.val
    
    def __str__(self):
        return str(self.val)
    
    def __add__(self, *ano_obj):
        sum = self.val
        for i in ano_obj:
            sum += i.val
        return MyDT(sum)
    
    # def add(self, *args):
    #     sum = self.val
    #     for i in args:
    #         sum += i.val
    #     return sum

    # def __sub__(self, ano_obj):
    #     return self.val - ano_obj.val

    def __sub__(self, *ano_obj):
        sum = self.val
        for i in ano_obj:
            sum -= i.val
        return MyDT(sum)
    
    # def sub(self, *args):
    #     diff = self.val
    #     for i in args:
    #         diff -= i.val
    #     return diff
    
    # def __mul__(self, ano_obj):
    #     return self.val * ano_obj.val
    
    def __mul__(self, *ano_obj):
        sum = self.val
        for i in ano_obj:
            sum *= i.val
        return MyDT(sum)
    
    # def mul(self, *args):
    #     prod = self.val
    #     for i in args:
    #         prod *= i.val
    #     return prod
    
    def __floordiv__(self, ano_obj):
        return self.val // ano_obj.val
    
    def floordiv(self, *args):
        quo = self.val
        for i in args:
            quo //= i.val
        return quo
    
    def __truediv__(self, ano_obj):
        return self.val / ano_obj.val
    
    def truediv(self, *args):
        quo = self.val
        for i in args:
            quo /= i.val
        return quo
    
    def __mod__(self, ano_obj):
        return self.val % ano_obj.val
    
    def mod(self, *args):
        rem = self.val
        for i in args:
            rem %= i.val
        return rem

   
# print(MyDT(10) + MyDT(20))
# print(MyDT(100) - MyDT(20))
# print(MyDT(10) * MyDT(20))
# print(MyDT(65) // MyDT(20))
# print(MyDT(102) / MyDT(20))
# print(MyDT(85) % MyDT(20))

# print(MyDT.add(MyDT(100), MyDT(200), MyDT(300), MyDT(400), MyDT(500)))
# print(MyDT.sub(MyDT(500), MyDT(200), MyDT(100), MyDT(50), MyDT(100)))
# print(MyDT.mul(MyDT(5), MyDT(2), MyDT(4), MyDT(3), MyDT(10)))
# print(MyDT.floordiv(MyDT(50), MyDT(2), MyDT(3), MyDT(2), MyDT(3)))

print(MyDT(10) + MyDT(20) + MyDT(30))
print(MyDT(60) - MyDT(20) - MyDT(10))
print(MyDT(60) * MyDT(20) * MyDT(10))