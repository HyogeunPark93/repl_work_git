n = int(input())
x, y = 1, 1
plans = input().split()

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
move_types = ["L", "R", "U", "D"]

for plan in plans:
    for i in range(plans):
        if plan == move_types[i]:
            x_new = x + dx[i]
            y_new = y - dy[i]

    if x_new < 1 or x_new > n or y_new > n or y_new < 1:
        continue

    x, y = x_new, y_new

print(x, y)
