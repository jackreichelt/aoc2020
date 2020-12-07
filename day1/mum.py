file_name = 'input.txt'
# file_name = 'Test.txt'

f = open(file_name, 'r')
#data = f.read().splitlines()

# for integer data
data = [int(x) for x in open(file_name).readlines()]

#print(len(data))

sum1 = 0

for d in data:
	remainder = 2020 - d
	if remainder in data:
		sum1 = d
		print(d)
		break
	
result = sum1 * (2020 - sum1)
print(result)
print()


sum2 = 0
sum3 = 0

for d1 in data:
	for d2 in data:
		if d1 == d2:
			continue
		remainder = 2020 - d1 - d2
		if remainder in data:
			sum2 = d1
			sum3 = d2
			break
	if sum2 > 0:
		break
	
d0 = 2020 - d1 - d2
print(d0, d1, d2)
result2 = d0 * d1 * d2
print(result2)

