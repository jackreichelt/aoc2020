#!/usr/bin/env python3
from math import prod

ACROSS = [1,3,5,7,1]
DROP = [1,1,1,1,2]
OPEN = '.'
TREE = '#'

rows = [x.strip() for x in open('input.txt').readlines()]
width = len(rows[0])

trees = [0,0,0,0,0]

for option in range(5):
  pos = 0
  
  for row in rows[::DROP[option]]:
    if row[pos] == TREE:
      trees[option] += 1
    pos = (pos + ACROSS[option]) % width
    
  print(f'For option {option}, {trees[option]} trees encountered')
  
print(f'Product: {prod(trees)}')


#for row in rows:
#	if row[pos] == TREE:
#		trees += 1
#	pos = (pos + ANGLE) % width
#
#print(f'{trees} trees encountered')