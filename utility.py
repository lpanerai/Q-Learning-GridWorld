# utility.py
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