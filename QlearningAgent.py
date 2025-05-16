import random

class QLearningAgent:
    """
    Agent using tabular Q-learning with epsilon-greedy policy.
    """
    def __init__(self, env, alpha=0.1, gamma=0.99, epsilon=0.1):
        self.alpha = alpha      # learning rate
        self.gamma = gamma      # discount factor
        self.epsilon = epsilon  # exploration probability
        self.env = env
        # Number of states = number of cells (even if some may be obstacles)
        self.n_states = env.width * env.height
        self.n_actions = 4  # four possible moves
        # Initialize Q-values to zero: matrix n_states × n_actions
        self.Q = [[0.0 for _ in range(self.n_actions)] for _ in range(self.n_states)]

    def state_to_index(self, state):
        """Maps the state (x, y) to an integer index 0..(w*h-1)."""
        x, y = state
        return y * self.env.width + x

    def choose_action(self, state):
        """Selects an action using an ε-greedy policy."""
        if random.random() < self.epsilon:
            # explore: random choice
            return random.choice(range(self.n_actions))
        else:
            # exploit: maximize Q(s,a) with random tie-breaking
            idx = self.state_to_index(state)
            q_vals = self.Q[idx]
            max_q = max(q_vals)
            # actions with maximum Q-value
            best_actions = [i for i, v in enumerate(q_vals) if v == max_q]
            return random.choice(best_actions)

    def update(self, state, action, reward, next_state, done):
        """Updates the Q-table using the Q-learning rule."""
        idx = self.state_to_index(state)
        next_idx = self.state_to_index(next_state)
        old_q = self.Q[idx][action]
        if done:
            target = reward  # if terminal state, no future value
        else:
            target = reward + self.gamma * max(self.Q[next_idx])
        # learning rule
        self.Q[idx][action] = old_q + self.alpha * (target - old_q)