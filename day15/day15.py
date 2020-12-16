#!/usr/bin/env python3

TESTS = [[0,3,6], [1,3,2], [2,1,3], [1,2,3], [2,3,1], [3,2,1], [3,1,2]]
INPUT = [14,1,17,0,3,20]

def game(starters, endTurn=2020):
  turn = 1
  latest = {}
  history = {}
  
  for i in starters:
    latest[i] = turn
    turn += 1
  
  lastNum = starters[-1]
  
  while turn <= endTurn:
    nextNum = latest[lastNum] - history.get(lastNum, latest[lastNum])
    if nextNum in latest:
      history[nextNum] = latest[nextNum]
    latest[nextNum] = turn
    lastNum = nextNum
        
    turn += 1

  return lastNum

print(game(INPUT, 30000000))