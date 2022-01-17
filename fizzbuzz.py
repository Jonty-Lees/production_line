# Here is a very simple solution to fizzbuzz, taking in the user input

user_num = int(input('What number do you want to go up too? : '))


for num in range(user_num):
    if num % 5 == 0 and num % 3 == 0:
        print('Fizzbuzz')
    elif num % 5 == 0:
        print('Buzz')
    elif num % 3 == 0:
        print('Fizz')
    else:
        print(num)
