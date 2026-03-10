'''
Abstraction:
    Hiding the internal implementation and showing only functionality to the 
    end user.

Abstract Method:
    If a method/function consists of only declaration not dsefinition then it will
    be called as "Abstract Method".

Abstract Class:
    If a class consists of atleast one abstract method then it will be called as 
    "Abstract class".

Concrete Class:
    It consists of zero(0) abstract method

abc: Module
ABC: Abstract Base Class
'''

from abc import ABC, abstractmethod

class ATM(ABC):
    @abstractmethod
    def generate_pin(self):
        pass

    @abstractmethod
    def forget_pin(self):
        pass

    @abstractmethod
    def check_bal(self):
        pass

    @abstractmethod
    def withdraw(self):
        pass

    @abstractmethod
    def deposit(self):
        pass

class SBI_ATM(ATM):
    def generate_pin(self):
        print('It is used to generate ATM pin!')

    def forget_pin(self):
        print('Not able to remember the pin! Then forget now!')

    def check_bal(self):
        print('No balance is there in your account :(')

    def deposit(self):
        print('Save your money by giving it to me!')

    def withdraw(self):
        print('Do not withdraw the money! Please!')

obj = SBI_ATM()
obj.generate_pin()
obj.forget_pin()
obj.check_bal()
obj.withdraw()
obj.deposit()