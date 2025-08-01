import pyomo.environ as pyo
from pyomo.environ import *
from pyomo.opt import SolverFactory

model = pyo.ConcreteModel()

model.x = pyo.Var(bounds=(0,10))
model.y = pyo.Var(bounds=(0,10))
x = model.x
y = model.y

model.C1 = pyo.Constraint(expr = -x + 2*y*x <= 8)
model.C2 = pyo.Constraint(expr = 2*x + y <= 14)
model.C3 = pyo.Constraint(expr = 2*x - y <= 10)

model.obj = pyo.Objective(expr = x + y*x, sense=pyo.maximize)

opt = SolverFactory('ipopt',executable='C:\\Ipopt-3.11.1-win64-intel13.1\\bin\\ipopt.exe')
opt.solve(model)

model.pprint()

x_value = pyo.value(model.x)
y_value = pyo.value(model.y)

print(f"Optimal solution: x = {x_value}, y = {y_value}")