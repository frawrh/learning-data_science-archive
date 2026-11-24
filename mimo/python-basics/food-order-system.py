italian_food = ["Pasta Bolognese", "Pepperoni pizza", "Margherita pizza", "Lasagna"]

def find_meal(name, menu):
  if name in menu:
    return name
  else:
    return None

def select_meal(name):
  return find_meal(name, italian_food)

def display_available_meals():
  print("Available Italian Meals: ")
  for food in italian_food:
    print(food)

def create_summary(name, amount):
  order = select_meal(name)
  if order is not None:
    return f"name: {name} amount: {amount}"
  else:
    return "Meal not found"

print("Welcome to the Food Order System!")
display_available_meals()
name_input = input("meal choice: ")
amount_input = input("order quantity: ")

result = create_summary(name_input, amount_input)
print(result)
