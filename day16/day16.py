#!/usr/bin/env python3

rules, myTicket, otherTickets = open('input.txt').read().split('\n\n')

# Get all valid fields
allValidFields = set()
fields = {}
for rule in rules.split('\n'):
  field, bothRanges = rule.split(': ')
  ranges = bothRanges.split(' or ')
  validValues = set()
  fields[field] = validValues
  for eachRange in ranges:
    minVal, maxVal = eachRange.split('-')
    validValues.update({x for x in range(int(minVal), int(maxVal)+1)})
  allValidFields.update(validValues)
    
errorRate = 0

validTickets = []

for ticket in otherTickets.split('\n')[1:]:
  ticket = [int(x) for x in ticket.split(',')]
  for value in ticket:
    if value not in allValidFields:
      errorRate += value
      break
  else:
    validTickets.append(ticket)
  
print(f'Ticket scanning error rate: {errorRate}')

possibleFields = [set(fields.keys()) for x in range(len(fields))]

# Calculate possible fields
for ticket in validTickets:
  for i, value in enumerate(ticket):
    fieldsToDelete = set()
    for field in possibleFields[i]:
      if value not in fields[field]:
        fieldsToDelete.add(field)
    possibleFields[i].difference_update(fieldsToDelete)
    
# Remove single possibilites from others
removed = True
while removed:
  removed = False
  for possibilities in possibleFields:
    if len(possibilities) == 1:
      itemToRemove = list(possibilities)[0]
      for other in possibleFields:
        if len(other) != 1:
          other.discard(itemToRemove)
          removed = True

print('Possibilities removed')

departureProduct = 1
myTicket = [int(x) for x in myTicket.split('\n')[1].split(',')]

for i, field in enumerate(possibleFields):
  fieldName = list(field)[0]
  if fieldName.startswith('departure'):
    departureProduct *= myTicket[i]

print('My departure values:', departureProduct)