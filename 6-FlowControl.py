#Conditionals

# if, elif, else

#conditional.py

value = int(input('Enter a number: '))

if value == 3:
    print('value is 3')
    
# Run conditional.py at least twice.
# The first time, enter the value 3.
# The second and subsequent times, input any other integer value.

# We can expand the if statement to include some code that runs when value is not 3:

#conditional.py

value = int(input('Enter a number: '))

if value == 3:
    print('value is 3')
else:
    print('value is NOT 3')
    
# Note that the else block isn't a proper statement; it's part of the if statement.

# We can nest if statements inside an outer if. In this next example, we nest an if statement inside the else block of the outer if:

#conditional.py

value = int(input('Enter a number: '))

if value == 3:
    print('value is 3')
else:
    if value == 4:
        print('value is 4')
    else:
        print('value is NOT 3 or 4')
        
# The elif statement is a shorthand way to write an if statement that checks multiple conditions. The following code is equivalent to the previous example:

#conditional.py

if value == 3:
    print('value is 3')
elif value == 4:
    print('value is 4')
else:
    print('value is NOT 3 or 4')
    
if value == 3:
    print('value is 3')
    print('value is an odd number')
    print('value is a prime number')
elif value == 4:
    print('value is 4')
    print('value is an even number')
    print('value is NOT a prime number')
elif value == 9:
    print('value is 9')
    print('value is an odd number')
    print('value is NOT a prime number')
else:
    print('value is something else')
    
#Comparisons

# Remember that comparison operators return a Boolean value: True or False.

# The following table lists the comparison operators in Python:

print(5 == 5)                 # True
print(5 == 4)                 # False

print('abc' == 'abc')         # True
print('abc' == 'abcd')        # False

print(5 == '5')               # False

print([1, 2, 3] == [1, 2, 3]) # True
print([1, 2, 3] == [3, 2, 1]) # False

print(5 == float(5))                # True

big_num = 12345678901234567
print(float(big_num) == big_num)    # False

# Comparisons with strings are case-sensitive. Thus, 'abc' is not equal to 'aBc'. You can use the str.lower and str.upper methods to achieve a case-insensitive comparison:

print('abc' == 'aBc')                 # False
print('abc'.lower() == 'aBc'.lower()) # True
print('abc'.upper() == 'aBc'.upper()) # True

# != is the inequality operator. It returns True if the two operands are not equal:

print(5 != 5)             # False
print(5 != 4)             # True
print('abc' != 'abc')     # False
print('abc' != 'aBc')     # True
print(5 != '5')           # True

# < and <=

# The less-than operator < returns True if the left operand is less than the right operand:

print(4 < 5)              # True
print(5 < 4)              # False
print(5 < 5)              # False

print(4 <= 5)             # True
print(5 <= 4)             # False
print(5 <= 5)             # True

print('4' < '5')          # True
print('5' < '4')          # False
print('5' < '5')          # False

print('42' < '402')       # False
print('42' < '420')       # True
print('420' < '42')       # False

# > and >=

# The greater-than operator > returns True if the left operand is greater than the right operand:

print(4 > 5)              # False
print(5 > 4)              # True
print(5 > 5)              # False

print(4 >= 5)             # False
print(5 >= 4)             # True
print(5 >= 5)             # True

print('4' > '5')          # False
print('5' > '4')          # True
print('5' > '5')          # False

print('42' > '402')       # True
print('42' > '420')       # False
print('420' > '42')       # True

#Logical Operators

#The not, and, and or logical operators provide the ability to combine conditions

# not

print(not True)           # False
print(not False)          # True
print(not(4 == 4))        # False
print(not(4 != 4))        # True

#and and or 

# Examples

print((4 == 4) and (7 == 7))        # True
print((4 == 4) and (7 == 3))        # False
print((4 == 9) and (7 == 7))        # False
print((4 == 9) and (7 == 3))        # False

print((4 == 4) or (7 == 7))         # True
print((4 == 4) or (7 == 3))         # True
print((4 == 9) or (7 == 7))         # True
print((4 == 9) or (7 == 3))         # False

#Short Circuits

# The and and or operators are short-circuit operators. This means that the second operand is not evaluated if the first operand is sufficient to determine the result.

# Truthiness

# In Python, any object can be used in a Boolean context. The following objects are considered False:

# Examples

value = 5                     # 5 is truthy
if value:
    print(f'{value} is truthy')
else:
    print(f'{value} is falsy')
    
value = 0                     # 0 is falsy
if value:
    print(f'{value} is truthy')
else:
    print(f'{value} is falsy')
    
#Truthiness and Short-Circuit Evaluation

# Example

print(3 and 'foo')   # last evaluated op: 'foo'
print('foo' and 3)   # last evaluated op: 3
print(0 and 'foo')   # last evaluated op: 0
print('foo' and 0)   # last evaluated op: 0

print(3 or 'foo')    # last evaluated op: 3
print('foo' or 3)    # last evaluated op: 'foo'
print(0 or 'foo')    # last evaluated op: 'foo'
print('foo' or 0)    # last evaluated op: 'foo'
print('' or 0)       # last evaluated op: 0
print(None or [])    # last evaluated op: []

# Logical expression that returns a non-Boolean object instead of a Boolean:

foo = None
bar = 'qux'
is_ok = foo or bar

if foo or bar:
    is_ok = True
else:
    is_ok = False
    
# Logical Operator Procedure

# ==, !=, <=, <, >, >= - Comparison
# not - Logical NOT
# and - Logical AND
# or - Logical OR

print(1 or 2 and 3)
print(0 or 2 and 3)
print(1 or 0 and 3)
print(1 or 2 and 0)
print(0 or 0 and 3)
print(0 or 2 and 0)
print(1 or 0 and 0)
print(0 or 0 and 0)

print(1 and 2 or 3)
print(0 and 2 or 3)
print(1 and 0 or 3)
print(1 and 2 or 0)
print(0 and 0 or 3)
print(0 and 2 or 0)
print(1 and 0 or 0)
print(0 and 0 or 0)

#match/case statement

# The match statement is a new feature in Python 3.10. It is similar to the switch statement in other languages. The match statement is used to compare a value against a series of patterns and execute the corresponding block of code.

#match.py

value = 5

match value:
    case 5:
        print('value is 5')
    case 6:
        print('value is 6')
    case _: # default case
        print('value is neither 5 nor 6')
# value is 5

#if/else statement

# The match statement is similar to the if/else statement. The if/else statement is used to execute a block of code based on a condition.

value = 5

if value == 5:
    print('value is 5')
elif value == 6:
    print('value is 6')
else:
    print('value is neither 5 nor 6')
# value is 5

#multiple values in a case

# You can specify multiple values in a case statement by separating them with a comma.

value = 5

match value:
    case 1 | 2 | 3 | 4:
        print('value is < 5')
    case 5 | 6:
        print('value is 5 or 6')
    case _: # default case
        print('value is not 1, 2, 3, 4, 5, or 6')
# value is 5 or 6

#Ternary Expressions

# The ternary expression is a one-liner if/else statement. It is used to assign a value to a variable based on a condition.

# Syntax

if shape.sides() == 3:
    print("Triangle")
else:
    print("Square")

print("Triangle" if shape.sides() == 3 else "Square")

print('N/A' if value == None else value)

