from task_s import add

result = add.delay(2, 8)
print('hello world!')
print(result.ready())
print(result.get())
print(result.ready())