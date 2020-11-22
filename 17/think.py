import functools
import time

if __name__ == "__main__":

    def my_decorator(func):
        # 这个是装饰器传参位置
        def wrapper(*args, **kargs):
            print('in wraps')
            func(*args, **kargs)
        return wrapper
    
    def greet():
        print('in greet')
    
    greet = my_decorator(greet)
    greet()

    @my_decorator
    def greet_1():
        print('in greet_1')

    greet_1()
    print(help(greet_1))

    def my_decorator_1(func):

        @functools.wraps(func)
        def wrapper_1(*args, **kargs):
            print("wrapper_1")
            func(*args, **kargs)
        return wrapper_1

    @my_decorator_1
    def greet_2():
        print('in greet_2')
    greet_2()
    print(help(greet_2))

    # 对于装饰器，一定有一个外层提供闭包接口，那么一定只有一个参数，func 
    def num(num):
        def my_decorator_2(func):
            @functools.wraps(func)
            def wrapper_2(*args, **kargs):
                print("wrapper_2 {}".format(num))
                func(*args, **kargs)
            return wrapper_2
        return my_decorator_2

    # 想要自定义参数
    # greet_3 = num(111)(greet_3)
    @num(111)
    def greet_3(num_g):
        print('int greet_3 {}'.format(num_g))
    greet_3(222)
    print(help(greet_3))


    class Count():
        def __init__(self, func, max_num):
            print('init')
            self._func = func
            self._num  = 0
            self._max  = max_num

        # @functools.wraps(self._func)
        def __call__(self, *args, **kargs):
            self._func(*args, **kargs)
            self._num  += 1
            print('in call {}'.format(self._num))

    # 生成  count 实例
    # greet_4 = Count(greet_4)
    @Count
    def greet_4(num1, num2):
        print("greet_4 {} {}".format(num1, num2))

    greet_4(1, 2)
    # print(help(greet_4))