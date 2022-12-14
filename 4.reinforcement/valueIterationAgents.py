# valueIterationAgents.py
# -----------------------
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


# valueIterationAgents.py
# -----------------------
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


import mdp, util

from learningAgents import ValueEstimationAgent
import collections


class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """

    def __init__(self, mdp, discount=0.9, iterations=100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter()  # A Counter is a dict with default 0
        self.runValueIteration()

    def runValueIteration(self):
        # Write value iteration code here
        "*** YOUR CODE HERE ***"

        i = 0
        total_iterations = self.iterations
        while (i < total_iterations):
            value_store = self.values.copy()
            state_dict = self.mdp.getStates()
            for s in state_dict:
                value_to_beat = -99999999999
                all_actions_dict = self.mdp.getPossibleActions(s)
                value_store[s] = self.updateValue(all_actions_dict, s, value_to_beat)
            self.values = value_store
            i += 1

    def updateValue(self, all_actions_dict, s, value_to_beat):
        if not all_actions_dict:
            value_to_beat = 0
        else:
            for action in all_actions_dict:
                computed_Q = self.computeQValueFromValues(s, action)
                current = computed_Q
                value_to_beat = current if value_to_beat < current else value_to_beat
        return value_to_beat

    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]

    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        reward = 0
        transition_states = self.mdp.getTransitionStatesAndProbs(state, action)
        for nstate in transition_states:
            s_dash = nstate[0]
            prob = nstate[1]
            is_terminal = self.mdp.isTerminal(s_dash)
            rew = self.mdp.getReward(state, action, s_dash)
            if is_terminal:
                reward = (prob * 1) * rew
            else:
                dis = self.discount
                val = self.values[s_dash]
                dis_val = dis * val
                calculated = (prob * rew) + (prob * dis_val)
                reward = reward + calculated

        return reward

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
        s = state
        val_dict = [None, -999999]
        actions_dict = self.mdp.getPossibleActions(s)

        for i in actions_dict:
            Q_val = self.computeQValueFromValues(s, i)
            if Q_val > val_dict[1]:
                val_dict[0] = i
                val_dict[1] = Q_val

        return val_dict[0]

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)


class AsynchronousValueIterationAgent(ValueIterationAgent):
    """
        * Please read learningAgents.py before reading this.*

        An AsynchronousValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs cyclic value iteration
        for a given number of iterations using the supplied
        discount factor.
    """

    def __init__(self, mdp, discount=0.9, iterations=1000):
        """
          Your cyclic value iteration agent should take an mdp on
          construction, run the indicated number of iterations,
          and then act according to the resulting policy. Each iteration
          updates the value of only one state, which cycles through
          the states list. If the chosen state is terminal, nothing
          happens in that iteration.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state)
              mdp.isTerminal(state)
        """
        ValueIterationAgent.__init__(self, mdp, discount, iterations)

    def runValueIteration(self):
        "*** YOUR CODE HERE ***"

        i = 0
        max_iteration = self.iterations
        while i < max_iteration:
            num_states = self.mdp.getStates()
            index = i % len(num_states)
            s = self.mdp.getStates()[index]
            v = -999999
            temp3 = self.upd_val(s, v)
            self.values[s] = temp3
            i = i + 1

    def upd_val(self, s, v):
        possible_actions = self.mdp.getPossibleActions(s)
        if not possible_actions:
            v = 0
        else:
            action_dict = self.mdp.getPossibleActions(s)
            for action in action_dict:
                q_val = self.computeQValueFromValues(s, action)
                if v < self.computeQValueFromValues(s, action):
                    v = self.computeQValueFromValues(s, action)

        return v


class PrioritizedSweepingValueIterationAgent(AsynchronousValueIterationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A PrioritizedSweepingValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs prioritized sweeping value iteration
        for a given number of iterations using the supplied parameters.
    """

    def __init__(self, mdp, discount=0.9, iterations=100, theta=1e-5):
        """
          Your prioritized sweeping value iteration agent should take an mdp on
          construction, run the indicated number of iterations,
          and then act according to the resulting policy.
        """
        self.theta = theta
        ValueIterationAgent.__init__(self, mdp, discount, iterations)

    def runValueIteration(self):
        "*** YOUR CODE HERE ***"

        mdp_states = self.mdp.getStates()
        pQueue = util.PriorityQueue()
        pred = {}

        for ith_state in mdp_states:
            pred[ith_state] = set()

        pred = self.addStatesToPred(mdp_states, pred)


        for ste in mdp_states:
            is_terminal = self.mdp.isTerminal(ste)
            if not is_terminal:
                state_val = self.values[ste]
                Qval = -999999
                mdp_actions1 = self.mdp.getPossibleActions(ste)
                self.updateQueueState(pQueue, mdp_actions1, ste, state_val, Qval)

        i = 0
        while i < self.iterations:
            if pQueue.isEmpty():
                break
            self.qUpdateForSelfValues(pQueue, pred)
            i = i + 1

    def qUpdateForSelfValues(self, pQueue, pred):
        s = pQueue.pop()

        if not self.mdp.isTerminal(s):
            value = -999999
            temp = self.upd_val(s, value)
            self.values[s] = temp
        pred_s = pred[s]
        stateInPred = pred_s

        for p in stateInPred:
            mdpActions = self.mdp.getPossibleActions(p)
            diff = self.values[p]
            initQVal = -999999

            for act in mdpActions:
                qVal = self.computeQValueFromValues(p, act)
                initQVal = qVal if qVal > initQVal else initQVal
            temp = (diff - initQVal)
            diff = abs(temp)
            pQueue.update(p, -diff) if diff > self.theta else None

    def updateQueueState(self, pQueue, mdp_actions1, ste, state_val, Qval):
        for action in mdp_actions1:
            qVal = self.computeQValueFromValues(ste, action)
            Qval = self.computeQValueFromValues(ste, action) if qVal > Qval else Qval
        temp = (state_val - Qval)
        difference = abs(temp)
        temp1 = -difference
        pQueue.push(ste, temp1)

    def upd_val(self, s, value):
        if self.mdp.getPossibleActions(s):
            for a in self.mdp.getPossibleActions(s):
                Val = self.computeQValueFromValues(s, a)
                value = Val if value < self.computeQValueFromValues(s, a) else value
        else:
            value = 0
        return value

    def addStatesToPred(self, mdp_states, pred):
        for ste in mdp_states:
            actions_from_state = self.mdp.getPossibleActions(ste)
            for act in actions_from_state:
                trans_states = self.mdp.getTransitionStatesAndProbs(ste, act)
                for tState in trans_states:
                    x = tState[0]
                    pred[x].add(ste)
        return pred
