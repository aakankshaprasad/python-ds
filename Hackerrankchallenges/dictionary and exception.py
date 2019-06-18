if __name__=="__main__":

    n=int(input())
    name={}
    for c in range (0,n):
        a=str(input())
        name[a.split(' ')[0]]=a.split(' ')[1]
    #print(name)
    count=0
    a=list()
    while True:
        try:
            b=str(input())
            a.append(b)
            if a[count] in name:
                print(a[count],'=',name[a[count]],sep='')
            else:
                print('Not found')
            count+=1
        except (EOFError):
            break
