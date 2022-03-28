from functools import wraps
import time
# ---- Декоратор с параметрами, реализованный через класс ----
class Sleep():
    ''' Фабрика декораторов-замедлителей
    '''
    def __init__(self, timeout):
        self.timeout = timeout
    def __call__(self, func):
        ''' Декоратор-замедлитель
        '''
        @wraps(func)
        def decorated(*args, **kwargs):
            ''' Декорированная функция
            '''
            time.sleep(self.timeout)
            res = func(*args, **kwargs)
            print('Function {} was sleeping in class'.format(func.__name__))
            return res
        return decorated
# Применение декоратора, основанного на классе,
@Sleep(3) # заключается в создании объекта данного класса
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)
print(' -- Использован декоратор, реализованный через класс --')
print('!!! Обратите внимание на то, сколько раз будет вызван декоратор (рекурсия)!!!')
print(factorial(2))
