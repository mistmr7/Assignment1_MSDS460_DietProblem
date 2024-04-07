from pulp import LpProblem, LpVariable, LpMinimize

# Define food items
food_items = {
    "Veggie mix": {
        "calories": 4000,
        "protein": 192,
        "sodium": 7570,
        "potassium": 13160,
        "iron": 42.8,
        "vitamin_d": 100,
        "calcium": 2160,
        "cost": 28.81,
    },
    "Milk": {
        "calories": 140,
        "protein": 13,
        "sodium": 280,
        "potassium": 550,
        "iron": 1,
        "vitamin_d": 5,
        "calcium": 380,
        "cost": 4.49,
    },
    "Eggs": {
        "calories": 70,
        "protein": 6,
        "sodium": 70,
        "potassium": 70,
        "iron": 0.9,
        "vitamin_d": 1,
        "calcium": 30,
        "cost": 0.16625,
    },
    "Chicken": {
        "calories": 110,
        "protein": 23,
        "sodium": 220,
        "potassium": 250,
        "iron": 0.7,
        "vitamin_d": 0,
        "calcium": 0,
        "cost": 0.93,
    },
    "Rice": {
        "calories": 160,
        "protein": 3,
        "sodium": 5,
        "potassium": 63,
        "iron": 0,
        "vitamin_d": 0,
        "calcium": 2,
        "cost": 0.10,
    },
}

# Define target nutritional values
target_calories = 35000
target_protein = 350
target_potassium = 32900
target_iron = 126
target_vitamin_d = 140
target_calcium = 9100
target_sodium = 35000

# Create a LP minimization problem
prob = LpProblem("Nutrition Optimization", LpMinimize)

# Define decision variables
food_vars = LpVariable.dicts("Food", food_items, lowBound=0, cat="Continuous")

# Define the objective function (minimize cost)
prob += sum(food_items[food]["cost"] * food_vars[food] for food in food_items)

# Add constraints
prob += (
    sum(food_items[food]["calories"] * food_vars[food] for food in food_items)
    >= target_calories
)
prob += (
    sum(food_items[food]["protein"] * food_vars[food] for food in food_items)
    >= target_protein
)
prob += (
    sum(food_items[food]["potassium"] * food_vars[food] for food in food_items)
    >= target_potassium
)
prob += (
    sum(food_items[food]["iron"] * food_vars[food] for food in food_items)
    >= target_iron
)
prob += (
    sum(food_items[food]["vitamin_d"] * food_vars[food] for food in food_items)
    >= target_vitamin_d
)
prob += (
    sum(food_items[food]["calcium"] * food_vars[food] for food in food_items)
    >= target_calcium
)
prob += (
    sum(food_items[food]["sodium"] * food_vars[food] for food in food_items)
    <= target_sodium
)

# Add constraint to use at least one of every food item
for food in food_items:
    prob += food_vars[food] >= 1

# Solve the optimization problem
prob.solve()

# Print the results
print("Optimal food choices:")
for food in food_items:
    if food_vars[food].value() > 0:
        print(f"{food}: {food_vars[food].value()}")

# Print nutritional values for targets
print("\nNutritional values for targets:")
print(
    f"Total calories: {sum(food_items[food]['calories'] * food_vars[food].value() for food in food_items)}"
)
print(
    f"Total protein: {sum(food_items[food]['protein'] * food_vars[food].value() for food in food_items)} grams"
)
print(
    f"Total potassium: {sum(food_items[food]['potassium'] * food_vars[food].value() for food in food_items)} mg"
)
print(
    f"Total iron: {sum(food_items[food]['iron'] * food_vars[food].value() for food in food_items)} mg"
)
print(
    f"Total Vitamin D: {sum(food_items[food]['vitamin_d'] * food_vars[food].value() for food in food_items)} mcg"
)
print(
    f"Total calcium: {sum(food_items[food]['calcium'] * food_vars[food].value() for food in food_items)} mg"
)
print(
    f"Total sodium: {sum(food_items[food]['sodium'] * food_vars[food].value() for food in food_items)} mg"
)
