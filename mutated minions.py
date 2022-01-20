count = 0
t= int(input())
for j in range(t):
    (n , k) = map(int,input().split(" "))

    s = str(input())
    sp = s.split()

    for i in range(len(sp)):
        d = int(sp[i]) + k
        if (d % 7 == 0):
            count += 1

    print(count)
    count =0