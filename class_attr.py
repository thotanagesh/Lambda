class person():
	"""docstring for person"""
	def __init__(self, name,age):
		self.name = name
		self.age=age
		
	def show(self):
		print('Name:',self.name)
		print("Age:",self.age)

p=person('Ravi Teja',19
print(hasattr(p,p.name))
#print(hasattr(p,p.sec))
print(getattr(p,p.name))
print(getattr(p,p.age,20))
print(setattr(p,'name1','rt'))
