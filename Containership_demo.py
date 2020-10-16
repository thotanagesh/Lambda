class salary:
	def __init__(self,pay):
		self.pay=pay
	def get_total(self):
		return(self.pay*12

class emp:
	def __init__(self,ipay,bonus):
		self.ipay=ipay
		self.bonus=bonus
		self.obj_salary=salary(self.ipay)
	def annual_salary(self):
		return "Total:"+str(self.obj_salary.get_total()+self.bonus)

obj_emp=emp(50000,1000)
print(obj_emp.annual_salary())
