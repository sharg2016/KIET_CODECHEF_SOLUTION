r , o , c = map(int , input().split())

if(r==720):
    print("NO")

else:
    d = (20-o)*6*6

    if (r-d) <= c:
        print("YES")
    else:
        print("NO")