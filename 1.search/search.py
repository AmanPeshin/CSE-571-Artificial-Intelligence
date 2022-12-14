# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

    frontier = util.Stack()
    explored = []
    path = []
    initial_state = problem.getStartState()

    if problem.isGoalState(initial_state):
        return []

    frontier.push((initial_state, path))

    while frontier.isEmpty() != True:
        considered_node, path = frontier.pop()
        explored.append(considered_node)

        if problem.isGoalState(considered_node):
            return path

        children_nodes = problem.getSuccessors(considered_node)

        if children_nodes:
            for child_node in children_nodes:
                child_node_xy = child_node[0]
                if child_node_xy not in explored:
                    updated_path_to_child = path + [child_node[1]]
                    frontier.push((child_node_xy, updated_path_to_child))
    return []
    util.raiseNotDefined()


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    frontier = util.Queue()
    explored = []
    path = []
    initial_state = problem.getStartState()

    if problem.isGoalState(initial_state):
        return []

    frontier.push((initial_state, path))

    while frontier.isEmpty() != True:
        considered_node, path = frontier.pop()
        explored.append(considered_node)

        if problem.isGoalState(considered_node):
            return path

        children_nodes = problem.getSuccessors(considered_node)

        if children_nodes:
            for child_node in children_nodes:
                child_node_xy = child_node[0]
                frontier_check_list = (i[0] for i in frontier.list)
                if child_node_xy not in explored and child_node_xy not in frontier_check_list:
                    updated_path_to_child = path + [child_node[1]]
                    frontier.push((child_node_xy, updated_path_to_child))

    return []
    util.raiseNotDefined()


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    initial_state = problem.getStartState()
    explored = []
    path = []
    frontier = util.PriorityQueue()

    if problem.isGoalState(initial_state):
        return []

    frontier.push((initial_state, path, 0), 0)

    while frontier.isEmpty() != True:
        considered_node, path, cost = frontier.pop()

        if problem.isGoalState(considered_node):
            return path

        if considered_node not in explored:
            explored.append(considered_node)
            children = problem.getSuccessors(considered_node)
            for child in children:
                child_node_xy = child[0]
                updated_path_to_child = path + [child[1]]
                updated_cost_to_child = cost + child[2]
                frontier.push((child_node_xy, updated_path_to_child, updated_cost_to_child), updated_cost_to_child)

    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    explored = []
    frontier = util.PriorityQueue()
    path = []
    initial_state = problem.getStartState()
    initial_state_heuristic = heuristic(initial_state, problem)

    if problem.isGoalState(initial_state):
        return []
    priority = 0
    frontier.push((initial_state, path, priority), priority + initial_state_heuristic)

    while frontier.isEmpty() != True:
        considered_node, path, cost = frontier.pop()

        if problem.isGoalState(considered_node):
            return path

        if considered_node not in explored:
            explored.append(considered_node)
            children = problem.getSuccessors(considered_node)
            for child in children:
                child_node_xy = child[0]
                heuristic_cost_of_child = heuristic(child_node_xy, problem)
                updated_path_to_child = path + [child[1]]
                updated_cost_to_child = cost + child[2]
                f_n_cost = updated_cost_to_child + heuristic_cost_of_child
                frontier.push((child_node_xy, updated_path_to_child, updated_cost_to_child), f_n_cost)

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
