import heapq

class Node:
    def __init__(self, state, parent=None, action=None, cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.f = 0 # f = g + h, where g is cost and h is heuristic

    def __lt__(self, other):
        return self.f < other.f

def a_star(problem, heuristic):
    start_node = Node(problem.initial_state)
    start_node.f = heuristic(start_node.state)
    frontier = []
    heapq.heappush(frontier, start_node)
    explored = set()
    while frontier:
        node = heapq.heappop(frontier)
        if problem.is_goal_state(node.state):
            path = []
            cost = 0
            while node.parent is not None:
                path.append(node.state)
                cost += node.cost
                node = node.parent
            path.reverse()
            print("Path: ", path)
            print("Cost: ", cost)
            return path, cost
        explored.add(node.state)
        for child in problem.successor_function(node.state):
            if child.state in explored:
                continue
            child.parent = node
            child.f = child.cost + heuristic(child.state)
            heapq.heappush(frontier, child)
    return None, None

# Sample input 1:
class Problem:
    def __init__(self, initial_state):
        self.initial_state = initial_state

    def is_goal_state(self, state):
        if state == "G":
            return True
        return False

    def successor_function(self, state):
        if state == "S":
            return [Node("A", cost=5), Node("B", cost=4), Node("C", cost=3)]
        if state == "A":
            return [Node("D", cost=2), Node("E", cost=6)]
        if state == "B":
            return [Node("F", cost=1), Node("G", cost=2)]
        if state == "C":
            return [Node("G", cost=4)]
        return []

def heuristic(state):
    if state == "S":
        return 0
    if state == "A":
        return 3
    if state == "B":
        return 2
    if state == "C":
        return 3
    if state == "D":
        return 1
    if state == "E":
        return 5
    if state == "F":
        return 0
    if state == "G":
        return 0

p = Problem("S")
path, cost = a_star(p, heuristic)

