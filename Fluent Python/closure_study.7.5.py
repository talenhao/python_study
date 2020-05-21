def make_averager():
    series = []
    # closure 闭包函数
    def averager(new_value):
        # series 自由变量
        series.append(new_value)
        total = sum(series)
        return total/len(series)
    return averager

avg = make_averager()
print(avg(10))
print(avg(11))
print(avg(12))
print("局部变量:", avg.__code__.co_varnames)
print("自由变量:", avg.__code__.co_freevars)
print("自由变量绑定的闭包函数元素:", avg.__closure__)
print("局部变量内容:", avg.__closure__[0].cell_contents)


# 对于自由变量是非可变类型使用nonlocal声明
def make_averager2():
    count = 0
    total = 0
    # closure 闭包函数
    def averager(new_value):
        # 声明成自由变量
        nonlocal count, total
        count += 1
        total += new_value
        return total/count
    return averager

avg = make_averager2()
print(avg(10))
print(avg(11))
print(avg(12))
print("局部变量:", avg.__code__.co_varnames)
print("自由变量:", avg.__code__.co_freevars)
print("自由变量绑定的闭包函数元素:", avg.__closure__)
print("局部变量内容:",[ closure.cell_contents for closure in avg.__closure__])