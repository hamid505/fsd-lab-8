
campus = {
    "Hostel": {"Cafeteria": 150, "Admin Block": 300},
    "Cafeteria": {"Academic Block": 200, "Sports Complex": 100},
    "Admin Block": {"Academic Block": 120},
    "Sports Complex": {"Academic Block": 160},
    "Academic Block": {"Library": 100},
    "Library": {}
}

heuristic = {
    "Hostel": 350,
    "Cafeteria": 260,
    "Admin Block": 150,
    "Sports Complex": 220,
    "Academic Block": 90,
    "Library": 0
}


def get_h(path):
    last_node = path[-1]
    return heuristic[last_node]


def get_cost(path):
    total = 0

    for i in range(len(path) - 1):
        current = path[i]
        next_node = path[i + 1]
        total += campus[current][next_node]

    return total


def gbfs(start, goal):
    frontier = [[start]]
    explored_count = 0

    while len(frontier) > 0:
        frontier.sort(key=get_h)
        path = frontier.pop(0)
        node = path[-1]

        explored_count += 1
        print("Exploring:", node, "Path:", path,
              "h =", get_h(path))

        if node == goal:
            print("Total nodes explored:", explored_count)
            return path

        for neighbour in campus[node]:
            if neighbour not in path:
                new_path = path + [neighbour]
                frontier.append(new_path)

    print("Goal not found.")
    return None


answer = gbfs("Hostel", "Library")

if answer is not None:
    print("Path found by GBFS:", answer)
    print("Total distance:", get_cost(answer), "meters")
