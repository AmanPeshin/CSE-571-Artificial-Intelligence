# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent


class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """

    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices)  # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        foods = newFood.asList()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghost_state.scaredTimer for ghost_state in newGhostStates]

        "*** YOUR CODE HERE ***"
        e_value = 100000
        ghostPositions = successorGameState.getGhostPositions()
        for i in range(0, len(ghostPositions)):
            m_dis = manhattanDistance(newPos, ghostPositions[i])
            c_scare_time = newScaredTimes[i]
            if c_scare_time <= 1 and m_dis < 3:
                return -e_value
        x = successorGameState.getNumFood()
        y = currentGameState.getNumFood()
        if x < y:
            return e_value
        else:
            for food in foods:
                d = manhattanDistance(newPos, food)
                min_distance = min(e_value, d)
                val = 1 / min_distance
                return val


def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()


class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn='scoreEvaluationFunction', depth='2'):
        self.index = 0  # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)


class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"

        def min_agent(state, which_agent_will_play, depth):
            moves_list = state.getLegalActions(which_agent_will_play)
            min_score = float("inf")
            m = moves_list
            for action in m:
                next_state = state.generateSuccessor(which_agent_will_play, action)
                which_agent_will_play_new = which_agent_will_play + 1
                depth_new = depth - 1
                min_score = min(min_score, state_or_leaf_value(next_state, which_agent_will_play_new, depth_new))
            return min_score

        def max_agent(state, which_agent_will_play, depth):
            moves_list = state.getLegalActions(which_agent_will_play)
            max_score = float("-inf")
            m = moves_list
            for action in m:
                next_state = state.generateSuccessor(which_agent_will_play, action)
                which_agent_will_play_new = which_agent_will_play + 1
                depth_new = depth - 1
                max_score = max(max_score, state_or_leaf_value(next_state, which_agent_will_play_new, depth_new))
            return max_score

        def state_or_leaf_value(state, agent, depth):
            which_agent_will_play = get_next_agent(agent, state)
            win_cond = state.isWin()
            lose_cond = state.isLose()
            depth_check = depth == 0
            if win_cond or lose_cond or depth_check:
                return self.evaluationFunction(state)
            return max_agent(state, which_agent_will_play, depth) if which_agent_will_play == 0 else min_agent(state, which_agent_will_play, depth)

        def get_next_agent(agent, state):
            n_agent = state.getNumAgents()
            return agent % n_agent

        def get_best_result(next_move_list, game_state_scores):
            best_score = max(game_state_scores)
            for i in range(len(game_state_scores)):
                if game_state_scores[i] == best_score:
                    return next_move_list[i]

        next_move_list = gameState.getLegalActions(0)
        game_state_scores = []
        calculated_depth_based_on_agent = self.depth * gameState.getNumAgents() - 1
        for i in next_move_list:
            game_state_scores.append(state_or_leaf_value(gameState.generateSuccessor(0, i), 1, calculated_depth_based_on_agent))
        return get_best_result(next_move_list, game_state_scores)


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"

        def min_agent(state, which_agent_will_play, depth, alpha, beta):
            min_score = float("inf")
            for move in state.getLegalActions(which_agent_will_play):
                next_state = state.generateSuccessor(which_agent_will_play, move)
                which_agent_will_play_new = which_agent_will_play + 1
                depth_new = depth - 1
                min_score = min(min_score, state_or_leaf_value(next_state, which_agent_will_play_new, depth_new, alpha, beta))
                if min_score < alpha:
                    return min_score
                beta = min(beta, min_score)
            return min_score

        def max_agent(state, which_agent_will_play, depth, alpha, beta):
            max_score = -float("inf")
            for move in state.getLegalActions(which_agent_will_play):
                next_state = state.generateSuccessor(which_agent_will_play, move)
                which_agent_will_play_new = which_agent_will_play + 1
                depth_new = depth - 1
                max_score = max(max_score, state_or_leaf_value(next_state, which_agent_will_play_new, depth_new, alpha, beta))
                if max_score > beta:
                    return max_score
                alpha = max(alpha, max_score)
            return max_score

        def state_or_leaf_value(state, which_agent_will_play, depth, alpha, beta):
            which_agent_will_play = get_next_agent(which_agent_will_play, state)
            win_cond = state.isWin()
            lose_cond = state.isLose()
            depth_check = depth == 0
            if win_cond or lose_cond or depth_check:
                return self.evaluationFunction(state)
            return max_agent(state, which_agent_will_play, depth, alpha, beta) if which_agent_will_play == 0 else min_agent(state, which_agent_will_play, depth, alpha, beta)

        def get_next_agent(agent, state):
            n_agent = state.getNumAgents()
            return agent % n_agent

        next_move_list = gameState.getLegalActions(0)
        calculated_depth_based_on_agent = self.depth * gameState.getNumAgents() - 1
        alpha, beta = -float("inf"), float("inf")
        move = None
        for i in next_move_list:
            score = state_or_leaf_value(gameState.generateSuccessor(0, i), 1, calculated_depth_based_on_agent, alpha, beta)
            if score > alpha:
                alpha = score
                move = i
        return move


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"

        def min_agent(state, which_agent_will_play, depth):
            legal_moves = state.getLegalActions(which_agent_will_play)
            length_of_moves = float(len(legal_moves))
            min_score = 0
            move_probability = 1.0 / length_of_moves
            for action in legal_moves:
                next_state = state.generateSuccessor(which_agent_will_play, action)
                which_agent_will_play_new = which_agent_will_play + 1
                depth_new = depth - 1
                min_score = min_score + move_probability * state_or_leaf_value(next_state, which_agent_will_play_new, depth_new)
            return min_score

        def max_agent(state, which_agent_will_play, depth):
            legal_moves = state.getLegalActions(which_agent_will_play)
            max_score = float("-inf")
            for action in legal_moves:
                next_state = state.generateSuccessor(which_agent_will_play, action)
                which_agent_will_play_new = which_agent_will_play + 1
                depth_new = depth - 1
                max_score = max(max_score, state_or_leaf_value(next_state, which_agent_will_play_new, depth_new))
            return max_score

        def state_or_leaf_value(state, which_agent_will_play, depth):
            which_agent_will_play = get_next_agent(which_agent_will_play, state)
            win_cond = state.isWin()
            lose_cond = state.isLose()
            depth_check = depth == 0
            if win_cond or lose_cond or depth_check:
                return self.evaluationFunction(state)
            return max_agent(state, which_agent_will_play, depth) if which_agent_will_play == 0 else min_agent(state, which_agent_will_play, depth)

        def get_next_agent(agent, state):
            return agent % state.getNumAgents()

        def get_best_result(next_move_list, game_state_scores):
            best_score = max(game_state_scores)
            for i in range(len(game_state_scores)):
                if game_state_scores[i] == best_score:
                    return next_move_list[i]

        next_move_list = gameState.getLegalActions(0)
        game_state_scores = []
        calculated_depth_based_on_agent = self.depth * gameState.getNumAgents() - 1
        for i in next_move_list:
            game_state_scores.append(state_or_leaf_value(gameState.generateSuccessor(0, i), 1, calculated_depth_based_on_agent))
        return get_best_result(next_move_list, game_state_scores)
