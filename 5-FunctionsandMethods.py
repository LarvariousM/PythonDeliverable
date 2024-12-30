#Calling Functions

#Using a function means calling, invoking, executing, or running it. All these terms mean the same thing: you're using the function to do something.

def hello():
    print('Hello')
    return True

hello()         # invoking function; ignore return value
print(hello())  # using return value in a `print` call

print('hello', 'good-bye', 'farewell')

#If you have a lot of arguments, you can break them up into multiple lines. This makes the code easier to read.

print(
    'hello',
    'good-bye',
    'farewell',
    'adios',
    'ciao',
    'auf wiedersehen',
)

#Built-in Functions

#Python has many built-in functions. You can use these functions without importing any modules.

#Learn more here 👉 https://docs.python.org/3/library/functions.html

print(min(-10, 5, 12, 0, -20))      # -20
print(max(-10, 5, 12, 0, -20))      # 12

print(min('over', 'the', 'moon'))   # 'moon'
print(max('over', 'the', 'moon'))   # 'the'

print(max(-10, '5', '12', '0', -20))
# TypeError: '>' not supported between instances
# of 'str' and 'int'

#Use of max and min argument

my_tuple = ('i', 'tawt', 'i', 'taw', 'a',
            'puddy', 'tat')
print(min(my_tuple)) # 'a'
print(max(my_tuple)) # 'tawt'

#ord and chr

print(ord('a'))               # 97
print(ord('A'))               # 65
print(ord('='))               # 61
print(ord('~'))               # 126

print(chr(97))                # a
print(chr(65))                # A
print(chr(61))                # =
print(chr(126))               # ~

#any and all

collection1 = [False, False, False]
collection2 = (False, True, False)
collection3 = {True, True, True}

print(any(collection1))       # False
print(any(collection2))       # True
print(any(collection3))       # True
print(any([]))                # False

print(all(collection1))       # False
print(all(collection2))       # False
print(all(collection3))       # True
print(all([]))                # True

#Functions for the REPL

#The id Function

#The id function returns the memory address of an object. This address is unique to each object.

# Paste this code into the Python REPL
# Don't run it as a program

s = 'Hello, world!'
t = 'Hello, world!'
print(id(s) == id(t))         # False

s = 'supercalifragilisticexpialidocious'
t = 'supercalifragilisticexpialidocious'
print(id(s) == id(t))         # True

x = 5
y = 5
print(id(x) == id(y))         # True

x = 5
y = 6
print(id(x) == id(y))         # False

#Creating Functions

def func_name():
    func_body
    
 def say():
    print('Hi!')
    
#say.py

def say():
    print('Output from say')

print('First')
say()
print('Last')

def say():
    """
    The say function prints "Hi!"
    """
    print('Hi!')

print('-' * 60)
print(say.__doc__)
print('-' * 60)
help(say)

#Scope

#Scope is the area of a program where a variable is accessible. Python has four levels of scope:

def well_howdy(who):
    greeting = 'Howdy'
    print(f'{greeting}, {who}')

well_howdy('Angie')
print(greeting)

greeting = 'Salutations'

def well_howdy(who):
    greeting = 'Howdy'
    print(f'{greeting}, {who}')

well_howdy('Angie')
print(greeting)

#Namespaces

#A namespace is a collection of names. In Python, a namespace is a mapping from names to objects.

#Arguments and Parameters

#Arguments are the values you pass to a function. Parameters are the variables that receive the arguments.

#say2.py

def say(text):
    print(text)

say('hello')
say('hi')
say('how do you do')
say('Quite all right')

#Return Values

#A function can return a value using the return statement. The return statement ends the function and sends a value back to the caller.

def add(a, b):
    return a + b

add(2, 3)           # returns 5

def add(a, b):
    return a + b

two_and_three = add(2, 3)
print(two_and_three)  # 5

#Predicates

#A predicate is a function that returns a boolean value. Predicates are often used with the filter function.

def is_digit(char):
    if char >= '0' and char <= '9':
        return True

    return False

#Default Parameters

#You can assign default values to parameters. If you don't provide a value for a parameter, Python uses the default value.

def say(text='hello'):
    print(text + '!')

say('Howdy') # Howdy!
say()        # hello!

def say(msg1, msg2, msg3='dummy message', msg4):
    pass
# SyntaxError: non-default argument follows default argument

def say(msg1, msg2, msg3='dummy message',
                    msg4='omitted message'):
    print(msg1)
    print(msg2)
    print(msg3)
    print(msg4)

say('a', 'b', 'c', 'd')
# a
# b
# c
# d

say('a', 'b', 'c')
# a
# b
# c
# omitted message

say('a', 'b')
# a
# b
# dummy message
# omitted message

say('a', 'b', , 'd')
# a
# b
# d               # oops - expecting 'dummy message'
# omitted message # oops again - expected 'd'

#Functions vs Methods

#A function is a block of code that performs a specific task. A method is a function that belongs to an object.

my_str = 'abc-123-def'
print(my_str.upper())         # ABC-123-DEF

import math

print(math.sqrt(5))           # 2.23606797749979

#Mutating the Caller

#A function can change the value of a mutable object. This is called mutating the caller.

odd_numbers = [1, 3, 5, 7, 9]
odd_numbers.pop()
print(odd_numbers)  # [1, 3, 5, 7]

def add_new_number(my_list):
    my_list.append(9)

numbers = [1, 2, 3, 4, 5]
add_new_number(numbers)
print(numbers) # [1, 2, 3, 4, 5, 9]

# Returning a new object
def add_new_number(my_list):
    return my_list + [9]

numbers = [1, 2, 3, 4, 5]
new_numbers = add_new_number(numbers)
print(new_numbers) # [1, 2, 3, 4, 5, 9]
print(numbers)     # [1, 2, 3, 4, 5]



