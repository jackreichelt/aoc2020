#!/usr/bin/env python3

PLUS = '+'
MULT = '*'

# evaluate modes enum
VALUE = 0
OP = 1
SKIPPING = 2

def evaluate(ex):
  total = 0
  op = PLUS
  currVal = ''
  mode = VALUE
  bracketsClosed = 0

  for i, char in enumerate(ex):
    if ex[:i].count(')') < bracketsClosed:
      continue
    if mode == SKIPPING:
      mode = OP
      if char == ' ':
        continue
      elif char == ')':
        mode = VALUE
      
    if mode == VALUE:
      if char == ' ':
        if op == PLUS:
          total += int(currVal)
        elif op == MULT:
          total *= int(currVal)
        currVal = ''
        mode = OP
      elif char == '(':
        sub, closed = evaluate(ex[i+1:])
        if op == PLUS:
          total += sub
        elif op == MULT:
          total *= sub
        currVal = ''
        mode = SKIPPING
        bracketsClosed += closed
      elif char == ')':
        if currVal:
          if op == PLUS:
            total += int(currVal)
          elif op == MULT:
            total *= int(currVal)
        return total, bracketsClosed + 1
      else:
        currVal += char
        
    elif mode == OP:
      if char == '+':
        op = PLUS
      elif char == '*':
        op = MULT
      else:
        mode = VALUE
  
  if char != ')':
    if op == PLUS:
      total += int(currVal)
    elif op == MULT:
      total *= int(currVal)
  
  return total, bracketsClosed
    
expressions = [x.strip() for x in open('test.txt').readlines()]
total = 0
for ex in expressions:
  total += evaluate(ex)[0]

print(total)



"""
Test for Renee:
154580
(7 * (4 + 8 + 6)) + 5 + (5 * 6 + 6 + (6 * 7 + 7 + 3 * 6 + 3) * 5 * (5 + 6 * 8)) + 5 + 4
"""