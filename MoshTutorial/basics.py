import math

"""
Tutorial: https://www.youtube.com/watch?v=_uQrJ0TkZlc&t=7729s
"""


course = 'Python learning tutorial'
print(course[0:-3])
print("Another variable: ")
another = course[:]
print(another)

# works only on python > 3.6
# formated_string = (f'this is an another  course')
# print(formated_string)

print(len(another))
print(another.upper())

# find and return the location of 'P'
print(another.find('P'))

# replaces 'P' to J
print(another.replace('P', 'J'))


# Math
x = 2.9
print(round(2.9))
print(abs(-2.9))  # always retrun positive value
print(math.ceil(2.9))

is_hot = False
is_cold = True
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It is cold day")
    print("wear warm clothes")
else:
    print("It is a lovely day")

print("enjoy your day")

price = 1000000
has_good_credit = True

if has_good_credit:
    downpayemnt = 0.1 * price
else:
    downpayemnt = 0.2 * price

print("the downpayment is $" + str(downpayemnt))

# Logical Operators
has_high_income = False
has_good_credit = True
if has_good_credit and not has_high_income:
    print("eligilble for loan")
else:
    print("not eligible for loan")


# while loop
secret_number = 9
guest_count = 0
guess_limit = 3
while guest_count < guess_limit:
    guess = int(input("Guess:"))
    guest_count += 1
    if guess == secret_number:
        print("You won!")
        break
else:
    print("You Lost!")


# Data Types
x = 10.0001
y = 2
quo, reminder = divmod(x, y)
print("Quotient", quo)
print("Reminder", reminder)


# Execptin handline
try:
    age = int(input('Age:'))
    income = 20000
    risk = income/age
    print(age)
except ValueError:
    print("Invalid value")
except ZeroDivisionError:
    print("Age cannot be 0")


# Class
class Point:
    # constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


# Initialize with constructor
point1 = Point(10, 20)
print(point1.x)
print(point1.y)
point1.x = 10
point1.y = 20
print(point1.x)
print(point1.y)


# Inherritance
class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    pass


class Cat(Mammal):
    def walk(self):
        print("walk")
