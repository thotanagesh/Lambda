from abc import ABC,abstractmethod

class abs(ABC):
	@abstractmethod
	def display(self):
		print('IN ABSTRACT METHOD')

class B(abs):
	def display(self):
		super().display()
		print('IN CLASS B')

obj=B()
obj.display()

#output

'''IN ABSTRACT METHOD
IN CLASS B'''