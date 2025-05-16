# README

## Project Overview

This project implements a Q-learning agent that learns to navigate a 2D GridWorld environment to reach a goal while avoiding obstacles. It provides a real-time animations with Pygame (`pygame_visualizer.py`) to display the agent’s trajectory during training and testing.

## Directory Structure

```
project/
├── GridWorld.py            # GridWorld environment definition
├── QlearningAgent.py       # Q-learning agent implementation
├── utility.py              # Utility functions: simulation and Matplotlib visualization
├── main.py                 # Training and testing script with Matplotlib
├── pygame_visualizer.py    # Training and testing with Pygame animation
├── README.md               # Project documentation
└── requirements.txt        # Python dependencies
```

## Dependencies

Install the following Python libraries:

* `pygame` (for real-time rendering)

Example `requirements.txt`:

```
pygame>=2.0
```

Install via:

```bash
pip install -r requirements.txt
```

## Module Descriptions

### 1. GridWorld.py

* **`GridWorldEnv`**: Defines the grid environment with start, goal, and obstacle positions.

  * `reset()`: Resets the agent to the start position.
  * `step(action)`: Executes an action (up, down, left, right) and returns `(next_state, reward, done)`.

### 2. QlearningAgent.py

* **`QLearningAgent`**: Implements tabular Q-learning with an ε-greedy policy.

  * Parameters:

    * `alpha`: Learning rate
    * `gamma`: Discount factor
    * `epsilon`: Exploration probability
  * Methods:

    * `choose_action(state)`: Selects an action using ε-greedy.
    * `update(state, action, reward, next_state, done)`: Updates the Q-table.

### 3. utility.py

* `visualize_gridworld(env, path, episode=None)`: Draws the grid and agent’s path using Matplotlib.
* `run_simulation(agent, env)`: Simulates a full episode following the current policy.

### 4. main.py

* Runs the training loop for a specified number of episodes, updating the Q-table.
* Every `visualize_every` episodes, it prints progress and displays the current path with Matplotlib.
* After training, runs a test episode with `epsilon=0.0` and visualizes the final path.

### 5. pygame\_visualizer.py

* **`PygameGridWorld`**: Renders the environment and agent’s movement step-by-step using Pygame.

  * `render_episode(path, episode)`: Animates the path and updates the window title with the episode and step count.
* Mirrors `main.py` logic but visualizes in a Pygame window.

## Customization

* **Grid Dimensions**: Modify `width` and `height` in `GridWorldEnv`.
* **Learning Parameters**: Adjust `alpha`, `gamma`, and `epsilon` in `QLearningAgent`.
* **Visualization Frequency**: Change `visualize_every` in both `main.py` and `pygame_visualizer.py`.
* **Graphics Settings**: Customize colors, cell size, and FPS in `utility.py` and `pygame_visualizer.py`.

## Contributing

Contributions, issues, and pull requests are welcome! Please update this `README.md` with any new features or changes.

