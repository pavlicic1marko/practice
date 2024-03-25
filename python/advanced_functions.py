import time
import inspect


# decorators
# create a decorator to measure the time it took to execute a function
def measure_time(function):
    def wrapper():
        t1 = time.time()
        function()
        t2 = time.time() - t1
        print("time for function {0} to execution is: {1}".format(function.__name__, t2))

    return wrapper


@measure_time
def print_and_sleep_1s():
    time.sleep(1)
    print(inspect.currentframe().f_code.co_name)


@measure_time
def print_and_sleep_2s():
    time.sleep(2)
    print(inspect.currentframe().f_code.co_name)


'''
print_and_sleep_1s()
print_and_sleep_2s()
print(type(print_and_sleep_1s))
'''


# decorators with arguments

def dec_argument(argument):
    def decorator_function(original_function):
        def wrapper_function(*args, **kwargs):
            print(argument,'Executed Before', original_function.__name__)
            result = original_function(*args, **kwargs)
            print(argument,'Executed After', original_function.__name__)
            return result
        return wrapper_function
    return decorator_function

@dec_argument('this is prefix text:')
def dispaly_info(name, age):
    print('dispaly_info ran with arguments:', name, age)


'''
dispaly_info(1,2)
dispaly_info('12','34')
'''


# first-class functions, function that return functions as result
# or as arguments receives functions
def square(x):
    return x * x


func_ex = square(5)
f = square


def map_function(list1, function):
    result = []
    for item in list1:
        result.append(function(item))
    return result


'''
print(f(5))
print(func_ex)
print(map_function([1,2,3,4,5],square))
'''


# closers
# inner function still hase access to the variables of the scope of outer function after it stoped executing

def outer_func(msg):
    message = msg

    def inner_func():
        print(message)

    return inner_func


my_func1 = outer_func('msg')
my_func2 = outer_func('part2')

'''
my_func1()
my_func2()
'''
