A,B,C,X = map(int,input().split())
if A+B >= X or A+C >= X or B+C>=X or B+A>=X or C+A >=X or C+B>=X :
    print("YES")
else:
    print("NO")
