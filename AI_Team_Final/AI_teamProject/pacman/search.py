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

from typing import Set
import util
from util import Queue, PriorityQueue, Stack, Counter

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
    return  [s, s, w, s, w, w, s, w]

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
    "* YOUR CODE HERE *"
    closedSet = set()
    fringe = Stack()
    fringe.push((problem.getStartState(),[]))
    while not fringe.isEmpty():
        currentState, path = fringe.pop()
        # Goal Test
        if(problem.isGoalState(currentState)):
            return path
        if(currentState not in closedSet):
            closedSet.add(currentState)
            successors = problem.getSuccessors(currentState)
            for succState, action, stepCost in successors:
                fringe.push((succState,path + [action]))
    return []



def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "* YOUR CODE HERE *"
    closedSet = set()
    fringe = Queue()
    fringe.push((problem.getStartState(),[]))
    while not fringe.isEmpty():
        currentState, path = fringe.pop()
        # print(path)
        # Goal Test
        if(problem.isGoalState(currentState)):
            return path
        if(currentState not in closedSet):
            closedSet.add(currentState)
            successors = problem.getSuccessors(currentState)
            for succState, action, stepCost in successors:
                fringe.push((succState,path + [action]))
    return []



def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def uniformCostSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "* YOUR CODE HERE *"
    closedSet = set()
    fringe = PriorityQueue()
    fringe.push((problem.getStartState(),[], 0), 0)
    while not fringe.isEmpty():
        currentState, path, currCost = fringe.pop()
        # Goal Test
        if(problem.isGoalState(currentState)):
            return path
        if(currentState not in closedSet):
            closedSet.add(currentState)
            successors = problem.getSuccessors(currentState)
            for succState, action, stepCost in successors:
                fringe.push((succState,path + [action], currCost + stepCost), currCost + stepCost)
    return []


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "* YOUR CODE HERE *"
    closedSet = set()
    fringe = PriorityQueue()
    fringe.push((problem.getStartState(),[], 0), 0)
    while not fringe.isEmpty():
        currentState, path, currCost = fringe.pop()
        # Goal Test
        if(problem.isGoalState(currentState)):
            print(currentState)
            return path
        if(currentState not in closedSet):
            closedSet.add(currentState)
            successors = problem.getSuccessors(currentState)
            for succState, action, stepCost in successors:
                fringe.push((succState,path + [action], currCost + stepCost), currCost + stepCost + heuristic(succState, problem))
    return []



def MM(problem, heuristic=nullHeuristic):
    def find_min(open, g):
        f_min = float("inf")
        for index,(_,_,item) in enumerate(open.heap):
            n = item[0]
            f = heuristic(n, problem) + g[n]
            f_min = min(f_min, f)
        return f_min, min(g.values())
    # g_f(n), g_f(n)
    gf,gb = 0,0
    # Declare Forward and Backward fringes using priority queue Data structure.
    openf,openb = PriorityQueue(), PriorityQueue()
    oppositeDir = {'East': 'West', 'North': 'South', 'West': 'East', 'South': 'North'}
    # Forward and backward closed sets.
    closedf, closedb =  {},{}
    # Hash map to store the g values of the nodes
    gfs,gbs = {},{}
    startState = problem.getStartState()
    goalState = problem.getGoalState()
    gfs[startState] = 0
    gbs[goalState] = 0
    U = float("inf")
    eps = 0
    # Push start and goal to the open set with priority = max(f(n), 2* g(n))
    openf.push((startState ,[] ,0 ), max(heuristic(startState, problem), 2 * gf))
    openb.push((goalState, [], 0) , max(heuristic(goalState, problem), 2 * gb))
    while not openf.isEmpty() and not openb.isEmpty():
        # Pop the top elements in both the priority queues
        statef, pathf, gf = openf.pop()
        stateb, pathb, gb = openb.pop()

        # Find which node to be expanded, statef  stateb, by calculating taking minimums of g(n).
        C = min(gf, gb)
        fmin_b, gmin_b = find_min(openb, gbs)
        fmin_f, gmin_f = find_min(openf, gfs)

        # Termination condition. Terminate at the point where we have achieved optimal path hence we can stop.
        if U<=max(C, fmin_f, fmin_b, gmin_b + gmin_f + eps):
            # Calculating the paths to be returned by using the dictionary of closed which store the paths to the node from start/goal.
            if statef == stateb:
                return pathf + [oppositeDir[d] for d in pathb][::-1]
            # IF stateb node was already explored during F expansion we use its stored path from start.
            if stateb in closedf:
                pathf = closedf[stateb]
                return pathf + [oppositeDir[d] for d in pathb][::-1]
            # IF statef node was already explored during b expansion we use its stored path from goal.
            if statef in closedb:
                pathb = closedb[statef]
                return pathf + [oppositeDir[d] for d in pathb][::-1]
        # Node in the forward PQ has smaller g(n)
        if C == gf:
            # Store the path in a hash table to reuse it during termination 
            closedf[statef] = pathf
            successors = problem.getSuccessors(statef)
            # Iterate through the successors of the node in forward PQ.
            for succState, action, stepCost in successors:
                # If the node is in OpenF + ClosedF set and has larger g value, update the g value to the new value 
                # and add it to the PQ.
                if openf.isStatePresentInPQ(succState) or succState in closedf:
                    if gfs[succState] < gf + stepCost:
                        continue
                    if succState in closedf:
                        del closedf[succState]
                    else:
                        openf.deletePQ(succState)
                gf_succ = gf + stepCost
                gfs[succState] = gf_succ
                ff = heuristic(succState, problem) + gf_succ
                # Add the child node to the PQ.
                openf.push((succState, pathf + [action],  max(ff, 2 * gf_succ)), max(ff, 2 * gf_succ))
                # Update U
                if openb.isStatePresentInPQ(succState):
                    U = min(U, gfs[succState] + gbs[succState])
            # Since the node in backward PQ was not used push it back to the queue.
            openb.push((stateb, pathb, gb), gb)
        # Node in the forward Q has smaller g(n)
        else:
            # Store the path in a hash table to reuse it during termination 
            closedb[stateb] = pathb
            successors = problem.getSuccessorsBS(stateb)
            # Iterate through the successors of the node in forward PQ.
            for succState, action, stepCost in successors:
                # If the node is in OpenB + ClosedB set and has larger g value, update the g value to the new value 
                # and add it to the PQ.
                if openb.isStatePresentInPQ(succState) or succState in closedb:
                    if gbs[succState] < gb + stepCost:
                        continue
                    if succState in closedb:
                        del closedb[succState]
                    else:
                        openb.deletePQ(succState)
                gb_succ = gb + stepCost
                gbs[succState] = gb_succ
                fb = heuristic(succState, problem) + gb_succ
                openb.push((succState, pathb + [action],  max(fb, 2 * gb_succ)), max(fb, 2 * gb_succ))
                if openf.isStatePresentInPQ(succState):
                    U = min(U, gfs[succState] + gbs[succState])
            # Since the node in forward PQ was not used push it back to the queue.
            openf.push((statef, pathf, gf), gf)
    return []

def MM0(problem):
    # Since for MM0 h(n)=0 for all n which is nothing but a null heuristic, hecne call the MM with null heuristic to get MM0
    return MM(problem, nullHeuristic)

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
bdmm = MM
bdmm0 = MM0
