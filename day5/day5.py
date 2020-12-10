def seatId(bp):
  row = int(bp[:7].replace('F', '0').replace('B', '1'), 2)
  col = int(bp[7:].replace('L', '0').replace('R', '1'), 2)
  return row * 8 + col

passes = [seatId(x.strip()) for x in open('input.txt').readlines()]

for id in range(min(passes), max(passes)):
  if id not in passes and id-1 in passes and id+1 in passes:
    print(id)
