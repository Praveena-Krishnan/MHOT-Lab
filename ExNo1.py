import itertools
import time

# Function to solve TSP using brute force
def tsp_brute_force(graph):
    num_nodes = len(graph)
    nodes = list(range(1, num_nodes))  # Nodes excluding the starting node (0)
    min_cost = float('inf')
    optimal_path = None

    # Start timer
    start_time = time.time()

    # Generate all permutations of nodes except the starting node
    for perm in itertools.permutations(nodes):
        current_path = [0] + list(perm) + [0]  # Cycle back to the starting node
        current_cost = 0

        # Calculate the cost of the current path
        for i in range(len(current_path) - 1):
            current_cost += graph[current_path[i]][current_path[i + 1]]

        # Update the minimum cost and optimal path
        if current_cost < min_cost:
            min_cost = current_cost
            optimal_path = current_path

    # End timer
    end_time = time.time()
    execution_time = end_time - start_time

    return optimal_path, min_cost, execution_time

# Function to solve Hamiltonian Circuit using brute force
def hamiltonian_cycle_brute_force(graph):
    num_nodes = len(graph)
    nodes = list(range(num_nodes))  # All nodes
    min_cost = float('inf')
    optimal_cycle = None

    # Start timer
    start_time = time.time()

    # Generate all permutations of nodes excluding the starting node
    for perm in itertools.permutations(nodes[1:]):  # Permutations of all except node 0
        cycle = [0] + list(perm) + [0]  # Form a cycle
        is_valid = True
        current_cost = 0

        # Check validity and calculate the cost of the cycle
        for i in range(len(cycle) - 1):
            if graph[cycle[i]][cycle[i + 1]] == 0:  # No edge exists
                is_valid = False
                break
            current_cost += graph[cycle[i]][cycle[i + 1]]

        # Update the minimum cost and optimal cycle if valid
        if is_valid and current_cost < min_cost:
            min_cost = current_cost
            optimal_cycle = cycle

    # End timer
    end_time = time.time()
    execution_time = end_time - start_time

    return optimal_cycle, min_cost, execution_time

# Example graph as an adjacency matrix
graph = [
    [0, 20, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 10],
    [45, 40, 30, 0]
]

# Solve TSP
tsp_path, tsp_cost, tsp_time = tsp_brute_force(graph)
print("Travelling Salesman Problem:")
print(f"Optimal Path: {tsp_path}")
print(f"Cost: {tsp_cost}")
print(f"Execution Time: {tsp_time:.6f} seconds\n")

# Solve Hamiltonian Circuit
hamiltonian_path, hamiltonian_cost, hamiltonian_time = hamiltonian_cycle_brute_force(graph)
print("Hamiltonian Circuit:")
print(f"Optimal Cycle: {hamiltonian_path}")
print(f"Cost: {hamiltonian_cost}")
print(f"Execution Time: {hamiltonian_time:.6f} seconds")
