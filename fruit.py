class Fruit:
	def __init__(self, data = {"color": "unknown"}):
		self.data = data

	def set_color(self, color: str):
		self.data["color"] = color

	def print_color(self):
		print(f"I'm { self.data.get('color') }")


orange = Fruit()
orange.set_color("orange")
orange.print_color() # Prints "I'm orange"


apple = Fruit()
apple.print_color() # ????
