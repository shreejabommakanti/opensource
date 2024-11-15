x, n = map(int, input().split())
add_pass = n-x *100

new_planes = (add_pass + 99) // 100
print(new_planes)
