#!/usr/bin/env python3

layout = [list(x.strip()) for x in open('input.txt')]

EMPTY = 'L'
OCCUPIED = '#'
FLOOR = '.'

def nextRound1(layout):
  newLayout = []
  changed = False
  
  for y, row in enumerate(layout):
    newRow = []
    for x, spot in enumerate(row):
      if spot == FLOOR:
        newRow.append(FLOOR)
      elif spot == EMPTY:
        if adjCount(layout, y, x) == 0:
          newRow.append(OCCUPIED)
          changed = True
        else:
          newRow.append(EMPTY)
      elif spot == OCCUPIED:
        if adjCount(layout, y, x) >= 4:
          newRow.append(EMPTY)
          changed = True
        else:
          newRow.append(OCCUPIED)
    newLayout.append(newRow)
  return newLayout, changed

def nextRound2(layout):
  newLayout = []
  changed = False
  
  for y, row in enumerate(layout):
    newRow = []
    for x, spot in enumerate(row):
      if spot == FLOOR:
        newRow.append(FLOOR)
      elif spot == EMPTY:
        if visibleCount(layout, y, x) == 0:
          newRow.append(OCCUPIED)
          changed = True
        else:
          newRow.append(EMPTY)
      elif spot == OCCUPIED:
        if visibleCount(layout, y, x) >= 5:
          newRow.append(EMPTY)
          changed = True
        else:
          newRow.append(OCCUPIED)
    newLayout.append(newRow)
  return newLayout, changed

def adjCount(layout, row, col):
  adjChairs = 0
  for rowMod in [row-1, row, row+1]:
    for colMod in [col-1, col, col+1]:
      if 0 <= rowMod < len(layout) and 0 <= colMod < len(layout[0]) and (row != rowMod or col != colMod):
        try:
          if layout[rowMod][colMod] == OCCUPIED:
            adjChairs += 1
        except e:
          print(e)
  return adjChairs

def visibleCount(layout, row, col):
  visChairs = 0
  for rowMod in [-1, 0, 1]:
    for colMod in [-1, 0, 1]:
      if rowMod == colMod == 0:
        continue
      currRow = row + rowMod
      currCol = col + colMod
      while 0 <= currRow < len(layout) and 0 <= currCol < len(layout[0]):
        target = layout[currRow][currCol]
        if target == OCCUPIED:
          visChairs += 1
          break
        if target == EMPTY:
          break
        currRow = currRow + rowMod
        currCol = currCol + colMod
  return visChairs

def pprintLayout(layout):
  print('\n'.join([''.join(x) for x in layout])+'\n')
  
  
newLayout, changed = nextRound2(layout)
#counter = 0
while changed:
#  counter += 1
#  print(f'done round {counter}')
  layout = newLayout
  newLayout, changed = nextRound2(layout)
  
print('\n'.join([''.join(x) for x in layout]).count('#'))

"""
Wrong answers:
5824
"""