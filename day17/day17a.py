#!/usr/bin/env python3
      
def cubesToCheck(cubes):
  minX = 0
  maxX = 0
  minY = 0
  maxY = 0
  minZ = 0
  maxZ = 0
  
  for x, y, z in cubes.keys():
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
      
  return minX-1, maxX+1, minY-1, maxY+1, minZ-1, maxZ+1

def adjacentActiveCubes(cubes, x, y, z):
  adjacentActives = 0
  for xMod in [-1, 0, 1]:
    for yMod in [-1, 0, 1]:
      for zMod in [-1, 0, 1]:
        if xMod == yMod == zMod == 0:
          continue
        if cubes.get((x+xMod, y+yMod, z+zMod), False):
          adjacentActives += 1
          
  return adjacentActives

def nextRound(cubes):
  newCubes = {}
  
  minX, maxX, minY, maxY, minZ, maxZ = cubesToCheck(cubes)
  
  for x in range(minX, maxX+1):
    for y in range(minY, maxY+1):
      for z in range(minZ, maxZ+1):
        adjacentActives = adjacentActiveCubes(cubes, x, y, z)
        if cubes.get((x,y,z), False) == True:
          if adjacentActives == 2 or adjacentActives == 3:
            newCubes[(x,y,z)] = True
        else:
          if adjacentActives == 3:
            newCubes[(x,y,z)] = True
  return newCubes

def countActives(cubes):
  return sum(cubes.values())

rows = [x.strip() for x in open('test.txt').readlines()]

# mapping (x, y, z) -> bool
cubes = {}

for y, row in enumerate(rows):
  for x, col in enumerate(row):
    if col == '#':
      cubes[(x,y,0)] = True

for i in range(6):
  cubes = nextRound(cubes)
print('Total active cubes:', countActives(cubes))