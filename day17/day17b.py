#!/usr/bin/env python3
      
def cubesToCheck(cubes):
  minX = 0
  maxX = 0
  minY = 0
  maxY = 0
  minZ = 0
  maxZ = 0
  minW = 0
  maxW = 0
  
  for x, y, z, w in cubes.keys():
    if x < minX:
      minX = x
    elif x > maxX:
      maxX = x
      
    if y < minY:
      minY = y
    elif y > maxY:
      maxY = y
      
    if z < minZ:
      minZ = z
    elif z > maxZ:
      maxZ = z
    
    if w < minW:
      minW = w
    elif w > maxW:
      maxW = w
      
  return minX-1, maxX+1, minY-1, maxY+1, minZ-1, maxZ+1, minW-1, maxW+1

def adjacentActiveCubes(cubes, x, y, z, w):
  adjacentActives = 0
  for xMod in [-1, 0, 1]:
    for yMod in [-1, 0, 1]:
      for zMod in [-1, 0, 1]:
        for wMod in [-1, 0, 1]:
          if xMod == yMod == zMod == wMod == 0:
            continue
          if cubes.get((x+xMod, y+yMod, z+zMod, w+wMod), False):
            adjacentActives += 1
          
  return adjacentActives

def nextRound(cubes):
  newCubes = {}
  
  minX, maxX, minY, maxY, minZ, maxZ, minW, maxW = cubesToCheck(cubes)
  
  for x in range(minX, maxX+1):
    for y in range(minY, maxY+1):
      for z in range(minZ, maxZ+1):
        for w in range(minW, maxW+1):
          adjacentActives = adjacentActiveCubes(cubes, x, y, z, w)
          if cubes.get((x,y,z,w), False) == True:
            if adjacentActives == 2 or adjacentActives == 3:
              newCubes[(x,y,z,w)] = True
          else:
            if adjacentActives == 3:
              newCubes[(x,y,z,w)] = True
  return newCubes

def countActives(cubes):
  return sum(cubes.values())

rows = [x.strip() for x in open('input.txt').readlines()]

# mapping (x, y, z, w) -> bool
cubes = {}

for y, row in enumerate(rows):
  for x, col in enumerate(row):
    if col == '#':
      cubes[(x,y,0,0)] = True

for i in range(6):
  cubes = nextRound(cubes)
print('Total active cubes:', countActives(cubes))