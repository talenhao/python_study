#/bin/env python3
def revList2(lst):
    def revListHelper(index):
        if index == -1:
            return []
        first = [lst[index]]
        restrev = revListHelper(index-1)
        result = first + restrev
        return result
        
    return revListHelper(len(lst)-1)
def main():
    print(revList2([1,2,3,4,5]))
if __name__ == "__main__":
    main()