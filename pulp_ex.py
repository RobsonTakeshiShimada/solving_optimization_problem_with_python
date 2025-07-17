import pulp as pl

model = pl.LpProblem("Example_Problem", pl.LpMaximize)

x = pl.LpVariable("x", 0, 10)
y = pl.LpVariable("y", 0, None)

# constraints
model += -x + 2 * y <= 8
model += 2*x + y <= 14
model += 2*x - y <= 10
# objective function
model += x + y

status = model.solve()

x_value = pl.value(x)
y_value = pl.value(y)

print(f"Status: {pl.LpStatus[status]}")
print(f"x = {x_value}, y = {y_value}")
print(f"Objective value = {pl.value(model.objective)}")
