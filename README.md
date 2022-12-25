# Python OOP Weirdness

Take this Python code:
```python
class Fruit:
	def __init__(self, data = {"color": "unknown"}):
		self.data = data

	def set_color(self, color: str):
		self.data["color"] = color

	def print_color(self):
		print(f"I'm { self.data.get('color') }")


orange = Fruit() # new instance of Fruit class
orange.set_color("orange") # Set the color
orange.print_color() # Prints "I'm orange"
```

It is a simple example of object oriented programming.  
We delcare a class called `Fruit`, create an instance of the class (called `orange`), and then set that instance's color with the `set_color()` method.  
Then we use the `print_color()` method to print the instance's `color` attribute in the `data` dictionary.  
In this example it is expected that we see `I'm orange` printed to the console. But what happens if we create a new instance of that class without setting a color?

```python
class Fruit:
	def __init__(self, data = {"color": "unknown"}):
		self.data = data

	def set_color(self, color: str):
		self.data["color"] = color

	def print_color(self):
		print(f"I'm { self.data.get('color') }")


orange = Fruit() # new instance of Fruit class
orange.set_color("orange") # Set the color
orange.print_color() # Prints "I'm orange"


apple = Fruit() # new instance of Fruit class
# We don't set the apple's color
apple.print_color() # ????
```

We would logically expect `apple.print_color()` to print `I'm unknown` to the console, since we are setting the `color` attribute of the `data` variable to `"unknown"`...  
But for some stupid reason it prints out `I'm orange`.  

I have created and tested programs in JavaScript and C++ with the same structure and they preform much more logically. I am going to do more research into this weird behavior of Python.

