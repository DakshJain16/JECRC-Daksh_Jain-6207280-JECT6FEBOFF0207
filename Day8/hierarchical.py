'''
It is a type of inheritance in which the properties will be derieved from single parent class to
multiple child class.
'''

class Parent:
    gold = '2kg'
    silver = '10kg'
    no_of_flats = 12

class SmallestBrother(Parent):
    name = 'Rickon'

class ElderBrother(Parent):
    my_name = 'Rob'

class Sister(Parent):
    sis_name = 'Sansa'

print(SmallestBrother.gold)
print(ElderBrother.silver)
print(Sister.no_of_flats)