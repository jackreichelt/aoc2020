#!/usr/bin/env python3

instructions = [x.strip() for x in open('input.txt').readlines()]

def applyValueMask(value, mask):
  binVal = format(int(value), '036b')
  maskedVal = ''
  for index, bit in enumerate(mask):
    maskedVal += bit if bit != 'X' else binVal[index]
  return int(maskedVal, 2)

def applyMemMask(address, mask):
  binAdd = format(int(address), '036b')
  maskedAdd = ''
  for index, bit in enumerate(mask):
    if bit == '0':
      maskedAdd += binAdd[index]
    elif bit == '1':
      maskedAdd += '1'
    else:
      maskedAdd += 'X'
  return maskedAdd

def permutateAddress(maskedAdd):
  permutations = []
  for i in range(int('1' + maskedAdd.count('X')*'0', 2)):
    perm = list(maskedAdd)
    bits = format(i, '0'+str(maskedAdd.count('X'))+'b')
    bitIndex = 0
    for index, char in enumerate(perm):
      if char == 'X':
        perm[index] = bits[bitIndex]
        bitIndex += 1
    permutations.append(''.join(perm))
  return permutations
    
def part1():
  mask = ''
  memory = {}
  
  for inst in instructions:
    command, value = inst.split(' = ')
    if command == 'mask':
      mask = value
    elif command.startswith('mem'):
      address = command[command.find('[')+1:-1]
      memory[address] = applyValueMask(value, mask)
      
  print(sum(memory.values()))
  
def part2():
  mask = ''
  memory = {}
  
  for inst in instructions:
    command, value = inst.split(' = ')
    if command == 'mask':
      mask = value
    elif command.startswith('mem'):
      address = command[command.find('[')+1:-1]
      addresses = permutateAddress(applyMemMask(address, mask))
      for address in addresses:
        memory[address] = int(value)
  print(sum(memory.values()))

part1()
part2()