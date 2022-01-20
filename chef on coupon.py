n = int(input())

for i  in range(n):
    d , c = map(int,input().split())
    a = list(map(int , input().split()))
    b = list(map(int , input().split()))

    charge = d+d
    coupon = c
    sum1 = sum(a)
    sum2 = sum(b)

    if(sum1 < 150):
        coupon += d

    if(sum2 < 150):
        coupon += d

    if (coupon < charge):
        print("YES")
    else:
        print("NO")

