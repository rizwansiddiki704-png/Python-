class car :
	def __init__(self,make,model,year):
		self.make= make
		self.model= model
		self.year= year
		
	def get_descriptive_name(self):
			long_name=f"{self.make} , {self.model} , {self.year}"
			return long_name.title()
class ElectricCar(car):
	def __init__(self,make,model,year):
			super().__init__(make,model,year)
			pass
			