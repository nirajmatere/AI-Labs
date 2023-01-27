class Node:
    def __init__(self, state, parent=None, action=None, cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.children = []

def dfs(node, goal_test):
    if goal_test(node.state):
        return node
    for child in node.children:
        result = dfs(child, goal_test)
        if result is not None:
            return result
    return None

def tree_search(problem, goal_test):
    root = Node(problem.initial_state)
    queue = [root]
    while len(queue) > 0:
        current_node = queue.pop(0)
        if goal_test(current_node.state):
            return current_node
        children = problem.get_children(current_node.state)
        for child_state, action, cost in children:
            child_node = Node(child_state, current_node, action, cost)
            current_node.children.append(child_node)
            queue.append(child_node)
    return None

def get_path(node):
    path = []
    cost = 0
    while node is not None:
        path.append(node.state)
        cost += node.cost
        node = node.parent
    return path[::-1], cost

class Problem:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state
    def get_children(self, state):
        children = []
        if state == "A":
            children.append(("B", "left", 1))
            children.append(("C", "right", 2))
        elif state == "B":
            children.append(("D", "up", 3))
            children.append(("E", "down", 4))
        elif state == "C":
            children.append(("F", "up", 5))
            children.append(("G", "down", 6))
        return children


# Example usage:
problem = Problem("A", "F")
goal_node = tree_search(problem, lambda state: state == problem.goal_state)
if goal_node is not None:
    path, cost = get_path(goal_node)
    print("Found goal state:", goal_node.state)
    print("Path:", path)
    print("Cost:", cost)
else:
    print("Goal state not found")
