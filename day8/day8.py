class computer:
  
  def __init__(self, instructions):
    self.reg = 0
    self.ip = 0
    self.instructions = instructions
    self.history = set()
    
  def run(self, suppressWarnings):
    opCodes = {
      'nop': self.nop,
      'acc': self.acc,
      'jmp': self.jmp,
    }
    
    while True:
      if self.ip in self.history:
        if not suppressWarnings:
          print(f'Loop breaking. Reg {self.reg}')
        return False
      if self.ip > len(self.instructions):
        print(f'Instruction {self.ip} not found.')
        return False
      
      self.history.add(self.ip)
      op, val = self.instructions[self.ip].split()
      opCodes[op](int(val))
      self.ip += 1
      
      if self.ip == len(self.instructions):
        print(f'Booting finished. Reg {self.reg}')
        return True
      
  def nop(self, val):
    pass
    
  def acc(self, val):
    self.reg += val
    
  def jmp(self, val):
    self.ip += val - 1 # -1 to account for normal step)
    
instructions = [line.strip() for line in open('input.txt').readlines()]

for i, line in enumerate(instructions):
  if line[:3] == 'acc':
    continue
  
  if line[:3] == 'nop':
    newIns = instructions.copy()
    newIns[i] = 'jmp ' + line[4:]
  else:
    newIns = instructions.copy()
    newIns[i] = 'nop 0'
    
  comp = computer(newIns)
  
  if comp.run(True):
    break