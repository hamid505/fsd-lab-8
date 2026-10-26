
graph = {
    "S": {"A": 6, "B": 5, "C": 10},
    "A": {"E": 6},
    "B": {"E": 6, "D": 7},
    "C": {"D": 6},
    "D": {"F": 6},
    "E": {"F": 4},
    "F": {"G": 3},
    "G": {}
}

heuristic = {
    "S": 17, "A": 10, "B": 13, "C": 4,
    "D": 2, "E": 4, "F": 1, "G": 0
}

def get_g(path):
    total = 0
    for i in range(len(path) - 1):
        current_node = path[i]
        next_node = path[i + 1]
        total += graph[current_node][next_node]
    return total

def get_h(path):
    last_node = path[-1]
    return heuristic[last_node]

def get_f(path):
    return get_g(path) + get_h(path)

def a_star(start, goal):
    frontier = [[start]]
    explored_count = 0

    while len(frontier) > 0:
        frontier.sort(key=get_f)
        path = frontier.pop(0)
        node = path[-1]

        explored_count += 1

        print("Exploring:", node,
              "Path:", path,
              "g =", get_g(path),
              "h =", get_h(path),
              "f =", get_f(path))

        if node == goal:
            print("Total nodes explored:", explored_count)
            return path

        for neighbour in graph[node]:
            new_path = path + [neighbour]
            frontier.append(new_path)

    print("Goal not found.")
    return None
answer = a_star("S", "G")

if answer is not None:
    print("Path found by A*:", answer)
    print("Total cost of this path:", get_g(answer))
