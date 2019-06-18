# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":

    n = int(input())
    name = {}
    for c in range(0, n):
        a = str(input())
        name[a.split(' ')[0]] = a.split(' ')[1]
    while True:
        try:
            b = str(input())
            if b in name:
                print(b, '=', name[b], sep='')
            else:
                print('Not found')
        except (EOFError):
            break








