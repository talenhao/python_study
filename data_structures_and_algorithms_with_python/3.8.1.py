#!/bin/env python3
def revList(lst):
    seq = type(lst)()
    if lst == seq:
        return seq
    restrev = revList(lst[1:])
    first = lst[0:1]
    result = restrev + first
    return result
def main():
    print(revList([1,2,3,4]))
    print(revList("talen"))
if __name__ == "__main__":
    main()
