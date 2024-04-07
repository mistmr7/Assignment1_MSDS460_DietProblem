from pulp import LpVariable, LpProblem, LpStatus, value, LpMinimize


Vg = LpVariable("Vg", 0, None)  # Veggie Mix >= 0
Mk = LpVariable("Mk", 0, None)  # Milk >= 0
Eg = LpVariable("Eg", 0, None)  # Eggs >= 0
Ck = LpVariable("Ck", 0, None)  # Chicken >= 0
Ri = LpVariable("Ri", 0, None)  # Rice >= 0

prob = LpProblem("problem", LpMinimize)


# Set the Constraints
prob += (
    4000 * Vg + 140 * Mk + 70 * Eg + 110 * Ck + 160 * Ri >= 14000
)  # Calories >= 2000/day
prob += (
    7570 * Vg + 280 * Mk + 70 * Eg + 220 * Ck + 5 * Ri <= 35000
)  # Sodium <= 5000mg/day
prob += 192 * Vg + 13 * Mk + 6 * Eg + 23 * Ck + 3 * Ri >= 350  # Protein >= 50g/day
prob += 42.8 * Vg + 1 * Mk + 0.9 * Eg + 0.7 * Ck + 0 * Ri >= 126  # Iron >= 18 mg/day
prob += (
    13160 * Vg + 550 * Mk + 70 * Eg + 250 * Ck + 63 * Ri >= 32900
)  # Potassium >= 4700mg/day
prob += 100 * Vg + 5 * Mk + 1 * Eg + 0 * Ck + 0 * Ri >= 140  # Vitamin D >= 20 mcg/day
prob += (
    2160 * Vg + 380 * Mk + 30 * Eg + 0 * Ck + 2 * Ri >= 9100
)  # Calcium >= 1300mg/day

prob += 28.81 * Vg + 4.49 * Mk + 0.16625 * Eg + 0.93 * Ck + 0.1 * Ri

status = prob.solve()
LpStatus[status]

print("Ideal pulp solution for Vg, Mk, Eg, Ck, Ri")
print(value(Vg))
print(value(Mk))
print(value(Eg))
print(value(Ck))
print(value(Ri))


Vg = LpVariable("Vg", 1, None)  # Veggie Mix >= 1
Mk = LpVariable("Mk", 7, None)  # Milk >= 7
Eg = LpVariable("Eg", 1, None)  # Eggs >= 1
Ck = LpVariable("Ck", 7, None)  # Chicken >= 7
Ri = LpVariable("Ri", 1, None)  # Rice >= 1

prob = LpProblem("problem", LpMinimize)

# Set the Constraints
prob += (
    4000 * Vg + 140 * Mk + 70 * Eg + 110 * Ck + 160 * Ri >= 14000
)  # Calories >= 2000/day
prob += (
    7570 * Vg + 280 * Mk + 70 * Eg + 220 * Ck + 5 * Ri <= 35000
)  # Sodium <= 5000mg/day
prob += 192 * Vg + 13 * Mk + 6 * Eg + 23 * Ck + 3 * Ri >= 350  # Protein >= 50g/day
prob += 42.8 * Vg + 1 * Mk + 0.9 * Eg + 0.7 * Ck + 0 * Ri >= 126  # Iron >= 18 mg/day
prob += (
    13160 * Vg + 550 * Mk + 70 * Eg + 250 * Ck + 63 * Ri >= 32900
)  # Potassium >= 4700mg/day
prob += 100 * Vg + 5 * Mk + 1 * Eg + 0 * Ck + 0 * Ri >= 140  # Vitamin D >= 20 mcg/day
prob += (
    2160 * Vg + 380 * Mk + 30 * Eg + 0 * Ck + 2 * Ri >= 9100
)  # Calcium >= 1300mg/day

prob += 28.81 * Vg + 4.49 * Mk + 0.16625 * Eg + 0.93 * Ck + 0.1 * Ri

status = prob.solve()
LpStatus[status]

print(
    "Ideal pulp solution for Vg, Mk, Eg, Ck, Ri with minimum 7 cups of milk,\n7 servings of chicken and at least 1 of each."
)
print(value(Vg))
print(value(Mk))
print(value(Eg))
print(value(Ck))
print(value(Ri))


Vg = LpVariable("Vg", 1, None)  # Veggie Mix >= 1
Mk = LpVariable("Mk", 1, None)  # Milk >= 7
Eg = LpVariable("Eg", 1, 35)  # 35 >= Eggs >= 1
Ck = LpVariable("Ck", 1, None)  # Chicken >= 1
Ri = LpVariable("Ri", 1, 21)  # 21 >= Rice >= 1

prob = LpProblem("problem", LpMinimize)


# Set the Constraints
prob += (
    4000 * Vg + 140 * Mk + 70 * Eg + 110 * Ck + 160 * Ri >= 14000
)  # Calories >= 2000/day
prob += (
    7570 * Vg + 280 * Mk + 70 * Eg + 220 * Ck + 5 * Ri <= 35000
)  # Sodium <= 5000mg/day
prob += 192 * Vg + 13 * Mk + 6 * Eg + 23 * Ck + 3 * Ri >= 350  # Protein >= 50g/day
prob += 42.8 * Vg + 1 * Mk + 0.9 * Eg + 0.7 * Ck + 0 * Ri >= 126  # Iron >= 18 mg/day
prob += (
    13160 * Vg + 550 * Mk + 70 * Eg + 250 * Ck + 63 * Ri >= 32900
)  # Potassium >= 4700mg/day
prob += 100 * Vg + 5 * Mk + 1 * Eg + 0 * Ck + 0 * Ri >= 140  # Vitamin D >= 20 mcg/day
prob += (
    2160 * Vg + 380 * Mk + 30 * Eg + 0 * Ck + 2 * Ri >= 9100
)  # Calcium >= 1300mg/day

prob += 28.81 * Vg + 4.49 * Mk + 0.16625 * Eg + 0.93 * Ck + 0.1 * Ri

status = prob.solve()
LpStatus[status]

print(
    "Realistic Ideal pulp solution for Vg, Mk, Eg, Ck, Ri, capping eggs at 5 per day and rice at 3 servings per day"
)
print(value(Vg))
print(value(Mk))
print(value(Eg))
print(value(Ck))
print(value(Ri))
