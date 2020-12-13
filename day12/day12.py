#!/usr/bin/env python3

commands = [x.strip() for x in open('input.txt').readlines()]

wPos = (10, 1)
sPos = (0, 0)

for command in commands:
	inst = command[0]
	value = int(command[1:])
	if inst == 'N':
		wPos = (wPos[0], wPos[1]+value)
	elif inst == 'S':
		wPos = (wPos[0], wPos[1]-value)
	elif inst == 'E':
		wPos = (wPos[0]+value, wPos[1])
	elif inst == 'W':
		wPos = (wPos[0]-value, wPos[1])
	elif inst == 'L':
		for i in range(value // 90):
			wPos = (-wPos[1], wPos[0])
	elif inst == 'R':
		for i in range(value // 90):
			wPos = (wPos[1], -wPos[0])
	elif inst == 'F':
		sPos = (sPos[0] + wPos[0] * value, sPos[1] + wPos[1] * value)

print(abs(sPos[0]) + abs(sPos[1]))

"""
Wrong answers:
32363
"""