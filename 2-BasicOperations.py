#Addition

print (38 + 4)      #42
print (38.4 + 41.9) #80.3

#mixing integers & floats
print (38 + 41.5)   #79.5

#Subtraction

print (38 -4)       #34
print (38.4 - 41.9) # -3.5

#mixing integers & floats
print (38 - 41.5)   # -3.5

#Multiplication     

print (38 * 4)      #152
print (38.4 * 41.1) #1578.24

# mixing integers & floats
print(38 * 41.5) #1577.0

#Division with /

print(16 /4)        #4.0
print(16 /2.5)      #6.4

#Integer division with //

print(16 // 3)      # 5
print(16 // -3)     # -6
print(16 // 2.3)    # 6.0
print(-16 // 2.3)   # -7.0

#Exponentiation powers

print(16**3)        # 4096

#Modulo

print(15 % 3)       # 0
print(16 % 3)       # 1
print(17 % 3)       # 2
print(18 % 3)       # 0

from math import remainder

print(int(remainder(14, 7)))    # 0
print(int(remainder(17, 7)))    # 3
print(int(remainder(17, -7)))   # 3
print(int(remainder(-17, 7)))   # -3
print(int(remainder(-17, -7)))  # -3

#Floating Point Imprecision

print(0.1 + 0.2 == 0.3)         # False

import math
math.isclose(0.1 + 0.2, 0.3)    # True

from decimal import Decimal
Decimal('0.1') + Decimal('0.2') == Decimal('0.3')
# True

#Equality Comparison

print(42 == 42)       # True
print(42 == 43)       # False
print('foo' == 'foo') # True (works with strings)
print('FOO' == 'foo') # False (Case matters)

print(42 != 42)       # False
print(42 != 43)       # True
print('foo' != 'foo') # False (works with strings)
print('FOO' != 'foo') # True (Case matters)

#Ordered Comparison

#Less than: (<) and less than or equal to (<=)

print(42 < 41)           # False
print(42 < 42)           # False
print(42 <= 42)          # True
print(42 < 43)           # True

print('abcdf' < 'abcef') # True
print('abc' < 'abcdef')  # True
print('abcdef' < 'abc')  # False
print('abc' < 'abc')     # False
print('abc' <= 'abc')    # True
print('abd' < 'abcdef')  # False
print('A' < 'a')         # True
print('Z' < 'a')         # True

print('3' < '24')        # False
print('24' < '3')        # True

#Greater than: (>) and greater than or equal to (>=)

print(42 > 41)           # True
print(42 > 42)           # False
print(42 >= 42)          # True
print(42 > 43)           # False

print('abcdf' > 'abcef') # False
print('abc' > 'abcdef')  # False
print('abcdef' > 'abc')  # True
print('abc' > 'abc')     # False
print('abc' >= 'abc')    # True
print('abcdef' > 'abd')  # False
print('A' > 'a')         # False
print('Z' > 'a')         # False

print('3' > '24')        # True
print('24' > '3')        # False

#Sets

print({3, 1, 2} < {2, 4, 3, 1})         # True
print({3, 1, 2} > {2, 4, 3, 1})         # False
print({2, 4, 3, 1} > {3, 1, 2})         # True

#Lists (tuples work identically)

print([1, 2, 3] < [1, 2, 3, 4])         # True
print([1, 4, 3] < [1, 3, 3])            # False
print([1, 3, 3] < [1, 4, 3])            # True

#String Concatenation

#>>> 'foo' + 'bar'
#'foobar'

#'1' + '2'

print('abc' * 3)              # 'abcabcabc'
print(3 * 'abc')              # 'abcabcabc'

#Coercion

#Strings To Numbers

print(int('5'))               # 5
print(float('3.141592'))      # 3.141592

#Numbers to Strings

print(str(5))                 # '5'
print(str(3.141592))          # '3.141592'

#Implicit Coercion

# (Unnecessary) Explicit coercion
print(str(3))           # 3
print(str(False))       # False
print(str([1, 2, 3]))   # [1, 2, 3]
print(str({4, 5, 6}))   # {4, 5, 6}

# Implicit coercion
print(3)                # 3
print(False)            # False
print([1, 2, 3])        # [1, 2, 3]
print({4, 5, 6})        # {4, 5, 6}

#Determining Typessss

print(type(1))         # <class 'int'>
print(type(3.14))      # <class 'float'>
print(type(True))      # <class 'bool'>
print(type('abc'))     # <class 'str'>
print(type([1, 2, 3])) # <class 'list'>
print(type(None))      # <class 'NoneType'>

foo = 42               # Variables work, too
print(type(foo))       # <class 'int'>

print(type('abc').__name__)   # str
print(type(False).__name__)   # bool
print(type([]).__name__)      # list

print(type('abc') is str)     # True
print(type('abc') is int)     # False
print(type(False) is bool)    # True
print(type([]) is list)       # True
print(type([]) is set)        # False

print(isinstance('abc', str))    # True
print(isinstance([], set))       # False

class A:
    pass

class B(A):
    pass

b = B()

print(type(b).__name__) # B
print(type(b) is B)     # True
print(type(b) is A)     # False (b's type is
                        # not A)
print(isinstance(b, B)) # True
print(isinstance(b, A)) # True (b is instance of A and B)

#String Representations

my_str = 'abc'
print(my_str)       # abc
print(str(my_str))  # abc (same as print(my_str))
print(repr(my_str)) # 'abc' (note the quotes)

#Collection and String Lengths

print(len('Launch School'))       # 13 (string)
print(len(range(5, 15)))          # 10 (range)
print(len(range(5, 15, 3)))       # 4 (range)
print(len(['a', 'b', 'c']))       # 3 (list)
print(len(('d', 'e', 'f', 'g')))  # 4 (tuple)
print(len({'foo': 42, 'bar': 7})) # 2 (dict)
print(len({'foo', 'bar', 'qux'})) # 3 (set)

#Indexing and Key Access

my_str = "abc"                # string
print(my_str[0])              # 'a'
print(my_str[1])              # 'b'
print(my_str[2])              # 'c'
print(my_str[3])
# IndexError: string index out of range

my_range = range(5, 8)         # range
print(my_range[0])             # 5
print(my_range[1])             # 6
print(my_range[2])             # 7
print(my_range[3])
# IndexError: range object index out of range

my_list = [4, 5, 6]           # list
print(my_list[0])             # 4
print(my_list[1])             # 5
print(my_list[2])             # 6
print(my_list[3])
# IndexError: list index out of range

tup = (8, 9, 10)              # tuple
print(tup[0])                 # 8
print(tup[1])                 # 9
print(tup[2])                 # 10
print(tup[3])
# IndexError: tuple index out of range

#Dictionary Errors

my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict['a'])           # 1
print(my_dict['b'])           # 2
print(my_dict['c'])           # 3
print(my_dict['d'])           # KeyError: 'd'

#Using [] to Update Elements

my_list = [1, 2, 3, 4]
my_list[2] = 6
print(my_list)          # [1, 2, 6, 4]
my_list[4] = 10
# IndexError: list assignment index out of range

my_dict = {
    'dog': 'barks',
    'cat': 'meows',
    'pig': 'oinks',
}

my_dict['pig'] = 'snorts'
print(my_dict)
# Pretty printed for clarity
# {
#     'dog': 'barks',
#     'cat': 'meows',
#     'pig': 'snorts'
# }

my_dict['fish'] = 'glub glub'
print(my_dict)
# Pretty printed for clarity
# {
#     'dog': 'barks',
#     'cat': 'meows',
#     'pig': 'snorts',
#     'fish': 'glub glub'
# }

#Expressions and Statements

#Stand-alone Expressions

3 + 4            # Simple expression
print('Hello')   # Function call; returns None
my_list.sort()   # Method call; returns None

#Expression Evaluation

#>>> 1 + 2 + 3 + 4 + 5
#15

#>>> 4 * 5 - 1 + 2 * 3
#??

print(((4 * 5) - 1) + (2 * 3))   # 25
print((4 * ((5 - 1) + 2)) * 3)   # 72
print(((((4 * 5) - 1) + 2) * 3)) # 63
print(4 * (5 - (1 + (2 * 3))))   # -8

#Output vs Return Values

print('abc')

list(range(3))

