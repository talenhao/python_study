import time
import functools
"""
没有使用functools复制被装饰函数的属性时的输出,可以看到被装饰函数统一显示成clocked
**************************************** calling snooze(.123)
[0.12316942] snooze(0.123) -> None
clocked
**************************************** calling factorial(6)
[0.00000167] factorial(1) -> 1
[0.00005102] factorial(2) -> 2
[0.00008607] factorial(3) -> 6
[0.00013471] factorial(4) -> 24
[0.00016856] factorial(5) -> 120
[0.00020885] factorial(6) -> 720
6! = 720
clocked
使用functools复制被装饰函数的属性时的输出
**************************************** calling snooze(.123)
[0.12319827] snooze(0.123) -> None
snooze
**************************************** calling factorial(6)
[0.00000286] factorial(1) -> 1
[0.00011683] factorial(2) -> 2
[0.00017142] factorial(3) -> 6
[0.00024962] factorial(4) -> 24
[0.00029564] factorial(5) -> 120
[0.00035572] factorial(6) -> 720
6! = 720
factorial
""" 


def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        # 运行时间
        elapsed = time.time() - t0
        # 函数名称
        name = func.__name__
        # 参数
        arg_list = []
        if args:
            arg_list.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['{}={}'.format(k, v) for k, v in sorted(kwargs.items())]
            arg_list.append(', '.join(pairs))
        arg_str = ', '.join(arg_list)
        print("[{:.8f}] {}({}) -> {!r}".format(elapsed, name, arg_str, result))
        return result
    return clocked


@clock
def snooze(seconds):
    time.sleep(seconds)


@clock
def factorial(n):
    return 1 if n < 2 else n * factorial(n-1)


if __name__ == "__main__":
    print('*' * 40, "calling snooze(.123)")
    snooze(.123)
    print(snooze.__name__)
    
    print('*' * 40, "calling factorial(6)")
    print('6! =', factorial(6))
    print(factorial.__name__)
