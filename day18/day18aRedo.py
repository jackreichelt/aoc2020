#!/usr/bin/env python3
from math import prod

def evaluate(ex):
  ex = doParentheses(ex)
  ex = doOperations(ex)
  return str(ex)

def doParentheses(ex):
  if '(' not in ex:
    return ex
  
  outEx = ''
  
  buildingSub = False
  sub = ''
  lCount = 0
  rCount = 0
  
  for char in ex:
    if not buildingSub:
      if char != '(':
        outEx += char
      else:
        buildingSub = True
        sub = ''
        lCount = 1
        rCount = 0
    else:
      if char != ')':
        sub += char
        if char == '(':
          lCount += 1
      else:
        rCount += 1
        if rCount < lCount:
          sub += char
        else:
          outEx += evaluate(sub)
          buildingSub = False
    
  return outEx
    
def doOperations(ex):
  PLUS = '+'
  MULT = '*'
  
  total = 0
  op = PLUS
  tokens = ex.split(' ')
  
  for token in tokens:
    if token in [PLUS, MULT]:
      op = token
    else:
      if op == PLUS:
        total += int(token)
      else:
        total *= int(token)
  
  return total
  
expressions = [x.strip() for x in open('input.txt').readlines()]
counts = [int(evaluate(ex)) for ex in expressions]
total = sum(counts)
  
print(total)
