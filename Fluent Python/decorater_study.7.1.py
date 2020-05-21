"""
[Thu May 21 talen@tp ~]$ /home/talen/.pyenv/versions/3.7.3/bin/python3.7 /home/talen/PycharmProjects/study/scripts/decorater_study.py
running register <function f1 at 0x7f4912062950>
running register <function f2 at 0x7f49120629d8>
running main()
registry ->  [<function f1 at 0x7f4912062950>, <function f2 at 0x7f49120629d8>]
running f1()
running f2()
running f3()
[Thu May 21 talen@tp ~]$ 
装饰器在导入模块时立即执行,
被装饰函数只有在调用时执行。
"""
registry = []

def register(func):
    print("running register {}".format(func))
    registry.append(func)
    return func

@register
def f1():
    print("running f1()")


@register
def f2():
    print("running f2()")


def f3():
    print("running f3()")


def main():
    print("running main()")
    print("registry -> ", registry)
    f1()
    f2()
    f3()


if __name__ == "__main__":
    main()