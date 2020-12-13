#!/usr/bin/env python
from math import prod

timestamp, busses = [x.strip() for x in open('input.txt').readlines()]
part1Busses = [int(x) for x in busses.split(',') if x != 'x']

answer = min([(bus - int(timestamp) % bus, bus) for bus in part1Busses])
print(f'Part 1: {answer[0] * answer[1]}')

part2Busses = []
xs = 0
for part in busses.split(','):
  if part != 'x':
    part2Busses.append((int(part), xs))
  xs += 1

startTimes = [0]
multipliers = [1]
currentTime = max(startTimes)
findIndex = 0
loops = 0
while True:
  currentIndex = 0
  for bus, offset in part2Busses:
    if currentIndex == findIndex:
      loops += 1
    if currentIndex == findIndex + 1:
      if len(startTimes) == len(multipliers):
        startTimes.append(currentTime)
      else:
        multipliers.append(loops)
        findIndex += 1
      loops = 0
    if (currentTime + offset) % bus != 0:
      currentTime += 1 * prod(multipliers)
      break
    currentIndex += 1
  else:
    print(f'Part 2: {currentTime}')
    break