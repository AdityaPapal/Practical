class Node:
    def __init__(self, position, parent=None, cost=0, heuristic=0):
        self.position = position
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

    def total_cost(self):
        return self.cost + self.heuristic

def heuristic(node, goal):
    # Manhattan distance heuristic
    return abs(node.position[0] - goal[0]) + abs(node.position[1] - goal[1])

def astar(grid, start, goal):
    open_list = []
    closed_set = set()

    start_node = Node(start, None, 0, heuristic(Node(start), goal))
    open_list.append(start_node)

    while open_list:
        current_node = min(open_list, key=lambda node: node.total_cost())
        open_list.remove(current_node)

        if current_node.position == goal:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        closed_set.add(current_node.position)

        for next_move in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_position = (current_node.position[0] + next_move[0], current_node.position[1] + next_move[1])

            if new_position[0] < 0 or new_position[0] >= len(grid) or new_position[1] < 0 or new_position[1] >= len(grid[0]) or grid[new_position[0]][new_position[1]] == 1:
                continue

            if new_position in closed_set:
                continue

            new_node = Node(new_position, current_node, current_node.cost + 1, heuristic(Node(new_position), goal))

            open_list.append(new_node)

    return None

# Example usage:
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]
start = (0, 0)
goal = (4, 4)

path = astar(grid, start, goal)
if path:
    print("Path found:", path)
else:
    print("No path found")
