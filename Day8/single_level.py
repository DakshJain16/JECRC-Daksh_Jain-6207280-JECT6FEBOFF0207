## Inheritance

'''
1. Single Level - we will have a single parent & child class. Also the properties will be derived only one time
2. Multi-level
3. Multiple
4. Hierarchical
5. Hybrid
'''

## Parent class or Super Class
## The class from which we are going to derive the properties, is known as Parent class
class Parent:
    bank_balance = '54L'
    def __init__(self, members):  ## Parent constructor
        self.members = members

    def desc(self):
        print('I am the parent class')

## Child class or Sub class
## The class in which we are going to derive the properties, is known as Child class

class Child(Parent):
    def __init__(self, child_name, *args):  ## child constructor
        self.child_name = child_name
        super().__init__(args)    #---> constructor chaining

    def display(self):  
        super().desc()    #---> method chaining

# obj = Child()
# print(obj.bank_balance)
# obj.desc()

obj = Child('Raj', 'Mom', 'Dad')
print(obj.members)
print(obj.child_name)
obj.display()

## constructor chaining: Calling parent class's constructor from inside child class's constructor is k/a constructor chaining
