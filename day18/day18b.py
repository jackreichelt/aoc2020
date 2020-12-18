#!/usr/bin/env python3
from math import prod

def evaluate(ex):
  ex = doParentheses(ex)
  ex = doAdditionThenMultiplication(ex)
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
    
def doAdditionThenMultiplication(ex):
  mults = []
  sections = [x.split(' + ') for x in ex.split(' * ')]
  for section in sections:
    mults.append(sum([int(x) for x in section]))
  return prod(mults)
  
expressions = [x.strip() for x in open('input.txt').readlines()]
total = 0
for ex in expressions:
  total += int(evaluate(ex))
  
print(total)
