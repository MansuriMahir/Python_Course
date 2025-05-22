def my_decorator(func):
    def wrapper():
        print('**********')
        func()
        print('**********')
    return wrapper

@my_decorator
def greeting (wrapper):
    print('hello wrold!!!')

greeting()
    