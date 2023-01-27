import heapq

class Problem:
    def __init__(self):
        self.initial_state = "Arad"
        self.goal_state = "Bucharest"
        self.edges = {
            "Arad": {"Zerind": 75, "Sibiu": 140, "Timisoara": 118},
            "Zerind": {"Arad": 75, "Oradea": 71},
            "Oradea": {"Zerind": 71, "Sibiu": 151},
            "Sibiu": {"Arad": 140, "Oradea": 151, "Fagaras": 99, "RimnicuVilcea": 80},
            "Timisoara": {"Arad": 118, "Lugoj": 111},
            "Lugoj": {"Timisoara": 111, "Mehadia": 70},
            "Mehadia": {"Lugoj": 70, "Dobreta": 75},
            "Dobreta": {"Mehadia": 75, "Craiova": 120},
            "Craiova": {"Dobreta": 120, "RimnicuVilcea": 146, "Pitesti": 138},
            "RimnicuVilcea": {"Sibiu": 80, "Craiova": 146, "Pitesti": 97},
            "Fagaras": {"Sibiu": 99, "Bucharest": 211},
            "Pitesti": {"RimnicuVilcea": 97, "Craiova": 138, "Bucharest": 101},
            "Bucharest": {"Fagaras": 211, "Pitesti": 101}
        }

    def goal_test(self, state):
        return state == self.goal_state

    def successors(self, state):
        return [(next_state, cost) for next_state, cost in self.edges[state].items()]

    def cost(self, state, action):
        return self.edges[state][action]

def heuristic(state):
    # Euclidean distance from the current state to Bucharest
    # (this is just an example, any other heuristic can be used)
    x1, y1 = state_coordinates[state]
    x2, y2 = state_coordinates["Bucharest"]
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

state_coordinates = {
    "Arad": (91, 492),
    "Zerind": (374, 366),
    "Oradea": (229, 304),
    "Sibiu": (207, 457),
    "Timisoara": (94, 410),
    "Lugoj": (165, 377),
    "Mehadia": (241, 283),
    "Dobreta": (242, 241),
    "Craiova": (253, 205),
    "RimnicuVilcea": (233, 185),
    "Fagaras": (178, 469),
    "Pitesti": (100, 528),
    "Bucharest": (400, 548)
}
