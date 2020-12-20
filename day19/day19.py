#!/usr/bin/env python3
class Rule:
  def __init__(self, ruleString):
    self.ruleString = ruleString
    if self.ruleString.count('"') == 2:
      self.ruleString = self.ruleString[1:-1]
      self.literal = True
    else:
      self.literal = False
      self.variants = [x.split() for x in self.ruleString.split(' | ')]
      
  def matches(self, message, part2=False):
    if self.literal:
      return message.startswith(self.ruleString), 1
    elif part2 == True and self.ruleString == '8 11':
      messageChunks = len(message) // 8
      bChunks = 1
      aChunks = messageChunks - 1
      variants = []
      while bChunks < aChunks:
        variants.append(['42'] * aChunks + ['31'] * bChunks)
        bChunks += 1
        aChunks -= 1
    else:
      variants = self.variants
      
    for variant in variants:
      startIndex = 0
      for segment in variant:
        matches, matchLength = rules[segment].matches(message[startIndex:])
        if not matches:
          break
        else:
          startIndex += matchLength
      else:
        return True, startIndex
    return False, 0
    
def match(message, part2=False):
  potential, length = rules['0'].matches(message, part2)
  return potential == True and length == len(message)

rules = {x.strip().split(': ')[0] : Rule(x.strip().split(': ')[1]) for x in open('inputRules.txt').readlines()}
messages = [x.strip() for x in open('inputMessages.txt').readlines()]

count = 0
for message in messages:
  if match(message, True):
    count += 1
  
print(count)