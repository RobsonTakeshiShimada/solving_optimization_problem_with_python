from pyscipopt import Model

model = Model("example")

x = model.addVar('x',vtype='INTEGER')  # Continuous variable x
y = model.addVar('y')  # Continuous variable y  
z = model.addVar('z')  # Integer variable z

model.setObjective(z, sense='maximize')  # Objective function to maximize

model.addCons(z == x+y*x)  # Adding a constraint
model.addCons(-x + 2 * y * x <= 8)  # Adding a constraint
model.addCons(2 * x + y <= 14)  # Adding another constraint
model.addCons(2 * x - y <= 10)  # Adding a third constraint

model.optimize()  # Solve the problem

sol = model.getBestSol()  # Get the best solution

print('x=', sol[x])
print('y=', sol[y])  # Print the values of x and y in the optimal solution