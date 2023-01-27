class Node:
    def __init__(self, state, parent=None, action=None, cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.children = []

def dfs(node, goal_test):
    if goal_test(node.state,problem):
        return node
    for child in node.children:
        result = dfs(child, goal_test)
        if result is not None:
            return result
    return None

def tree_search(problem, goal_test):
    root = Node(problem.initial_state)
    return dfs(root, goal_test)


class Problem:
    def __init__(self):
        self.initial_state = "A"
        self.goal_state = "F"
        
def goal_test(state,problem):
    return state == problem.goal_state

problem = Problem()

root = Node(problem.initial_state)

# Create the tree structure
root.children = [Node("B", root), Node("C", root), Node("D", root)]
root.children[0].children = [Node("E", root.children[0])]
root.children[2].children = [Node("F", root.children[2])]

result = tree_search(problem, goal_test)

if result is not None:
    path = []
    cost = 0
    node = result
    while node is not None:
        path.append(node.state)
        cost += node.cost
        node = node.parent
    path = path[::-1]
    print(f"Found goal state: {result.state}")
    print(f"Path: {path}")
    print(f"Cost: {cost}")
else:
    print("Goal state not found")
