# int concatenation to string
age = 31
age += 1
my_age = 'This is my age'
print(type(age))
print(my_age + " " + str(age))
#__________________________________________________________

# float
height = 250.65
print(height)
print(type(height))
#__________________________________________________________

# boolean
human = True
print('Are you a human? -- '+str(human))
print(type(human))
#__________________________________________________________

#multile assignment
name, last_name, age = 'John',  'Smith', 87
print('Hi, my name is ' + name,  last_name + ' and I am ' +str(age) + ' old')
Spongebob = Patrick = Sandy = 30
print(Spongebob)
print(Patrick)
print(Sandy)
#__________________________________________________________

# String length, find, capitalize, upper/lower, isDigit
name = 'my Bro'
print(len(name))
print(name.find("r"))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isdigit())
print(name.isalpha())
print(name.count('o'))
print(name.replace('my', 'mine'))
print(name*3)

#__________________________________________________________

# type casting - covert the data type og a value to another data type
x = 1
y = 2.0
z = "3"
print(int(y))
print(int(z)*3)
print(float(x))

#__________________________________________________________
# Input 
name  = input("What is your name? : ")
print("Your name is  " + name)

age = int(input('How old are you? : '))
if age <= 18:
    print('You are too young')
else:
    print('Welcome, adult')


#__________________________________________________________
# import math
import math

pi = 3.14
print(round(pi))
print(math.ceil(pi))
print(math.floor(pi))
print(abs(-8))
print(pow(pi, 3))
print(math.sqrt(81))

x, y, z = 89, 120, -5
print(max(x,y,z))
print(min(x,y,z))
average = (x+y+z)/3
print(average)

#__________________________________________________________

#SLICING
# slicing - create a substring by extracting elements from another string
#       indexing[] or slice()
#      [start:stop:step]
name = "My code"
first_name = name[::6]
print(first_name)  # <--input Me

website_1 = "http://google.com"
website_2 = "http://wikipedia.com"
slice = slice(7, -4)
print(website_1[slice])  #<--google
print(website_2[slice])  #<--wikipedia

#__________________________________________________________

# WHILE LOOPS -unlimited 
name = ""
while len( name) ==0:
    name = input("Enter your name : ")
print("Hello " + name)

#__________________________________________________________
# FOR LOOP -limited

for i in range(10):
    print (i+1)

for i in range(50,100+10,10):
    print (i)
for i in "Hawai":
    print (i)


import time
from datetime import datetime
for i in range(10, 0, -1):
    print(i)
    time.sleep(1)
print("Merry Christmas!!")
now = datetime.now()
current_time = now.strftime("%H:%M")
print("Current Time =", current_time)
#__________________________________________________________

# Nested Loops - a nested loops are a general concepnt of another loop
rows = int(input("How many rows? : "))
colomns = int(input("How many colomns? : "))
symbol = input("Enter the symbol to use : ")
for r in range(rows):
    for c in range(colomns):
        print(symbol, end=" ")
    print()
#__________________________________________________________


# LOOP CONTROL STATEMENT -change a loops execution from its normal sequence
# Break = used to terminate the loop entirely
while True:
    namme = input("Enter your name: ")
    if namme != "":
        break
# Continue = skips to the next iteration of the loop
phone_number = "123-456-7899"
for i in phone_number:
    if i == "-":
        continue
    print(i, end = "")
# Pass = does nothing, acts as a placeholder
for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i, end=", ")
#__________________________________________________________

 # LIST-used to store multiple items in a single variable
food = ["pizza", "oranges", "pelemeni"] 
print(food[2])
print(food)
food.append("banana")
# food.remove('pizza')
# food.pop() - remove last element from the list
food.insert(0,'cake')
food.sort()
# food.clear()
for i in food:
    print(i)
#__________________________________________________________

# 2D LISTS -multidimention lists
drinks= ['cofee', 'soda','tea']
dinner = ['pizza', 'sushi', 'pie', 'hamburger']
desert = ['cake', 'icecream']

food = [drinks,dinner,desert]
print('desert only----> '+str(food[2][0])) #cake
for i in food:
    print (i) 
#__________________________________________________________

#Tuple - collection which is ordered and unchangable,
# used to group together related data
student = ('John', 21, 'male')
print(student.count('John')) #1
print(student.index('John')) #0
for x in student:
    print(x, end=" ")
if 'John' in student:
    print("<-------John is today in the class!")

#__________________________________________________________

# SET-collection which is unordered, unindexed.No dubæicate values
utensils = {"fork", "spoon", "knife", "knife"}
dishes = {"bowl", "plate", "cup", "fork"}
print(utensils.intersection(dishes), '<----common element')
print('Differences , print what utensilshas and dishes havent -->')
print(utensils.difference(dishes))

utensils.add('pica cutter')
utensils.remove("knife")
# utensils.update(dishes)
# for x in utensils:
#     print(x)
dinner_table = utensils.union(dishes)
for x in dinner_table:
    print(x)
#__________________________________________________________


# DICTIONARIES
# A changeable, unordered collection of unique key:value pairs
# Fast because they use hashing, allow us to access a value quickly
capitals = {'USA': 'Washington DC',
            'India': 'New Deli',
            'China': 'Beijing',
            'Russia': 'Moscow'}
# print(capitals.values(), '<---all values')
# print(capitals.get('India'), '-----India only, using get')
# print(capitals.get('Germany'), '-----Germany, which is not in the dictionary')
# print(capitals['Russia'], '-----Russia only, using []')
# print(capitals.keys(), '----keys')
print(capitals.items(), '----items, (key-value)')
capitals.update({'Germany':'Berlin'})
capitals.update({'USA':'Las Vegas'})
capitals.pop('China')
# capitals.clear()
for key, value in capitals.items():
    print(key + '--' + value)
#__________________________________________________________

# INDEX OPERATOR [] -gives access to a sequence's element (str, list, tuples)
name = "john Smith!"
if name[0].islower():
    name = name.capitalize()
print(name)
first_name = name[:4].upper()
print(first_name)
last_name = name[5:10].lower()
print(last_name)
last_character = name[-1]
print(last_character)

#__________________________________________________________

# FUNCTOIN - a block of code which is executed only when it is called
def my_function(name):
    print("Dear " + name.upper() + ", hello from a function")

my_function('John')
#__________________________________________________________

# RETUNRN STATEMENT-funct send values/obj back to the caller
# These val/obj are knows as the funct return value
def multiply(x,y):
    return (x*y)
result = multiply(60,29)
print(result)
#__________________________________________________________

# Keyord arguments -arguments preceded by an identifier whe we pass them to a func
#The order of the arguments does't matter, unlike positional arguments 
#Python knows the name od the arguments that our func receives

def hello(first,middle,last):
    print("Hello "+first+" "+middle+" "+last)


hello(last="Knudsen",middle="Lars",first="Mr")
#__________________________________________________________

# NESTED FUNCTIONS CALLS =  function calls inside other function calls
                          innermost function calls are resolved first
                          returned value is used as argument for the next outer function

# num = input("Enter a whole positive number: ")
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)

print(round(abs(float(input("Enter a whole positive number: "))))) #-78.56-->79
#__________________________________________________________


# SCOPE = The region that a variable is recognized
        A variable is only available from inside the region it is created.
        A global and locally scoped version of a variable can be created

name = "Johny" # global scope (available inside & outside functions)

def display_name():
    name = "Depp"    # local scope (available only inside this function)
    print(name)


display_name()
print(name)
#__________________________________________________________

#*args =   parameter that will pack all arguments into a tuple
               useful so that a function can accept a varying amount of arguments

def add(*stuff):
    sum=0
    stuff = list(stuff)
    stuff[0]=0
    for i in stuff:
        sum +=i
    return sum
# def add(*args):
#     total = 0
#     for val in args:
#         total+=val
#     return total
print(add(1,2,3,4,5,6))


print(("nested functions calls ").upper())
#__________________________________________________________
# **kwargs =   parameter that will pack all arguments into a dictionary
#                     useful so that a function can accept a varying amount of keyword arguments

def hello(**kwargs):
    #print("Hello " + kwargs['first'] + " " + kwargs['last'])
    print("Hello",end=" ")
    for key,value in kwargs.items():
        print(value,end=" ")


hello(title="Mr.",first="John",middle="William",last="Smith")
def person(**kwargs):
    print("Here is a person", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")
person(name="Janis", surname="Freimanis", age=25)
#__________________________________________________________

#str.format() =    optional method that gives users
 #                 more control when displaying output

animal = "cow"
item = "moon"

print("The "+animal+" jumped over the "+item)

# {} = format field
print("The {} jumped over the {}".format("cow","moon"))
print("The {0} jumped over the {1}".format(animal,item)) # positional arguments
print("The {animal} jumped over the {item}".format(animal="cow",item="moon"))   # keyword arguments

text = "The {} jumped over the {}"
print(text.format("cow","moon"))

name = "Bro"

print("My name is {}".format(name))
print("My name is {:10}".format(name,name))   # amount of padding
print("My name is {:<10}".format(name,name))  # < = left align
print("My name is {:>10}".format(name,name))  # > = right align
print("My name is {:^10}".format(name,name))  # ^ = center align


#str.format() =    optional method that gives users
#                  more control when displaying output

number = 1000

print("The number pi is {:.3f}".format(number))
print("The number is {:,}".format(number))
print("The number is {:b}".format(number))
print("The number is {:o}".format(number))
print("The number is {:X}".format(number))
print("The number is {:E}".format(number))

#__________________________________________________________

#  random numbers 
import random

x = random.randint(1,6)
y = random.random()
print(random.randint(1,6))
print(random.random()) #between 0 and 1

myList = ['rock','paper','scissors']
z = random.choice(myList)
print(z)

cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
random.shuffle(cards)
print(cards)
#__________________________________________________________

# exception =   events detected during execution that interrupt the flow of a program

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero! idiot!")
except ValueError as e:
    print(e)
    print("Enter only numbers plz")
except Exception as e:
    print(e)
    print("something went wrong :(")
else:
    print(result)
finally:
    print("This will always execute")
#__________________________________________________________

#---------------------ALL ABOUT FILES---------------------------------

# FILE DETECTION
import os

path = "C:\\Users\\ebazi\\Dropbox\\My PC (DESKTOP-R3B1CDB)\\Desktop\\learn_py"
if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory!")
else:
    print("That location doesn't exist!")
#__________________________________________________________

# READ A FILE
try:
    with open('test.txt') as file:
        print(file.read())
    print(file.closed) #<---TRUE
except FileNotFoundError as e:
    print(e)
#__________________________________________________________

# WRITE FILES
text = "I am writting in the file!\n I am the BOSS\n"
# overwrite all text in the file
with open('test.txt', 'w') as file:
    file.write(text)

# append/add the file data
with open('test.txt', 'a') as file:
    file.write(text)

#__________________________________________________________

# COPY FILES IN PYTHON
# copyfile() =  copies contents of a file
# copy() =      copyfile() + permission mode + destination can be a directory
# copy2() =     copy() + copies metadata (file’s creation and modification times)

import shutil

shutil.copyfile('test.txt','copy.txt') #src,dst

#__________________________________________________________

# MOVE FILES 
import os

source = 'copy.txt'
destination = 'C:\\Users\\ebazi\\Dropbox\\My PC (DESKTOP-R3B1CDB)\\Desktop\\learning_python .txt'
try:
    if os.path.exists(destination):
        print('there is already exists that file')
    else:
        os.replace(source, destination)
        print(source + ' was moved')
except FileNotFoundError as e:
    print(e)
    print(source + ' was not found')
#__________________________________________________________

# MOVE FILES
import os
import shutil
path = 'empty_folder'
try:
   # os.remove(path) # for a file
   # os.rmdir(path) # delete en ampty directory
   shutil.rmtree(path) #delete a directory and all files in it
except FileNotFoundError:
    print('That file was not found')
except PermissionError :
    print('You do not have a permission to defete the folder')
except OSError:
    print('You cannot delete that using that function')
else:
    print(path + '  was deleted')
#__________________________________________________________

# BASIC GAME -ROCK, PAPER, SCISORS
import random

while True:
    choices = ["rock","paper","scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, or scissors?: ").lower()

    if player == computer:
        print("computer: ",computer)
        print("player: ",player)
        print("Tie!")

    elif player == "rock":
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")

    elif player == "scissors":
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")

    elif player == "paper":
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")

    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        break

print("Bye!")
#__________________________________________________________

# # QUIZ GAME
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1
    for key in questions:
        print('-----------------------------------------------')
        print(key)
        for i in options[question_num - 1]:
            print(i)
        guess = input('Enter (A, B, C or D):  ')
        guess = guess.upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key), guess)
        question_num = +1
    display_score(correct_guesses, guesses)


def check_answer(answer, guess):
    if answer == guess:
        print('correct')
        return 1
    else:
        print('wrong')
        return 0


def display_score(correct_guesses, guesses):
    print('........................................')
    print('RESULTS')
    print('........................................')

    print('Answers:  ', end='')
    for i in questions:
        print(questions.get(i), end='')
    print()
    print('Guesses:  ', end='')
    for i in guesses:
        print(i, end='')
    print()
    score = int((correct_guesses / len(questions)) * 100)
    print('Your score is: {0}%'.format(str(score)))


def play_again():
    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()
    if response == "YES":
        return True
    else:
        return False


# #dictionary for hold all questions with correct answers
questions = {
    "Who created Python?: ": "A",
    "What year was Python created?: ": "B",
    "Python is tribute to which comedy group?: ": "C",
    "Is the Earth round?: ": "A"
}
# # A list od the lists with the answers options
options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerberg"],
           ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
           ["A. True", "B. False", "C. sometimes", "D. What's Earth?"]]

new_game()
while play_again():
    new_game()

print("Byeeeeee!")
#__________________________________________________________

# Object Oriented Programming (POOP)
from car import Car

car_1 = Car('Chevy', 'Corvette', 2021, 'blue')
car_2 = Car('Ford', 'Mustang', 2022, 'black')
# print(car_2.make, car_2.model, car_2.year, car_2.color)
car_1.drive()
car_2.stop()
print(car_1.wheels)
print('All cars have  {0} wheels'.format(Car.wheels))
#__________________________________________________________

# Inheritance (receive/derive/inherit)
class Animal:
    alive = True

    def eat(self):
        print('This animal is eating')

    def sleep(self):
        print('This animal is sleeping')


class Rabbit(Animal):
    def run(self):
        print('This rabbit is running')


class Fish(Animal):
    def swim(self):
        print('This fish is swimming')


class Hawk(Animal):
    def fly(self):
        print('This hawk is flying')


rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
fish.eat()
hawk.sleep()

rabbit.run()
fish.swim()
hawk.fly()
#__________________________________________________________


# MULTILEVEL INHERITANCE (derived class inherits from the derived class)
# EX 1
class Organism:
    alive = True
class Animial(Organism):
    def eat(self):
        print('This animal is eating')
class Dog(Animial):
    def bark(self):
        print("All dogs bark")
dog = Dog()
print(dog.alive) #from organism
dog.eat() #from animal
dog.bark() #from dog

# EX 2
class Prey:
    def flee(self):
        print('This animal flees')
class Predator:
    def hunt(self):
         print('This animal is hunting')
class  Fish(Prey, Predator):
    def swim(self):
        print('This animal is swimming')
    def flee(self):  # METHOD Prey overriding 
        print("fish don't really flee")
fish =Fish()

fish.flee()
fish.hunt()
fish.swim()

#__________________________________________________________

# METHOD Chaining - calling multiple methods sequentially
class Car:

    def turn_on(self):
        print("You start the engine")
        return self

    def drive(self):
        print("You drive the car")
        return self

    def brake(self):
        print("You step on the brakes")
        return self

    def turn_off(self):
        print("You turn off the engine")
        return self


car = Car()

# car.turn_on().drive()
# car.brake().turn_off()
#car.turn_on().drive().brake().turn_off()

car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()

#__________________________________________________________

# SUPER FUNCTION 
# super() = Function used to give access to the methods of a parent class.
#                  Returns a temporary object of a parent class when used
class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):

    def __init__(self, length, width):

        super().__init__(length,width)  #SUPER!!!!

    def area(self):
        return self.length*self.width

class Cube(Rectangle):

    def __init__(self, length, width, height):
        super().__init__(length,width)  #SUPER!!!!
        self.height = height

    def volume(self):
        return self.length*self.width*self.height


square = Square(3, 3)
cube = Cube(3, 3, 3)

print(square.area())
print(cube.volume())

#__________________________________________________________

# ABSTRACT CLASSES
# Prevents a user from creating an object of that class
# + compels a user to override abstract methods in a child class

# abstract class = a class which contains one or more abstract methods.
# abstract method = a method that has a declaration but does not have an implementation.
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print("You drive the car")

    def stop(self):
        print("This car is stopped")

class Motorcycle(Vehicle):

    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("This motorcycle is stopped")


#vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

#vehicle.go()
car.go()
motorcycle.go()

#vehicle.stop()
car.stop()
motorcycle.stop()

#__________________________________________________________

# PASS OBJECTS AS ARGUMENTS
class Car:
    color = None
class Motorcycle:
    color = None
def change_color(vehicle, color):
    vehicle.color = color
car_1= Car()
car_2= Car()
car_3= Car()
moto = Motorcycle()
change_color(car_1,'red')
change_color(car_2,'green')
change_color(car_3,'blue')
change_color(moto, "black")
print(car_1.color)
print(car_2.color)
print(car_3.color)
print(moto.color)
#__________________________________________________________

# # duck typing = concept where the class of an object is less important than the methods/attributes
#               class type is not checked if minimum methods/attributes are present
#               “If it walks like a duck, and it quacks like a duck, then it must be a duck.”
class Duck:

    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("This duck is qwuacking")

class Chicken:

    def walk(self):
        print("This chicken is walking")

    def talk(self):
        print("This chicken is clucking")

class Person():

    def catch(self, duck):  #!!!!!as long as it has same atributes!!!!!!!!!!
        duck.walk()
        duck.talk()
        print("You caught the critter!")


duck = Duck()
chicken = Chicken()
person = Person()

person.catch(chicken) #!!!!!!!!!!!!!!!

#__________________________________________________________

# WALRUS OPERATOR :=
# new to Python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression

happy = True
print(happy) #--->

print(happy:=True)


foods = list()
while True:
  food = input("What food do you like?: ")
      if food == "quit":
          break
  foods.append(food) #---->

foods =list()
while food:=input("What food do you like?:  ") != 'quit':
    foods.append(food)

#__________________________________________________________

# ASSIGN FUCTIONS TO VARIABLES
# assignintg the memory adress
def hello():
    print('hello')
hello()
hi = hello
print(hi)
hi()

say = print
say('aloha')

#__________________________________________________________

# HIGHER ORDER FUNCTION
 #  Higher Order Function =  a function that either:
#                           1. accepts a function as an argument
#                               or
#                           2. returns a function
#                           (In python, functions are also treated as objects)
def loud(text):
    return text.upper()
def quiet(text):
    return text.lower()
def hello(func):
    text = func('Hello')
    print(text)
hello(loud)
hello(quiet)
#----dividend/divisor=quotient----#
def divisor(x):
    def divident(y):
        return y/x
    return divident
divide =divisor(5)
print(divide(125))
#__________________________________________________________

# LAMBDA FUNCTION = function written in 1 line using lambda keyword
#                   accepts any number of arguments, but only has one expression.
#                   (think of it as a shortcut)
#                   (useful if needed for a short period of time, throw-away)
#
# lambda parameters:expression
def double(x):
    return x*2
print(double(5)) # OR

double = lambda x: x * 2
print(double(10))

multiply = lambda x, y, z: x * y * z
print(multiply(125, 5, 10))

full_name = lambda first_name, last_name: first_name + ' ' + last_name
print(full_name('John', 'Smith'))

age_check = lambda age: True if age >= 18 else 'you are not allowed'
print(age_check(21))
#__________________________________________________________

# SORT METHOD -return a sorted list
# sort() method = used with lists
# sort () functions = used with iterables
# Ex1
students = ["Sandy", 'Lizzy', 'Craig', 'Eliah', 'Sara', 'Anna']
sorted_students  = sorted(students, reverse=True)
# students.sort(reverse=True) # reverse alphabetical 
for s in sorted_students:
    print(s)
# Ex2
students = [("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick", "D", 36),
            ("Spongebob", "B", 20),
            ("Mr.Grabs", "C", 78)]
# grade = lambda grades: grades[1]
# students.sort(key=grade)  # , reverse=True
age = lambda ages: ages[2]
students.sort(key=age)  # , reverse=True
for i in students:
    print(i)

# Ex3 tuple of tuples
students = (("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick", "D", 36),
            ("Spongebob", "B", 20),
            ("Mr.Grabs", "C", 78))
age = lambda ages:ages[2]
sorted_students = sorted(students, key=age)
for i in sorted_students:
    print(i)
#__________________________________________________________
# map() =   applies a function to each item in an iterable (list, tuple, etc.)
#
# map(function,iterable)
store = [("shirt",20.00),
         ("pants",25.00),
         ("jacket",50.00),
         ("socks",10.00)]
to_euros = lambda data: ( data[0],data[1]*0.82)
store_euros = map(to_euros, store)
for s in store_euros:
    print(s)
# to_dollars = lambda data: ( data[0],data[1]/0.82)
# store_dollars = map(to_dollars, store)
# for s in store_dollars:
#     print(s)


#__________________________________________________________

# FILTER()
# filter() =    creates a collection of elements from an iterable,
#               for which a function returns true
#
#               filter(function, iterable)

friends = [("Rachel",19),
           ("Monica",18),
           ("Phoebe",17),
           ("Joey",16),
           ("Chandler",21),
           ("Ross",20)]
age = lambda data: data[1]>=18
drinking_friends = list(filter(age,friends))
for i in drinking_friends:
    print(i)

#__________________________________________________________

# REDUCE()
# reduce() = apply a function to an iterable and reduce it to a single cumulative value.
#            performs function on first two elements and repeats process until 1 value remains
#
# reduce(function, iterable) like recycling

import functools

letters = ["H","E","L","L","O"]
word = functools.reduce(lambda x,y: x+y,letters)
print(word)

numbers = [1,2,3,4,5]
factorial = functools.reduce(lambda x,y:x*y, numbers)
print(factorial)
#__________________________________________________________

# LIST COMPREHENSION
# list comprehension =  a way to create a new list with less syntax
#                       can mimic certain lambda functions, easier to read
#                       list = [expression for item in iterable]
#                       list = [expression for item in iterable if conditional]
#                       list = [expression (if/else) for item in iterable]

# EX1
squares= [] #create an empty list
for i in range(1,11): #create a for loop 
    squares.append(i*i) #define what each loop iteraction should do
print(squares)
  # --or--
squares = [i*i for i in range(1,11)]
print(squares)

# EX2
students = [100,90,80,70,60,50,40,30,0]

# passed_students = list(filter(lambda i : i>=60,students))
# print(passed_students)
#   # --or--
passed_students = [i for i in students if i>=60]
passed_students = [i if i>=60 else "FAILED" for i in students]
# [100, 90, 80, 70, 60, 'FAILED', 'FAILED', 'FAILED', 'FAILED']
print(passed_students)

#__________________________________________________________
# DICTIONARY COMPREHENSION
# dictionary comprehension = create dictionaries using an expression
#                            can replace for loops and certain lambda functions
#
# dictionary = {key: expression for (key,value) in iterable}
# dictionary = {key: expression for (key,value) in iterable if conditional}
# dictionary = {key: (if/else) for (key,value) in iterable}
# dictionary = {key: function(value) for (key,value) in iterable}

cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
cities_in_C = {key: round((value-32)*(5/9)) for(key,value) in cities_in_F.items()}
print(cities_in_C)

weather = {'New York': "snowing", 'Boston': "sunny", 'Los Angeles': "sunny", 'Chicago': "cloudy"}
sunny_weather ={key:value for (key,value) in weather.items() if (value =="sunny")}
print(sunny_weather)

cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
desc_cities = {key: ('WARM' if value>=40 else 'COLD') for (key,value) in cities.items()}
print(desc_cities)

def check_temp(value):
    if value >= 70:
        return "HOT"
    elif 69 >= value >= 40:
        return "WARM"
    else:
        return "COLD"


cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
desc_cities = {key: check_temp(value) for (key,value) in cities.items()}
print(desc_cities)
#__________________________________________________________

# ZIP FUNCTIONS
zip(*iterables) =  aggregate elements from two or more iterables (list, tuples, sets, etc.)
                   creates a zip object with paired elements stored in tuples for each element

usernames = ["Dude", "Bro", "Mister"]
passwords = ("p@ssword", "abc123", "guest")
login_dates = ["1/1/2021","1/2/2021","1/3/2021"]

users = list(zip(usernames,passwords))
print(type(users))
for x in users:
    print(x)
#--------------------------------- 
users = dict(zip(usernames,passwords))
print(type(users))
for key,value in users.items():
    print(key + " : "+ value)
#--------------------------------- 
users =zip(usernames,passwords,login_dates)
for i in users:
    print(i)

#__________________________________________________________

# ***********************************
# if __name__ == '__main__'
# ***********************************

# y tho?
# 1. Module can be run as a standalone program
#    or
# 2. Module can be imported and used by other modules

#  Python interpreter sets "special variables", one of which is __name__
#  Python will assign the __name__ variable a value of '__main__' if it's
#  the initial module being run
if __name__ == '__main__':
    print(__name__)

#__________________________________________________________
# IMPORT TIME
import time

print(time.ctime(0))    # convert a time expressed in seconds since epoch to a readable string
#                                        epoch = when your computer thinks time began (reference point)
print(time.time())      # return current seconds since epoch
print(time.ctime(time.time())) # will get current time


***************************************************************************
time_object = time.localtime()
print(time_object)
# time.strftime(format, time_object) # # = formats a time_object to a string
time_object = time.localtime()  # # local time
time_object = time.gmtime()  # # UTC time
local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
print(local_time)

***************************************************************************
# time.strptime(string_string, format) = parses a string representing time/date and returns a struct_time object
time_string = "20 April, 2020"
time_object = time.strptime(time_string,"%d %B, %Y")
print(time_object)

***************************************************************************
# time.asctime(time_tuple) = accepts a time_object or a tuple up to 9 elements and returns a string
# (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.asctime(time_tuple)
print(time_string)

***************************************************************************
# time.asctime(time_tuple) = accepts a time_object or a tuple up to 9 elements and return seconds since epoch
# (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.mktime(time_tuple)
print(time_string)


#__________________________________________________________

# THREAD
# thread =  a flow of execution. Like a separate order of instructions.
#                  However each thread takes a turn running to achieve concurrency
#                  GIL = (global interpreter lock),
#                  allows only one thread to hold the control of the Python interpreter at any one time

# cpu bound = program/task spends most of it's time waiting for internal events (CPU intensive)
#             use multiprocessing

# io bound = program/task spends most of it's time waiting for external events (user input, web scraping)
#            use multithreading

import threading
import time


# print(threading.active_count())
# print(threading.enumerate()) # [<_MainThread(MainThread, started 16800)>]
def eat_breakfast():
    time.sleep(3)
    print("You ate breakfast")


def drink_coffee():
    time.sleep(4)
    print("You drank coffee")


def study():
    time.sleep(5)
    print("You finish studying")


x = threading.Thread(target=eat_breakfast, args=())
x.start()
y = threading.Thread(target=drink_coffee, args=())
y.start()
z = threading.Thread(target=study, args=())
z.start()
x.join()
y.join()
z.join()
# eat_breakfast()
# drink_coffee()
# study()
print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())
#__________________________________________________________

# DAEMON THREAD
# daemon thread = a thread that runs in the background, not important for program to run
#                 your program will not wait for daemon threads to complete before exiting
#                 non-daemon threads cannot normally be killed, stay alive until task is complete
#
#                 ex. background tasks, garbage collection, waiting for input, long running processes
import threading
import time

def timer():
    print()
    count=0
    while True:
        time.sleep(1)
        count += 1
        print("logged in for: ", count, "seconds")
x = threading.Thread(target=timer, daemon = True)
x.start()
# # x.setDaemon(True)
# # print(x.isDaemon)
answer = input("Do you wish to exit?")
#__________________________________________________________

# MULTIPROCESSING
# multiprocessing = running tasks in parallel on different cpu cores, bypasses GIL used for threading
#                   multiprocessing = better for cpu bound tasks (heavy cpu usage)
#                   multithreading = better for io bound tasks (waiting around)
from multiprocessing import Process, cpu_count
import time
def counter(num):
    count =0
    while count< num:
        count +=1
def main():
    print(cpu_count())
    a = Process(target=counter, args=(250000000,))
    b = Process(target=counter, args=(250000000,))
    c = Process(target=counter, args=(250000000,))
    d = Process(target=counter, args=(250000000,))
    a.start()
    b.start()
    c.start()
    d.start()
    a.join() # syncronization
    b.join()
    c.join()
    d.join()
    print("finished in: ", time.perf_counter(), '  seconds')
if __name__ == "__main__":
    main()
#__________________________________________________________

# # GUI windows

from tkinter import *
# # WIDGETS = GUI elements: buttons, textboxes, labels, images
# # WINDOWS = serves as s cotainer to hold or contain these widgets
window = Tk() #instantiate an instance of a window
window.geometry("420x420")
window.title("My first GUI program")
icon = PhotoImage(file="img/logo.png")
window.iconphoto(True, icon)
window.config(background="#5cfcff")
window.mainloop() #place window on computer screen, listen to events

#__________________________________________________________
# LABELS

from tkinter import *
# # label = an area widget that holds text and/or an image within a window
window = Tk()
photo = PhotoImage(file='img/ph.png')
label = Label(window,
              text='Hello World',
              font=('Arial', 40, 'bold'),
              fg='#00FF00', bg='black',
              relief=RAISED,  # # relief=SUNKEN/RAISED
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound='top'
              )

label.pack()
# label.place(x=50,y=0)
window.mainloop()
load an example dataset
#__________________________________________________________

# BUTTONS
from itertools import count
from tkinter import *

count =0

def click():
    global count
    count +=1
    print(count)


window = Tk()
photo = PhotoImage(file='img/like.png')
button = Button(window,
                text="Click me!",
                command=click,
                font=("Comic Sans", 30),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black",
                state = ACTIVE,  #state=DISABLED,
                image=photo,
                compound='bottom'
                )
button.pack()
window.mainloop()

#__________________________________________________________

# # ENTRY BOX
from pydoc import text
from tkinter import *


# # entry widget - textbox that accepts a single like of user input
def submit():
    username = entry.get()
    print("Hello  "+username)
    # entry.config(state=DISABLED)
def delete():
    entry.delete(0,END)
def backspace():
    entry.delete(len(entry.get())-1, END)

window = Tk()
entry = Entry(window,
              font=("Arial", 50),
              fg="#00FF00",
              bg="black",
              show="*")
# entry.insert(0,'spongebob')
entry.pack(side=LEFT)
submit_button = Button(window, text="submit", command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window, text="delete", command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window, text="backspace", command=backspace)
backspace_button.pack(side=RIGHT)
window.mainloop()

#__________________________________________________________

# GUI checkbox 
from pydoc import text
from tkinter import *
window = Tk()
def display():
    if (x.get()==1):
        print("You agree!")
    else:
         print("You don't agree :(")
x = IntVar()
photo = PhotoImage(file='img/py_logo.png')
check_button = Checkbutton(window,
                           text="I agree something", 
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display,
                           font=("Arial",20),
                           fg='#00FF00',
                           bg='black',
                           activeforeground='#00FF00',
                           activebackground='black',
                           padx=25,
                           pady=10,
                           image=photo,
                           compound='left')
check_button.pack()
window.mainloop()
#__________________________________________________________

# RADIO BUTTONS
radio button = similar to checkbox, but you can only select one from a group
from tkinter import *

food = ["pizza", "hamburger", "hotdog"]


def order():
    if (x.get() == 0):
        print("You ordered pizza!")
    elif (x.get() == 1):
        print("You ordered a hamburger!")
    elif (x.get() == 2):
        print("You ordered a hotdog!")
    else:
        print("huh?")


window = Tk()

pizzaImage = PhotoImage(file='img/pizza.png')
hamburgerImage = PhotoImage(file='img/hamburger.png')
hotdogImage = PhotoImage(file='img/hotdog.png')
foodImages = [pizzaImage, hamburgerImage, hotdogImage]

x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index],  # adds text to radio buttons
                              variable=x,  # groups radiobuttons together if they share the same variable
                              value=index,  # assigns each radiobutton a different value
                              padx=25,  # adds padding on x-axis
                              font=("Impact", 45),
                              image=foodImages[index],  # adds image to radiobutton
                              compound='left',  # adds image & text (left-side)
                              # indicatoron=0, #eliminate circle indicators
                              # width = 375, #sets width of radio buttons
                              command=order  # set command of radiobutton to function
                              )
    radiobutton.pack(anchor=W)
window.mainloop()
#__________________________________________________________

# SLIDING SCALE
from tkinter import *
def submit():
    print('The temperature is: '+ str(scale.get()) +' degrees C')
window = Tk()
hotImage = PhotoImage(file='img/fire_2_11.png')
hotLabel= Label(image=hotImage)
hotLabel.pack()
scale = Scale(window,
              from_=100,to=-100,
              length=600,
              orient=VERTICAL, #orientation of the scale
              font=('Consolas',15),
              tickinterval=10, # adds numeric indicators for value
            #   showvalue=0, #hide current value
              troughcolor_='#69EAFF',
              fg='#FF1C00',
              bg = '#111111'
              )

# scale.set(((scale['from']-scale['to'])/2)+scale['to'])
scale.pack()
button = Button(window, text='submit', command=submit)
button.pack()
coldImage = PhotoImage(file='img/snow_flake.png')
coldLabel= Label(image=coldImage)
coldLabel.pack()

window.mainloop()
#__________________________________________________________

# SELECTABLE List Box
listbox = A listing of selectable text items within it's own container

def submit():

    food = []

    for index in listbox.curselection():
        food.insert(index,listbox.get(index))

    print("You have ordered: ")
    for index in food:
        print(index)

def add():
    listbox.insert(listbox.size(),entryBox.get())
    listbox.config(height=listbox.size())

def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)

    listbox.config(height=listbox.size())

from tkinter import *

window = Tk()

listbox = Listbox(window,
                  bg="#f7ffde",
                  font=("Constantia",35),
                  width=12,
                  selectmode=MULTIPLE)
listbox.pack()

listbox.insert(1,"pizza")
listbox.insert(2,"pasta")
listbox.insert(3,"garlic bread")
listbox.insert(4,"soup")
listbox.insert(5,"salad")

listbox.config(height=listbox.size())

entryBox = Entry(window)
entryBox.pack()

frame = Frame(window)
frame.pack()

submitButton = Button(frame,text="submit",command=submit)
submitButton.pack(side=LEFT)

addButton = Button(frame,text="add",command=add)
addButton.pack(side=LEFT)

deleteButton = Button(frame,text="delete",command=delete)
deleteButton.pack(side=LEFT)

window.mainloop()
#__________________________________________________________

# MESSAGE BOXES

from email import message
from logging import warning
from msilib.schema import Icon
from tkinter import *
from tkinter import messagebox #import the message box library

def click():
    # messagebox.showinfo(title='This is an info message box',
    #                     message='You are a person')
    # messagebox.showwarning(title='WARNING',
    #                     message='You have a virus')
    # messagebox.showerror(title='ERROR',
    #                     message='Something went wrong')
    # if messagebox.askokcancel(title='Ask ok cancel', message='do you want to do the thing?'):
    #     print('You did a thing')
    # else: print('You canceled a thing!')
    # if messagebox.askretrycancel(title='Ask ok cancel', message='do you want to retry the thing?'):
    #     print('You retried a thing')
    # else: print('You canceled a thing!')
    # if messagebox.askyesno(title='Ask yes or no', message='Do you like cake?'):
    #     print('I like cake too')
    # else: print('Why do you not like cake?')
    # answer=messagebox.askquestion(title='Ask question', message='Do you like pie?')
    # if(answer=='yes'):
    #     print('I like pie too!')
    # else:   print('Why do you not like pie?')
    answer =messagebox.askyesnocancel(title='Yes no cancel', message='Do you like code?', icon='warning')
    if(answer==True):
        print('You are my Bro')
    elif(answer==False):
        print('Maybe you need to try')
    else: print('Sorry')
window = Tk()
button = Button(window, command=click, text='Click Me!' )
button.pack()
window.mainloop()
#__________________________________________________________

#  GUI colorchooser 
from tkinter import *
from tkinter import colorchooser # submodule
def click():
    window.config(bg=colorchooser.askcolor()[1])
window = Tk()
window.geometry("420x420")
button = Button(window,
                text='Change the color',
                command=click)
button.pack()
window.mainloop()

#__________________________________________________________

# TEXT AREA
from tkinter import *

# text widget = functions like a text area, you can enter multiple lines of text
def submit():
    input =text.get("1.0", END)
    print(input)
window = Tk()
window.geometry("420x420")
text = Text(window,
            bg='light yellow',
            font=('Ink Free',25),
            height=8,
            width=20,
            padx=20,
            pady=20,
            fg='purple')
text.pack()
button = Button(window, command=submit,  text='Submit the text',)
button.pack()
window.mainloop()

#__________________________________________________________

# GUI open a file (filedialog)

from tkinter import *
from tkinter import filedialog


def openFile():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\ebazi\\source\\python_proj\\helloWorld",
                                          title="Open file okay?",
                                          filetypes=(("text files", "*.txt"),
                                                     ("all files", "*.*")))
    file = open(filepath, 'r')
    print(file.read())
    file.close()


window = Tk()
button = Button(text="Open", command=openFile)
button.pack()
window.mainloop()

#__________________________________________________________

# SAVE A FILE /GUI save a file (filedialog)

from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\ebazi\\source\\python_proj\\helloWorld",
                                    defaultextension='.txt',
                                    filetypes=[
                                        ("Text file",".txt"),
                                        ("HTML file", ".html"),
                                        ("All files", ".*"),
                                    ])
    if file is None:
        return
    filetext = str(text.get(1.0,END))
    #filetext = input("Enter some text I guess: ") #use this if you want to use console window
    file.write(filetext)
    file.close()

window = Tk()
button = Button(text='save',command=saveFile)
button.pack()
text = Text(window)
text.pack()
window.mainloop()

#__________________________________________________________

# GUI menubar
from tkinter import *
def openFile():
    print('file has been opened!')
def saveFile():
    print('file has been saved!')
def cut():
     print('you cut some text!')
def copy():
     print('you copied some text!')
def paste():
     print('you pasted some text!')
window = Tk()
openImage = PhotoImage(file="img/open.png")
saveImage = PhotoImage(file="img/save.png")
exitImage = PhotoImage(file="img/exit.png")
menubar = Menu(window)
window.config(menu=menubar)
fileMenu = Menu(menubar, tearoff=0, font=('MV Boli',15))
menubar.add_cascade(label='File', menu=fileMenu)
fileMenu.add_command(label='Open', command=openFile, image=openImage, compound='left')
fileMenu.add_command(label='Save',command=saveFile, image=saveImage, compound='left')
fileMenu.add_separator()
fileMenu.add_command(label='Exit', command=quit, image=exitImage, compound='left')

editMenu = Menu(menubar, tearoff=0,font=('MV Boli',15))
menubar.add_cascade(label='Edit', menu=editMenu)
editMenu.add_command(label='Cut', command=cut)
editMenu.add_command(label='Copy', command=copy)
editMenu.add_command(label='Paste', command=paste)
window.mainloop()

#__________________________________________________________

# GUI frames
# frame ) a rectangular container to group and hold widgets
from tkinter import *
window = Tk()
frame = Frame(window, bg='pink',bd=5, relief=SUNKEN).pack()
frame.place(x=0, y=0)
Button(frame, text='W', font=('Consolas', 25), width=3).pack(side=TOP)
Button(frame, text='A', font=('Consolas', 25), width=3).pack(side=LEFT)
Button(frame, text='S', font=('Consolas', 25), width=3).pack(side=LEFT)
Button(frame, text='D', font=('Consolas', 25), width=3).pack(side=LEFT)

window.mainloop()
#__________________________________________________________

# open new window 
      #Toplevel() = new window 'on top' of other windows, linked to a 'bottom' window
                            #Tk() = new independent window
    #old_window.destroy()   #close out of old window
from tkinter import *
def create_window():
    # new_window = Tk()
    new_window = Toplevel()
old_window = Tk()
Button(old_window, text='Create new window', command=create_window).pack()
old_window.mainloop()

#__________________________________________________________

# add window tabs


from tkinter import *
from tkinter import ttk

window = Tk()
notebook = ttk.Notebook(window) # widget that manages a collection of windows/dispays
tab1 = Frame(notebook) # new frame for tab1
tab2 = Frame(notebook) 
tab3 = Frame(notebook) 
tab4 = Frame(notebook) 
notebook.add(tab1, text='Tab 1')
notebook.add(tab2, text='Tab 2')
notebook.add(tab3, text='Tab 3')
notebook.add(tab4, text='Tab 4')
notebook.pack(expand=True, fill = 'both') #expand - to fill any space not otherwise used
                                          # fill -fill space on x and y asis
Label(tab1, text='Hello, this is a tan nubber 1', width=50, height=25).pack()
Label(tab2, text='Hello, this is a tan nubber 2', width=50, height=25).pack()
Label(tab3, text='Hello, this is a tan nubber 3', width=50, height=25).pack()
Label(tab4, text='Hello, this is a tan nubber 4', width=50, height=25).pack()

window.mainloop()

#__________________________________________________________

# GUI Grid geometry 
from tkinter import *

##grid() = geometry manager that organizes widgets in a table-like structure in a parent widget

window = Tk()

titleLabel = Label(window,text="Enter your info",font=("Arial",25)).grid(row=0,column=0,columnspan=2)

firstNameLabel = Label(window,text="First name: ",width=20,bg="red").grid(row=1,column=0)
firstNameEntry = Entry(window).grid(row=1,column=1)

lastNameLabel = Label(window,text="Last name: ",bg="green").grid(row=2,column=0)
lastNameEntry = Entry(window).grid(row=2,column=1)

emailLabel = Label(window,text="email: ",bg="blue").grid(row=3,column=0)
emailEntry = Entry(window).grid(row=3,column=1)

submitButton = Button(window,text="Submit").grid(row=4,column=0,columnspan=2)

window.mainloop()

#__________________________________________________________

# PROGRESS BAR
from tkinter import *
from tkinter.ttk import *
import time

def start():
    GB = 100
    download = 0
    speed = 1
    while(download<GB):
        time.sleep(0.05)
        bar['value']+=(speed/GB)*100
        download+=speed
        percent.set(str(int((download/GB)*100))+"%")
        text.set(str(download)+"/"+str(GB)+" GB completed")
        window.update_idletasks()

window = Tk()

percent = StringVar()
text = StringVar()

bar = Progressbar(window,orient=HORIZONTAL,length=300)
bar.pack(pady=10)

percentLabel = Label(window,textvariable=percent).pack()
taskLabel = Label(window,textvariable=text).pack()

button = Button(window,text="download",command=start).pack()

window.mainloop()

#__________________________________________________________

# CANVAS WIDGET
#canvas =  widget that is used to draw graphs, plots, images in a window

from textwrap import fill
from tkinter import *
from tkinter.ttk import Style
from tracemalloc import start
from turtle import width
window = Tk()
canvas = Canvas(window, height=500, width=500)
# blueLine=canvas.create_line(0,0,500,500, fill='blue', width=5)
# redLine=canvas.create_line(0,500,500,0, fill='red', width=5)
# canvas.create_rectangle(50,50,250,250,fill='purple')

# points= [250,0,500,500,0,500]
# canvas.create_polygon(points, fill='yellow', outline='black', width=5)

# canvas.create_arc(0,0,500,500, style=PIESLICE, start=90,extent=180) #CHORD, ARC
canvas.create_arc(0,0,500,500, fill='red', extent=180, width=10) 
canvas.create_arc(0,0,500,500, fill='white', extent=180,start=180, width=10) 
canvas.create_oval(190,190,310,310, fill='white', width=10)
canvas.pack()
window.mainloop()

#__________________________________________________________

# KEY EVENTS

from cgitb import text
from tkinter import *
def dosomething(event):
    # print('you pressed: ' + event.keysym)
    label.config(text=event.keysym)

window = Tk()
window.bind('<Key>', dosomething) #<Key>
label = Label(window, font=('Helvetica',100))
label.pack()

window.mainloop()

#__________________________________________________________

# MOUSE EVENTS

from tkinter import *
def doSomething(event):
    print('Mouse coordinates: '+ str(event.x)+','+ str(event.y))
window = Tk()
# window.bind('<Button-1>', doSomething) #left mouse  click
# window.bind('<Button-2>', doSomething) #mouse wheel
#window.bind('<Button-3>', doSomething) # right mouse click
# window.bind('<Enter>', doSomething) # leave the window
window.bind('<Motion>', doSomething) # where the mouse moved 
window.mainloop()


#__________________________________________________________

# drag & drop widgets (GUI)
from tkinter import *
def drag_start(event):
    widget = event.widget
    widget.startX= event.x
    widget.startY = event.y
def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX +event.x
    y = widget.winfo_y() - widget.startY +event.y
    widget.place(x=x, y=y)
     

window = Tk()
label = Label(window,bg='red', height=5, width=10)
label.place(x=0, y=0)
label2 = Label(window,bg='blue', height=5, width=10)
label2.place(x=100, y=100)
label.bind('<Button-1>', drag_start)
label.bind('<B1-Motion>', drag_motion)

label2.bind('<Button-1>', drag_start)
label2.bind('<B1-Motion>', drag_motion)
window.mainloop()

#__________________________________________________________

# Move image via bind()
from tkinter import *

def move_up(event):
   label.place(x=label.winfo_x(), y=label.winfo_y()-10)
def move_down(event):
   label.place(x=label.winfo_x(), y=label.winfo_y()+10)
def move_left(event):
   label.place(x=label.winfo_x()-10, y=label.winfo_y())
def move_right(event):
   label.place(x=label.winfo_x()+10, y=label.winfo_y())

window = Tk()
window.geometry("500x500")

window.bind("<w>",move_up)
window.bind("<s>",move_down)
window.bind("<a>",move_left)
window.bind("<d>",move_right)
window.bind("<Up>",move_up)
window.bind("<Down>",move_down)
window.bind("<Left>",move_left)
window.bind("<Right>",move_right)

myimage = PhotoImage(file='img/racecar.png')
label = Label(window,image=myimage)
label.place(x=0,y=0)

window.mainloop()

# move image on canvas
from tkinter import *

def move_up(event):
   canvas.move(myimage,0,-10)
def move_down(event):
   canvas.move(myimage,0,10)
def move_left(event):
   canvas.move(myimage,-10,0)
def move_right(event):
   canvas.move(myimage,10,0)

window = Tk()

window.bind("<w>",move_up)
window.bind("<s>",move_down)
window.bind("<a>",move_left)
window.bind("<d>",move_right)

canvas = Canvas(window,width=500,height=500,bg='white')
canvas.pack()

photoimage = PhotoImage(file='img/racecar.png')
myimage = canvas.create_image(0,0,image=photoimage,anchor=NW)
window.mainloop()

#__________________________________________________________

# SIMPLE 2D ANAMATION
from tkinter import *
import time
WIDTH = 500 #constant
HEIGTH = 500
xVelosity= 3
yVelosity=2
window = Tk()
canvas = Canvas(window, width=WIDTH, height=HEIGTH, bg='blue')
canvas.pack()

background_photo = PhotoImage(file='img/space.png')
background = canvas.create_image(0,0,image=background_photo,anchor=NW)

photoimage = PhotoImage(file='img/racecar.png')
my_image = canvas.create_image(0,0,image=photoimage,anchor=NW)
image_width = photoimage.width()
image_height = photoimage.height()
while True:
    coordinates = canvas.coords(my_image)
    print(coordinates)
    if(coordinates[0]>= (WIDTH-image_width) or coordinates[0]<0):
        xVelosity = -xVelosity
    if(coordinates[1]>= (HEIGTH-image_height) or coordinates[1]<0):
        yVelosity = -yVelosity
    canvas.move(my_image,xVelosity,yVelosity)
    window.update()
    time.sleep(0.01)

window.mainloop()


#__________________________________________________________
# Python multiple animations 
from tkinter import *
from ball import Ball

import time


window = Tk()

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

volley_ball = Ball(canvas,0,0,100,1,1,"white")
tennis_ball = Ball(canvas,0,0,50,4,3,"yellow")
basket_ball = Ball(canvas,0,0,125,3,5,"orange")
bowling_ball = Ball(canvas,0,0,75,2,1,"black")

while True:
    volley_ball.move()
    tennis_ball.move()
    basket_ball.move()
    bowling_ball.move()
    window.update()
    time.sleep(0.01)

window.mainloop()

#__________________________________________________________

# CLOCK PROGRAMMING 
from tkinter import *
from time import *

def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)

    window.after(1000,update)


window = Tk()

time_label = Label(window,font=("Arial",50),fg="#00FF00",bg="black")
time_label.pack()

day_label = Label(window,font=("Ink Free",25,"bold"))
day_label.pack()

date_label = Label(window,font=("Ink Free",30))
date_label.pack()

update()

window.mainloop()

#__________________________________________________________

# SENDING EMAIL
import smtplib

sender = "sender@gmail.com"
receiver = "receiver@gmail.com"
password = "*****"
subject = "Python email test"
body = "I wrote an email! :D"

# header
message = f"""From: Snoop Dogg{sender}
To: Nicholas Cage{receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

try:
    server.login(sender,password)
    print("Logged in...")
    server.sendmail(sender, receiver, message)
    print("Email has been sent!")

except smtplib.SMTPAuthenticationError:
    print("unable to sign in")
#__________________________________________________________

