#!/usr/bin/env python3

PREAMBLE_LENGTH = 5

#INVALID = 127
#INVALID_INDEX = 14

INVALID = 14144619
INVALID_INDEX = 504

numbers = [int(x.strip()) for x in open('input.txt')]

def part1():
  for i, n in enumerate(numbers):
    if i < PREAMBLE_LENGTH:
      continue # makes future maths easier to just continue past preamble
    found = False
    for j in numbers[i-PREAMBLE_LENGTH:i]:
      if n - j != j and n - j in numbers[i-PREAMBLE_LENGTH:i]:
        found = True
        break
    if not found:
      print(f'Sum not found for {n} at index {i}')
      return
    
    #part1()
    
def part2():
  for size in range(2, len(numbers)):
    for start in range(0, len(numbers) - size):
      chunk = numbers[start:start+size]
      if sum(chunk) == INVALID:
        print(f'Sum found {chunk}')
        print(f'Answer = {min(chunk) + max(chunk)}')
        return
      
part2()