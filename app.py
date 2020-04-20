# Rules:
# If input divisible by 3 then return the string 'Fizz'
# If input divisible by 5 then return the string 'Buzz'
# If input divisible by both 3 and 5 return the string 'FizzBuzz'
# For any other numbers it will return the same number from the input

# 1st try

def fizz_buzz_mike_answer(input):
    if input % 3 == 0 and input % 5 == 0:
        return 'FizzBuzz'
    elif input % 3 == 0:
        return 'Fizz'
    elif input % 5 == 0:
        return 'Buzz'
    else:
        return input

def fizz_buzz_mosh_answer(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return 'FizzBuzz'
    if input % 3 == 0:
        return 'Fizz'
    if input % 5 == 0:
        return 'Buzz'
    return input

print(fizz_buzz_mosh_answer(3))