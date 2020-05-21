import time
import functools
"""
[Thu May 21 talen@tp ~]$ /home/talen/.pyenv/versions/3.7.3/bin/python3.7 "/home/talen/github/tianfei/python_study/Fluent Python/decorater_study.7.17.py"
**************************************** calling snooze(.123)
[0.12318444] snooze(0.123) -> None
**************************************** calling factorial(6)
[0.00000310] factorial(1) -> 1
[0.00009680] factorial(2) -> 2
[0.00016260] factorial(3) -> 6
[0.00025153] factorial(4) -> 24
[0.00031281] factorial(5) -> 120
[0.00038075] factorial(6) -> 720
6! = 720
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
    
    print('*' * 40, "calling factorial(6)")
    print('6! =', factorial(6))