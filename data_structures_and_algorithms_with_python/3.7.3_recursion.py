def revString(s):
    if s == "":
        return ""
    first = s[0:1]
    restrev = revString(s[1:])
    result = first + restrev
    return result
def main():
    print(revString('hello,talen'))
if __name__ == "__main__":
    main()
