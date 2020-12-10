numbers = [int(x.strip()) for x in open('input.txt').readlines()]

"""
Part 1
"""

#for a in numbers:
#	for b in numbers:
#		if a + b  == 2020:
#			print(f'{a} x {b} = {a*b}')
#			exit()

"""
Part 2
"""

for a in numbers:
  for b in numbers:
    for c in numbers:
      if a + b + c == 2020:
        print(f'{a} x {b} x {c} = {a*b*c}')
        exit()
        