#Variables and Variable Names

#Variables are names used to identify values aka data. Also called identifiers, constants, function names, and class names.

answer = 41
print(answer)       # 41

answer = 42
print(answer)       # 42

#Naming Conventions

# Use snake_case formatting for these names.
# Names may contain lowercase letters (a-z), digits (0-9), and underscores (_).
# Names should begin with a letter.
# If the name has multiple words, separate the words with a single underscore (_).
# Names that begin or end with one or two underscores have special meaning under the naming conventions. Don't use them until you understand how they are used.
# Names may only use letters and digits from the standard ASCII character set.

#Idiomatic Names

#foo
#answer_to_ultimate_question
#eighty_seven
#index_2
#index2

#Constant Names

# Use SCREAMING_SNAKE_CASE formatting for these names.
# Names may contain uppercase letters (A-Z), digits (0-9), and underscores (_).
# Names should begin with a letter.
# If the name has multiple words, separate the words with a single underscore (_).
# Names that begin or end with one or two underscores have special meaning under the naming conventions. Don't use them until you understand how they are used.
# Names may only use letters and digits from the standard ASCII character set.

#Idiomatic Names

#FOO
#ANSWER_TO_ULTIMATE_QUESTION
#EIGHTY_SEVEN
#INDEX_2
#INDEX2

#Creating and Reassigning Variables

forename = 'Clare'       # initialization (also called assignment)

forename = 'Clare'       # initialization (also called assignment)
# omitted code
forename = 'Victor'      # reassignment

#How Initialization and Reassignment Work

# Initialization is the process of creating a new variable and assigning it an initial value.

# Reassignment is the process of changing the value of an existing variable.

# Initialization and reassignment are both accomplished using the assignment operator (=).

foo = 'abcdefghi'

foo = 'Hello'

#Creating Constants

# Constants are variables whose values should not change during the execution of a program.

PINING_FOR = 'fjords'         # initialization

#Expressions and Assignments

# An expression is a combination of values, variables, and operators that Python evaluates to produce a result.

left_side = 5
right_side = 32
total = left_side + right_side  # total = 37
print(total)                    # prints 37

def square(number):
    return number * number

forty_two_squared = square(42)
print(forty_two_squared)                # 1764

foo = 42            # foo is 42
foo = foo - 2       # foo is now 40
foo = foo * 3       # foo is now 120
foo = foo + 5       # foo is now 125
foo = foo // 25     # foo is now 5
foo = foo / 2       # foo is now 2.5
foo = foo**3        # foo is now 15.625
print(foo)          # prints 15.625

#Augmented Assignments

# Augmented assignments are a shorthand way of performing an operation on a variable and then assigning the result back to the same variable.

foo = 42            # foo is 42
foo -= 2            # foo is now 40
foo *= 3            # foo is now 120
foo += 5            # foo is now 125
foo //= 25          # foo is now 5
foo /= 2            # foo is now 2.5
foo **= 3           # foo is now 15.625
print(foo)          # prints 15.625

#Augmented Assignments with Strings

bar = 'xyz'          # bar is 'xyz'
bar += 'abc'         # bar is now 'xyzabc'
bar *= 2             # bar is now 'xyzabcxyzabc'
print(bar)           # prints xyzabcxyzabc

#Augmented Assignments with Lists

bar = [1, 2, 3]     # bar is [1, 2, 3]
bar += [4, 5]       # + with lists appends
                    # bar is now [1, 2, 3, 4, 5]
print(bar)          # prints [1, 2, 3, 4, 5]

#Augmented Assignments with Sets

bar = {1, 2, 3}     # bar is {1, 2, 3}
bar |= {2, 3, 4, 5} # | performs set union
                    # bar is now {1, 2, 3, 4, 5}
bar -= {2, 4}       # - performs set difference
                    # bar is now {1, 3, 5}
print(bar)          # prints {1, 3, 5}

#Augmented Assignments with Constants

def foo(bar):
    print(bar)

a = 3
foo(a *= 2)
#     ^^
# SyntaxError: invalid syntax

def foo():
    a = 3
    return a *= 2
#            ^^
# SyntaxError: invalid syntax

#Reassignment vs Mutation

# Reassignment is the process of changing the value of a variable.

# Mutation is the process of changing the value of a mutable object.

num = 3               # assignment (initialization)
my_list = [1, 2, 3]   # assignment (initialization)
my_dict = {           # assignment (initialization)
    'a': 1,
    'b': 2,
}

num = 42              # Reassignment
my_list[1] = 42       # Reassignment of element,
                      # my_list is mutated!
my_dict['b'] = 3      # Reassignment of dict pair
                      # my_dict is mutated!

# You can still reassign the variables
my_list = [2, 3, 4]   # Reassignment
my_dict = { 'x': 0 }  # Reassignment

