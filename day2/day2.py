#!/usr/bin/env python3

lines = [x.strip().split(': ') for x in open('renee.txt').readlines()]

def parseRule(rule):
	# 1-3 a
	validRange, letter = rule.split(' ')
	min, max = validRange.split('-')
	return int(min), int(max), letter

def parseRule2(rule):
	# 1-3 a
	validRange, letter = rule.split(' ')
	min, max = validRange.split('-')
	return int(min)-1, int(max)-1, letter

def validatePassword(line):
	rule, password = line
	min, max, letter = parseRule(rule)
	
	return min <= password.count(letter) <= max

def validatePassword2(line):
	rule, password = line
	a, b, letter = parseRule2(rule)
	
	return password[a] != password[b] and (password[a] == letter or password[b] == letter)

validatedPasswords = [validatePassword(line) for line in lines]
validPasswords = sum(validatedPasswords)

print(validPasswords)