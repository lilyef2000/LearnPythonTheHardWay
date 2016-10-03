#!/usr/bin/python  
# -*- coding: utf-8 -*-  

## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Make a class named Dog that is-a Animal, and it has-a __init__ that takes self and name parameters
class Dog(Animal):
    def __init__(self, name):
        ## From self get the name attribute and set it to name.
        self.name = name
        
## Make a class named Cat that is-a Animal, and it has-a __init__ that takes self and name parameters
class Cat(Animal):
    def __init__(self, name):
        ## From self get the name attribute and set it to name.
        self.name = name

## Make a class nemed Person, and it has-a __init__ that takes self and name parameters
class Person(object):
    def __init__(self, name):
        ## From self get the name attribute and set it to name.
        self.name = name
        ## Person has-a pet of some kind and set it to None
        ## the self.pet attribute of that class is set to a default of None
        self.pet = None

## Make a class named Employee that is-a Person, and it has-a __init__ that takes self,name,and salary parameters
class Employee(Person):
    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        ## 首先找到Employee的父类（即类Person），然后把类Employee的对象self转换为类Person的对象，然后“被转换”的类Person对象调用自己的__init__函数
        super(Employee, self).__init__(name)
        ## Employee has-a salary and set it to salary
        self.salary = salary

## Make a class named Fish
class Fish(object):
    pass

## Make a class named Salmon that is-a Fish.
class Salmon(Fish):
    pass

## Make a class named Halibut that is-a Fish.
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")
## Set satan to an instance of class Cat with parameter "Rover".
satan = Cat("Satan")
## mary is-a Person
mary = Person("Mary")
## From mary get the pet attribute and set it to satan
mary.pet = satan
## Set frank to an instance of class Employee with parameter "Frank" and 120000
frank = Employee("Frank", 120000)
## From frank get the pet attribute and set it to rover
frank.pet = rover
## Set flipper to an instance of class Fish
flipper = Fish()
## Set crouse to an instance of class Salmon
crouse = Salmon()
## Set harry to an instance of class Halibut
harry = Halibut()