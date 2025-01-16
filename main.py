'''
The Fizz Game, commonly referred to as the FizzBuzz Game, is a simple and popular problem often used in programming interviews or as a fun classroom activity. The rules are as follows:

Count sequentially starting from 1.
For numbers divisible by 3, say "Fizz" instead of the number.
For numbers divisible by 5, say "Buzz" instead of the number.
For numbers divisible by both 3 and 5, say "FizzBuzz" instead of the number.
For all other numbers, just say the number.
'''

def fizz_buzz(n):
    for number in range(1, n+1):
        if number % 3 == 0 and number % 5 == 0:
            print('FizzBuzz')
        elif number % 3 == 0:
            print('Fizz')
        elif number % 5 == 0:
            print('Buzz')
        else:
            print(number)

fizz_buzz(50)