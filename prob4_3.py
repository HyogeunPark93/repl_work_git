init_pos = input()
row = int(init_pos[1])
col = int(ord(init_pos[0]))-int(ord('a'))+1

steps = [(-2,-1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

result = 0
for step in steps:
  row_new = row + step[0]
  col_new = col + step[1]
  if row_new <=8 and row_new >=1 and col_new <=8 and col_new >=1:
    result += 1

print(result)