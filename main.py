# Example integration into main.py:

from GridWorld import GridWorldEnv
from QlearningAgent import QLearningAgent
from pygame_visualizer import PygameGridWorld
from utility import run_simulation, generate_maze

#MAZE DIMENSION
MAZE_DIM=13
maze=generate_maze(MAZE_DIM)

env = GridWorldEnv(width=MAZE_DIM, height=MAZE_DIM, start=(0, 0), goal=(MAZE_DIM-1, MAZE_DIM-1), obstacles=maze)
agent = QLearningAgent(env, alpha=0.1, gamma=0.99, epsilon=0.25)

episodes = 1000
max_steps = 100
visualize_every = 50
renderer = PygameGridWorld(env)

for ep in range(episodes):
    state = env.reset()
    for t in range(max_steps):
        action = agent.choose_action(state)
        next_state, reward, done = env.step(action)
        agent.update(state, action, reward, next_state, done)
        state = next_state

        if done:
            break

    if (ep + 1) % visualize_every == 0:
        path,reward = run_simulation(agent, env)
        renderer.render_episode(path,episode=ep+1,reward=reward)

# Test phase
agent.epsilon = 0.0
path,reward = run_simulation(agent, env)
renderer.render_episode(path,reward=reward)
renderer.close()