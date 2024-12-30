#Literals
#You can use literals to represent most data type values. A literal is any syntactic notation that lets you directly represent an object in source code.
#For example, the following are all literals in Python: 👇

'Hello, world!' #str literal
3.141592        #float literal
True            #bool literal
{'a': 1, 'b': 2} #dict literal
[1, 2, 3]       #list literal]
(4, 5, 6)       #tuple literal
{7, 8, 9}       #set literal

#The following are ❌not❌ literals: 👇

range(10)       # Range of numbers: 0-9
range(1, 11)    # Range of numbers: 1-10
set()           # Empty set
frozenset([1, 2]) # Frozen set of values: 1 and 2

#Numeric Values aka Perform Calculations in Python...my ninja! 🐱‍👤
#Don't use commas or periods to seperate integers, use _!

1_2_3_4_5
9_18_33_32
9121_8733_6196

#Floats
#Use floating point data types to represent real numbers. These include integers and numbers with digits after the decimal point. ONly use a single decimal point to break up numbers.

4.0
3.2
-4.984576
33333.174320_0
432_456_987_899.0

#Big and Small Floats
#Use scientific notation to represent very large or very small numbers. Scientific notation uses the letter e to indicate the power of 10. For example, 1e6 is equal to 1 * 10^6, or 1,000,000.

print(3.14 * (10**20))        # 3.14e+20
print(3.14 * (10**-20))       # 3.14e-20

#e+10 = power of 10, e+20 = power of 20,

print(3.14e+20 / 2.72e-15)    # 1.1544117647058823e+35

#To write larger integers, use the int function to convert the number to an integer.

print(int(3.14e+20))           # 314000000000000000000

#Variables and Assignment
#Variables are names used to identify values aka data. Also called identifiers, constants, function names, and class names.

#Assigning Values to Variables

Red = 9
Green = 11

#Assigning Syntaxes to Assignments

foo = 'Black, Jesus!'
foo = 'Dont drop that yellow cake, bro!'

#Boolean Values
#Use the bool data type to represent boolean values. These values are either True or False. 

turn_on = True
turn_off = False

#Text Sequences
#Words, Sentences, Paragraphs, and more!

'Hello, Neo!'
'Follow the white rabbit.'
'Wake the fuck up, Neo!'

#Strings
#Text sequence of Unicode characters, Python uses string to represent such data

greeting = 'whats up mayne'
for letter in greeting:
    print(letter)
# m
# a
# y
# n
# e

#String Literals and Dealing With Quotes
#It's just quotes, dawg

'Can I have tommorrow off?' #Single quote
'No, you can not have tommorrow off, you IDJIT' #Double quotes

#Triple single quotes

'''Morpheus: "Neo, can you hear me?"
   Neo:      "Yes, I can hear you!"
   Morpheus: "Good...do you see that bitch over there in the red dress?"
   Neo:      "Yes, who is she?"
   Morpheus: "Shes....your future baby momma...and she's keeping it"
   Neo:      "AaAAAaaaAAAAaaaAAArrrgghhhh!, give me that damn blue pill"
   '''
   
#Indexing Strings
#TBA

#Raw Strings and f-Strings
#Raw strings are most often used with Windows-style file names and regular expressions.

# Both of these print my C:\Larvarious\LizzoXXXStash

print("C:\\Larvarious\\LizzoXXXStash")
print(r"C:\\Larvarious\LizzoXXXStash")

#Formatted string literals aka f-Strings
#F-strings enable an operation called string interpolation. You create an f-string by preceding the opening quote with the letter f.

foo = 'whats up mayne'
print(f'Use {{foo}} to embed a string: {foo}')
# Use {foo} to embed a string: whats up mayne

#Functions
#Functions are chunks of standalone, reusable Python code designed to perform an action.

#None
#None expresses the absence of a value. It can also indicate missing, unset, or unavailable data and may sometimes be an error indication.

#Sequences
#Sequences represent an ordered collection of objects. A sequence's objects can be accessed using a numeric index.

# - Lists and Tuples -

[ # Begin multi-line list literal
    "Frank Lucas's Drug Dealing Cartel",
    ( # Begin multi-line tuple literal
      'Denzel Washington',
      'Russell Crowe',
      'Chiwetel Ejiofor',
      'Josh Brolin',
      'Lymari Nadal',
      'Ted Levine',
    ), # End multi-line tuple literal
] # End multi-line list literal

#IMPORTANT FACTS ABOUT LISTS AND TUPLES

# The order of the elements is significant.
# Lists are mutable; tuples are immutable.
# Use indexing syntax to retrieve specific elements.
# Use indexing syntax to reassign specific list elements.
# Index numbers are non-negative integers starting from 0 and ending at the sequence's length minus 1. (Later, we will learn that negative integers are also allowed. For now, though, we'll only use non-negative integers.)





#EXERCISES



