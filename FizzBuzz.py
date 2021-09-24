# Rulez of FizzBuzz
# If the number is divisible by 3, print "is a Fizz number."
# If the number is divisible by 5, print "is a Buzz number."
# If the number is divisible by both 3 and 5, print "is a FizzBuzz number."
# Otherwise, print "is neither a fizzy or a buzzy number."

name = input('Enter your name here: ')
number = int(input('Enter your number here: '))

print (f'Hello {name}! You choose the number {number}!')

if number / 3 == number // 3 and number /5 == number //5:
    print(f'{number} is a FizzBuzz number.')

elif number / 3 == number // 3:
    print(f'{number} is a Fizz number.')

elif number /5 == number //5:
    print(f'{number} is a Buzz number.')
    
else:
    print (f'{number} is neither a fizzy or a buzzy number.')