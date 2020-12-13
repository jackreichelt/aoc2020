adaptors = sorted([int(x) for x in open('input.txt')])
target = adaptors[-1] + 3
adaptors.append(target)

def part1(adaptors):
  
  currentJ = 0
  diff1 = 0
  diff3 = 0
  
  while currentJ < target:
    if currentJ + 1 in adaptors:
      currentJ += 1
      diff1 += 1
    elif currentJ + 2 in adaptors:
      currentJ += 2
    elif currentJ + 3 in adaptors:
      currentJ += 3
      diff3 += 1
    else:
      print(f'Error. No adaptor found above {currentJ} jolts')
      exit()
      
  print(f'{diff1} * {diff3} = {diff1*diff3}')
  
diffZeroes = {x: 0 for x in adaptors}


def diffZeroCalc(num):
  variants = 0
  for lower in range(num-3, num):
    if lower == 0:
      variants += 1
    elif lower in adaptors:
      variants += diffZeroes[lower]
  return variants

for num in adaptors:
  diffZeroes[num] = diffZeroCalc(num)
  
print(f'Oh god, did it work? {diffZeroes[target]}')