import random


def print_square(n):
    if n == 1:
        print('*')
    elif n == 2:
        print('**')
        print('**')
    else:
        print('*' * n)
        print_rows(n-2, n)
        print('*' * n)


def print_rows(n, columns):
    if n != 0:
        print('*', ' ' * (columns-4), '*')
        print_rows(n-1, columns)


def retry(attempts=5, desired_value=None):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            print('attempts:', attempts, 'desired value:', desired_value)
            counter = attempts
            while True:
                result = func(*args, **kwargs)
                print('counter:', counter, 'result:', result)
                counter = counter - 1
                if (counter == 0) or (desired_value == result):
                    break
            if counter == 0:
                print('failure')
            else:
                return result
        return inner_wrapper
    return wrapper


@retry(attempts=10, desired_value=5)
def get_random_value():
    return random.choice((1, 2, 3, 4, 5))


@retry(desired_value=[1, 2])
def get_random_values(choices, size=2):
    return random.choices(choices, k=size)


# print(get_random_value())
# print(get_random_values([1, 2, 3, 4]))
# print_square(10)
