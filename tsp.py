from sys import maxsize
from itertools import permutations
import matplotlib.pyplot as plt

# Number of cities
v = 4

# Coordinates of cities for plotting (x, y)
city_coords = [(0, 0), (2, 3), (5, 2), (6, 6)]

# Distance graph (can also be generated using coordinates)
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

def traveling_salesman_path(graph, starting_point):
    vertex = [i for i in range(v) if i != starting_point]
    min_path_cost = maxsize
    best_path = []

    for perm in permutations(vertex):
        current_cost = 0
        k = starting_point
        for i in perm:
            current_cost += graph[k][i]
            k = i
        current_cost += graph[k][starting_point]

        if current_cost < min_path_cost:
            min_path_cost = current_cost
            best_path = [starting_point] + list(perm) + [starting_point]

    return best_path, min_path_cost

def plot_path(path, coords):
    x = [coords[i][0] for i in path]
    y = [coords[i][1] for i in path]

    plt.figure(figsize=(6,6))
    plt.plot(x, y, marker='o', linestyle='-', color='blue', linewidth=2)

    for i, city in enumerate(path):
        plt.text(coords[city][0], coords[city][1], f'{city}', fontsize=12, ha='right', va='bottom')

    plt.title("Shortest Traveling Salesman Path")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show()

# Run
starting_point = 0
best_path, cost = traveling_salesman_path(graph, starting_point)
print("Shortest Path:", best_path)
print("Minimum Cost:", cost)

plot_path(best_path, city_coords)
