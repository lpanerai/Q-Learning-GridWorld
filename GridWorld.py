class GridWorldEnv:
    """
    5x5 GridWorld environment: the state is the agent's position (x, y).
    The agent starts at `start` and must reach `goal`. Reward values:
    +10 at the goal, -1 for each valid step, -5 for hitting a wall/obstacle.
    """
    def __init__(self, width=5, height=5, start=(0, 0), goal=(4, 4), obstacles=None):
        self.width = width
        self.height = height
        self.start = start        # initial state
        self.goal = goal          # goal state
        self.obstacles = obstacles if obstacles is not None else []  # list of obstacle positions
        self.reset()

    def reset(self):
        """Resets the environment and returns the initial state."""
        self.agent_pos = self.start
        return self.agent_pos

    def step(self, action):
        """
        Executes the action (0=up, 1=down, 2=left, 3=right).
        Returns (next_state, reward, done).
        """
        x, y = self.agent_pos
        # Compute attempted position based on the action
        if action == 0:      new_pos = (x,   y-1)  # up (y decreases)
        elif action == 1:    new_pos = (x,   y+1)  # down (y increases)
        elif action == 2:    new_pos = (x-1, y)    # left (x decreases)
        elif action == 3:    new_pos = (x+1, y)    # right (x increases)
        else:
            raise ValueError("Invalid action.")

        # Check boundaries: if out of grid, stay and apply penalty
        if (new_pos[0] < 0 or new_pos[0] >= self.width or
            new_pos[1] < 0 or new_pos[1] >= self.height):
            reward = -5   # wall
            next_state = self.agent_pos
            done = False
        else:
            # If within bounds, check for obstacles
            if new_pos in self.obstacles:
                reward = -5  # obstacle
                next_state = self.agent_pos
                done = False
            else:
                # Valid move
                self.agent_pos = new_pos
                if new_pos == self.goal:
                    reward = 10  # goal reached
                    done = True
                else:
                    reward = -1  # step cost
                    done = False

        return self.agent_pos, reward, done