rows = [x.strip() for x in open('input.txt').readlines()]

total = 0
group = set('qwertyuiopasdfghjklzxcvbnm')

for row in rows:
  if row == '':
    total += len(group)
    group = set('qwertyuiopasdfghjklzxcvbnm')
  else:
    group.intersection_update(set(row))
total += len(group)

print(total)