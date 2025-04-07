def objective_function(x):
    return -x**2+4*x
def get_neighbors(x, step_size):
    return [x + step_size, x - step_size]
def hill_climbing (start, step_size=0.1, max_iteration = 5):
    current_state=start
    current_value = objective_function(current_state)
    print(f"Initial state (x) :{current_state}")
    for iteration in range (max_iteration):
        neighbors = get_neighbors(current_state , step_size )
        best_neighbor=None
        best_value=current_value
        for neighbor in neighbors:
            neighbor_value=objective_function(neighbor)
            if neighbor_value >best_value:
                best_neighbor = neighbor
                best_value = neighbor_value
        if best_neighbor is not None and best_value > current_value:
            current_state = best_neighbor
            current_value=best_value
            print(f"Iteration {iteration +1}: New current state (x):{current_state},f(x):{current_value}")
        else:
            print(f"Iteration {iteration + 1}: No better neighbors ,stopping.")
            break
    print(f"Final state(x):{current_state}")
    print(f" Final value of f(x):{current_value}")
hill_climbing(start = 0, step_size = 0.1, max_iteration=100)
