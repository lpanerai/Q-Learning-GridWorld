import pygame
import sys
from GridWorld import GridWorldEnv
from QlearningAgent import QLearningAgent
from  utility import run_simulation

import pygame
import sys
from GridWorld import GridWorldEnv
from QlearningAgent import QLearningAgent
from utility import run_simulation

class PygameGridWorld:
    CELL_SIZE = 20
    MARGIN = 1
    FPS = 5

    def __init__(self, env):
        pygame.init()
        self.env = env
        self.width = env.width * (self.CELL_SIZE + self.MARGIN) + self.MARGIN
        self.height = env.height * (self.CELL_SIZE + self.MARGIN) + self.MARGIN
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("GridWorld Q-Learning")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 24)

    def draw_grid(self, agent_pos):
        self.screen.fill((50, 50, 50))
        for x in range(self.env.width):
            for y in range(self.env.height):
                rect = pygame.Rect(
                    x * (self.CELL_SIZE + self.MARGIN) + self.MARGIN,
                    y * (self.CELL_SIZE + self.MARGIN) + self.MARGIN,
                    self.CELL_SIZE,
                    self.CELL_SIZE
                )
                color = (255, 255, 255)
                if (x, y) in self.env.obstacles:
                    color = (0, 0, 0)
                elif (x, y) == self.env.start:
                    color = (0, 255, 0)
                elif (x, y) == self.env.goal:
                    color = (255, 0, 0)
                pygame.draw.rect(self.screen, color, rect)

        # draw agent
        ax, ay = agent_pos
        agent_rect = pygame.Rect(
            ax * (self.CELL_SIZE + self.MARGIN) + self.MARGIN,
            ay * (self.CELL_SIZE + self.MARGIN) + self.MARGIN,
            self.CELL_SIZE,
            self.CELL_SIZE
        )
        pygame.draw.circle(
            self.screen,
            (0, 0, 255),
            agent_rect.center,
            self.CELL_SIZE // 3
        )

    def render_episode(self, path, episode=None, reward=0):
        for step_count, pos in enumerate(path, start=1):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            # update window title with episode and step
            reward_sum=sum(reward[:step_count])
            if episode is not None:
                pygame.display.set_caption(f"GridWorld Q-Learning - Ep {episode} Step {step_count} Reward {reward_sum}")
            self.draw_grid(pos)
            pygame.display.flip()
            self.clock.tick(self.FPS)

    def close(self):
        pygame.quit()