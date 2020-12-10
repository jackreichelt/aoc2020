#!/usr/bin/env python3
import re

class Passport:
  def __init__(self, inputData):
    self.fields = {x[:3]: x[4:] for x in inputData.strip().split(' ')}
    
  def byr(self):
    return 'byr' in self.fields and len(self.fields['byr']) == 4 and 1920 <= int(self.fields['byr']) <= 2002
  
  def iyr(self):
    return 'iyr' in self.fields and len(self.fields['iyr']) == 4 and 2010 <= int(self.fields['iyr']) <= 2020
  
  def eyr(self):
    return 'eyr' in self.fields and len(self.fields['eyr']) == 4 and 2020 <= int(self.fields['eyr']) <= 2030
  
  def hgt(self):
    if 'hgt' not in self.fields:
      return False
    unit = self.fields['hgt'][-2:]
    value = int(self.fields['hgt'][:-2])
    
    if unit == 'cm':
      return 150 <= value <= 193
    elif unit == 'in':
      return 59 <= value <= 76
    return False
  
  def hcl(self):
    return 'hcl' in self.fields and re.match(r'#[1234567890abcdef]{6}', self.fields['hcl']) != None
  
  def ecl(self):
    VALID_EYE_COLOURS = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return 'ecl' in self.fields and self.fields['ecl'] in VALID_EYE_COLOURS
  
  def pid(self):
    return 'pid' in self.fields and re.match(r'^\d{9}$', self.fields['pid']) != None
  
  def validate(self):
    VALIDATORS = [self.byr, self.iyr, self.eyr, self.hgt, self.hcl, self.ecl, self.pid] # not 'cid'
    
    for validator in VALIDATORS:
      if not validator():
        return False
      
    return True
  
rows = [x.strip() for x in open('input.txt').readlines()]
data = ''

validPassports = 0

for row in rows:
  if row == '':
    # process new passport
    validPassports += 1 if Passport(data).validate() else 0
    data = ''
  else:
    #add input data
    data += ' ' + row
    
print(f'Total valid passports: {validPassports}')