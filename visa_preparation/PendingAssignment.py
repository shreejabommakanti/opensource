assign,time,days = map(int,input().split())
if assign*time <= days*24*60:
    print("YES")
else:
    print("NO")
