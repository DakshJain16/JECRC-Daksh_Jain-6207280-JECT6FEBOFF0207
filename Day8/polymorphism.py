# class Temp:
#     def sum(self, a, b):
#         print(a + b)
#     ## Monkey Patching
#     ## It is a process of storing the previous method's address inside a variable before overriding the 
#     ## method area's address. Using that var, we can access the prev method's method area.
#     add_two_nums = sum 

#     def sum(self, a, b, c):
#         print(a + b + c)

# obj = Temp()
# obj.sum(10, 20, 30)
# obj.add_two_nums(10, 20)


## operator overloading

class MyDataType:
    def __init__(self, val):
        self.val = val
    
    def __add__(self, ano_obj):   #-----> for operator overloading
        return self.val + ano_obj.val
    
    def __mul__(self, ano_obj):
        return self.val * ano_obj.val

obj1 = MyDataType(10)
obj2 = MyDataType(20)
print(10 + 20)
print(obj1 + obj2)
print(obj1 * obj2)