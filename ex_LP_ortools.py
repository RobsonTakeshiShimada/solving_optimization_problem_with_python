from ortools.linear_solver import pywraplp

solver = pywraplp.Solver.CreateSolver('GLOP')

# Define the variables
x = solver.NumVar(0, 10, 'x') # This variable x can take values between 0 and 10
y = solver.NumVar(0, 10, 'y') # This variable y can take values between 0 and 10

solver.Add(-x+2*y <= 8 )  # Adding a constraint
solver.Add(2*x+y<= 14)  # Adding another constraint
solver.Add(2*x-y<=10)  # Adding a third constraint

solver.Maximize(x+y)  # Objective function to maximize

results = solver.Solve()  # Solve the problem

if results ==pywraplp.Solver.OPTIMAL:
    print('Optimnal solution found:')

print('x:', x.solution_value())
print('y:', y.solution_value())