class Fruit:
	def __init__(self, data = {"color": "unknown"}):
		self._data = data

	def set_color(self, color: str):
		self._data["color"] = color

	def print_data(self):
		print(f"I'm { self._data.get('color') }")


orange = Fruit()
orange.set_color("orange")
orange.print_data()


apple = Fruit()
apple.print_data()
