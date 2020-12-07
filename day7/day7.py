rules = [x.strip() for x in open('input.txt').readlines()]

TARGET = "shiny gold"

class colour:
	def __init__(self, name):
		self.name = name
		self.parents = []
		self.children = {}
		
	def addParent(self, parent):
		self.parents.append(parent)
	
	def addChild(self, child, count):
		self.children[child] = count
	
	def allAncestors(self):
		ancestorNames = {p.name for p in self.parents}
		for p in self.parents:
			ancestorNames = ancestorNames.union(p.allAncestors())
		return ancestorNames
	
	def allChildren(self):
		childrenHist = self.children.copy()
		for child, mult in self.children.items():
			grandchildren = child.allChildren()
			for gc, count in grandchildren.items():
				childrenHist[gc] = childrenHist.get(gc, 0) + count * mult
		return childrenHist
				
		
bagRules = {}
	
def parseRule(rule):
	# light red bags contain 1 bright white bag, 2 muted yellow bags.
	parent, allChildren = rule.split(' contain ')
	# parent = 'light red bags'
	# children = '1 bright white bag, 2 muted yellow bags.'
	parent = parent[:-5]
	children = [child[:-4].strip().split(' ', maxsplit=1) for child in allChildren.rstrip('s.').split(', ')]

	if parent not in bagRules.keys():
		bagRules[parent] = colour(parent)
	
	if allChildren != 'no other bags.':
		for count, child in children:
			if child not in bagRules.keys():
				bagRules[child] = colour(child)
			
			bagRules[parent].addChild(bagRules[child], int(count))
			bagRules[child].addParent(bagRules[parent])

for rule in rules:
	parseRule(rule)

targetBag = bagRules[TARGET]

print(sum(targetBag.allChildren().values()))

