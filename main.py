# Example integration into main.py:

from GridWorld import GridWorldEnv
from QlearningAgent import QLearningAgent
from pygame_visualizer import PygameGridWorld
from utility import run_simulation

env = GridWorldEnv(width=10, height=10, start=(9, 9), goal=(0, 0), obstacles=[(1, 2),(3, 3),(3,7),(5, 3),(6, 6)])
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