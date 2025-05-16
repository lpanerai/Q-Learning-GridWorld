# utility.py

import random

max_simulation_steps = 100

def run_simulation(agent, env):
    stato_corrente = env.reset()
    percorso = [stato_corrente]
    reward_list=[]
    done = False
    while not done:
        azione = agent.choose_action(stato_corrente)
        stato_successivo, reward, done = env.step(azione)
        percorso.append(stato_successivo)
        reward_list.append(reward)
        stato_corrente = stato_successivo
    return percorso[:max_simulation_steps],reward_list[:max_simulation_steps]


def generate_maze(size):
    if size % 2 == 0:
        raise ValueError("La dimensione deve essere un numero dispari per garantire il corretto funzionamento.")
    
    maze = [[1] * size for _ in range(size)]  # 1 = muro, 0 = percorso

    start = (0, 0)
    maze[start[1]][start[0]] = 0

    def neighbors(x, y):
        for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < size and 0 <= ny < size:
                yield nx, ny

    stack = [start]
    while stack:
        x, y = stack[-1]
        unvisited = [(nx, ny) for nx, ny in neighbors(x, y) if maze[ny][nx] == 1]
        if unvisited:
            nx, ny = random.choice(unvisited)
            maze[(y + ny) // 2][(x + nx) // 2] = 0
            maze[ny][nx] = 0
            stack.append((nx, ny))
        else:
            stack.pop()

    walls = [(x, y) for y in range(size) for x in range(size) if maze[y][x] == 1]
    return walls

# Esempio di utilizzo
muri_100 = generate_maze(101)  # Genera un labirinto 101x101 (dimensione dispari)