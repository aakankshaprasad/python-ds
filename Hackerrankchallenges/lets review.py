# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    n = int(input())
    # names=list()
    for index in range(n):
        a = str(input())
        str1 = list()
        str2 = list()
        strng = ""
        size = len(a)
        for index in range(0, size):
            if (index % 2 == 0):
                str1.append(a[index])
            else:
                str2.append(a[index])
        print (strng.join(str1), strng.join(str2))
