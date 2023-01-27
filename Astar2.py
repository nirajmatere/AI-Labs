import heapq

class Node:
    def __init__(self, state, parent=None, action=None, cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.priority = float('inf')
        self.children = []

class Problem:
    def __init__(self, initial_state, goal_state, actions, cost):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.actions = actions
        self.cost = cost

    def goal_test(self, state):
        return state == self.goal_state

    def heuristic(self, state):
        # Implement your heuristic function here
        pass

def a_star(problem):
    start = Node(problem.initial_state)
    start.priority = problem.heuristic(start.state)
    heap = [start]
    visited = set()
    while heap:
        node = heapq.heappop(heap)
        if problem.goal_test(node.state):
            return construct_path(node), node.cost
        if node.state in visited:
            continue
        visited.add(node.state)
        for action in problem.actions(node.state):
            child = Node(problem.result(node.state, action), node, action, node.cost + problem.cost(node.state, action, action))
            child.priority = node.cost + problem.cost(node.state, action, action) + problem.heuristic(child.state)
            heapq.heappush(heap, child)
    return None

def construct_path(node):
    path = []
    while node is not None:
        path.append(node.state)
        node = node.parent
    return path[::-1]

# Example usage
initial_state = 'A'
goal_state = 'G'
actions = lambda state: ['B', 'C', 'D'] if state == 'A' else ['E', 'F']
cost = lambda state, action, result: 1

problem = Problem(initial_state, goal_state, actions, cost)
path, cost = a_star(problem)
print(path)
print(cost)
