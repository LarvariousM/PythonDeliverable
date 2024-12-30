#Terminal Output

#Greetings.py
name = 'Jane'
print(f'Good morning, {name}!')

print(1, 2, 3, 'a', 'b', sep=',')      # 1,2,3,a,b
print('a', 'b', 'c', 'd', 'e', sep='') # abcde

#Terminal Input

#Personalized_Greeting.py
print("What's your name?")
name = input()

print(f'Good Morning, {name}!')

name = input("What's your name? ")

print(f'Good Morning, {name}!')

#Add Two Numbers

#Sum_Numbers.py

number1 = input('Enter the first number: ')
number2 = input('Enter the second number: ')
sum = number1 + number2

print(f'The numbers {number1} and {number2} '
      f'add to {sum}')

number1 = input('Enter the first number: ')
number2 = input('Enter the second number: ')
sum = float(number1) + float(number2)

print(f'The numbers {number1} and {number2} add to {sum}')

