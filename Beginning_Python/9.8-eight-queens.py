#!/usr/bin/env python3


import random
def conflict(state, next_x):
    """
    :param state:
    :param next_x:
    :return:
    """
    # 判断点的y标值跟已部署的点的数量值是相等的
    next_y = len(state)
    # 判断每个已经部署的point是否冲突,X值可以从state[y]获取
    for point in range(next_y):
        # 判断对称
        if abs(state[point]-next_x) in (0, next_y-point):
            return True
    return False


def queen_pos(num, state):
    """
    返回所有可放置的位置
    :param num:
    :param state:
    :return:
    """
    if len(state) == num-1:
        for pos in range(num):
            if not conflict(state, pos):
                yield pos


print(list(queen_pos(4, (1, 3, 0))))


def queens(num=8, state=()):
    """
    :param num:
    :param state:
    :return:
    """
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num-1:
                yield (pos,)
            else:
                for result in queens(num, state+(pos,)):
                    yield (pos,) + result


def pretty_print(solution):
    def line(pos, length=len(solution)):
        return '. ' * pos + 'X ' + '. ' * (length-pos-1)

    for pos in solution:
        print(line(pos))


random_list=random.choice(list(queens(8)))
print(random_list)
pretty_print(random_list)