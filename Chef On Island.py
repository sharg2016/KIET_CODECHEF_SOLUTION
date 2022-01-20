n=int(input())
l=[]
for i in range(n):
    s = str(input())
    l.append(s)
for i in l:
    sp = i.split()
    d = int(sp[0])//int(sp[2])
    e = int(sp[1])//int(sp[3])
    if d == e:
        if(d >= int(sp[4])):
            print("YES")
        else:
            print("NO")

    if e < d:
            if(e >= int(sp[4])):
                print("YES")
            else:
                print("NO")

    if d < e:
            if(d >= int(sp[4])):
                print("YES")
            else:
                print("NO")

