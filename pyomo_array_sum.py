import pyomo.environ as pyo
from pyomo.environ import *
from pyomo.opt import SolverFactory
import pandas as pd

# input data
dataGen = pd.read_excel('inputs.xlsx', sheet_name='gen')
dataLoad = pd.read_excel('inputs.xlsx', sheet_name='load')

Ng = len(dataGen)

# model
model = pyo.ConcreteModel()

model.Pg = pyo.Var(range(Ng),bounds=(0, None))

Pg = model.Pg

# constraints
# Power balance constraint
pg_sum = sum([Pg[g] for g in dataGen.id])
model.balance = pyo.Constraint(expr = pg_sum == sum(dataLoad.value))
# Generation limits: only generators 0 and 3 can produce power to load point 0
model.cond = pyo.Constraint(expr = Pg[0]+Pg[3] >= dataLoad.value[0])

model.limits = pyo.ConstraintList()
for g in dataGen.id:
    model.limits.add(expr = Pg[g] <= dataGen.limit[g]) 

# objFun
cost_sum = sum([dataGen.cost[g] for g in dataGen.id])
model.obj = pyo.Objective(expr = cost_sum)

opt = SolverFactory('glpk')
print("Solver available:", opt.available())
results = opt.solve(model)
print("Solver status:", results.solver.status)
print("Termination condition:", results.solver.termination_condition)

dataGen['Pg'] = [pyo.value(Pg[g]) for g in dataGen.id]
print(dataGen)