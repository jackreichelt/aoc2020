file_name = 'Data.txt'
#file_name = 'Test2.txt'

f = open(file_name, 'r')
data = f.read().splitlines()

class Bag:
	
	def __init__(self, bagLine):
		parts = bagLine.split(' bags contain ')
		self.colour = parts[0]
		if parts[1] == 'no other bags.':
			self.bag_list = {}
		else:
			bags_data = parts[1]
			bags_data = bags_data.replace(' bags', ' bag')
			bags_data = bags_data.replace(' bag.', '')
			
			bags = bags_data.split(' bag, ')
			self.bag_list = {}
			for bag in bags:
				bag_count, bag_colour = bag.split(' ', 1)
				self.bag_list[bag_colour] = int(bag_count)
			
			
	def __str__(self):
		bags = []
		for colour, number in self.bag_list.items():
			bags.append(f'{number} x {colour}')
		bagString = ', '.join(bags)
		return f'{self.colour}: {bagString}'
		
	def bag_can_hold(self, col, all_bags = {}):
		if col in self.bag_list:
			return True
		inner_colours = self.bag_list.keys()
		for inner in inner_colours:
			inner_bag = all_bags[inner]
			if inner_bag.bag_can_hold(col, all_bags):
				return True
		return False
		
	
	def bag_count(self):
		return sum(self.bag_list.values())
	
	
	def number_of_bags(self, all_bags = {}):
		total = 0
		colour = self.colour
		
		if len(self.bag_list) == 0:
			return 0
		
		total += self.bag_count()
		
		for colour, number in self.bag_list.items():
			inner_bag = all_bags[colour]
			total +=  inner_bag.number_of_bags(all_bags) * number
			
		return total
	

bags = [Bag(bagLine) for bagLine in data]
#for b in bags:
#	print(b)
#print()

bag_dict = { b.colour: b for b in bags }
#for (c, b) in bag_dict.items():
#	print(c, ': ', b)
#print()

goal = 'shiny gold'

valid_bags = [b for b in bags if b.bag_can_hold(goal, bag_dict)]
#for b in valid_bags:
#	print(b)
#print()

print(len(valid_bags))


gold_bag = bag_dict[goal]
bag_total = gold_bag.number_of_bags(bag_dict)
print(bag_total)
