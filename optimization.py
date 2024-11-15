import numpy as np
from scipy.optimize import linprog

def optimize_inventory(demand_forecast, cost_params):
    """
    Optimize inventory levels based on demand forecast and cost parameters.
    """
    num_items = len(demand_forecast)

    # Objective function coefficients (holding costs)
    c = cost_params['holding_cost'] * np.ones(num_items)

    # Inequality constraints (inventory >= demand)
    A = -np.eye(num_items)
    b = -demand_forecast

    # Bounds on inventory levels (non-negative)
    x_bounds = [(0, None) for _ in range(num_items)]

    # Solve the linear programming problem
    res = linprog(c, A_ub=A, b_ub=b, bounds=x_bounds, method='highs')

    if res.success:
        optimal_inventory = res.x
        return optimal_inventory
    else:
        raise ValueError('Optimization failed:', res.message)