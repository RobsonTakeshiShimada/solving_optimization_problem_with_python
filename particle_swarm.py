import numpy as np
from scipy.optimize import differential_evolution

def model_obj(x):
    pen = 0
    x0_rounded = np.round(x[0], 0)
    
    # Verificar restrições
    if not (-x0_rounded + 2*x[1]*x0_rounded <= 8): pen = 1e6
    if not (2*x0_rounded + x[1] <= 14): pen = 1e6
    if not (2*x0_rounded - x[1] <= 10): pen = 1e6
    
    # Função objetivo (maximizar x + x*y, então minimizar -(x + x*y))
    return -(x0_rounded + x[1]*x0_rounded) + pen

# Bounds para as variáveis [x, y]
bounds = [(0, 10), (0, 10)]

# Usando Differential Evolution (uma alternativa ao PSO)
result = differential_evolution(model_obj, bounds, seed=42, maxiter=1000)

print('Status:', result.success)
print('x=', np.round(result.x[0], 0))
print('y=', result.x[1])
print('Função objetivo:', -result.fun)  # Negativo porque estávamos minimizando