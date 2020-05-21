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
