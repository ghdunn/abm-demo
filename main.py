import random
import matplotlib.pyplot as plt

class Agent:
    def __init__(self, position, state):
        self.position = position
        self.state = state

class Environment:
    def __init__(self, width, height, num_agents):
        self.width = width
        self.height = height
        self.agents = self.initialize_agents(num_agents)

    def initialize_agents(self, num_agents):
        agents = []
        for _ in range(num_agents):
            position = (random.randint(0, self.width - 1), random.randint(0, self.height - 1))
            state = random.choice(['A', 'B'])
            agents.append(Agent(position, state))
        return agents

    def update(self):
        for agent in self.agents:
            new_position = (agent.position[0] + random.choice([-1, 0, 1]), agent.position[1] + random.choice([-1, 0, 1]))
            new_position = (max(0, min(self.width - 1, new_position[0])), max(0, min(self.height - 1, new_position[1])))
            agent.position = new_position

    def display(self):
        grid = [[' ' for _ in range(self.width)] for _ in range(self.height)]
        for agent in self.agents:
            grid[agent.position[1]][agent.position[0]] = agent.state
        for row in grid:
            print(' '.join(row))

def main():
    width, height, num_agents, num_steps = 10, 10, 5, 10
    env = Environment(width, height, num_agents)
    for _ in range(num_steps):
        env.update()
        env.display()
        print()

if __name__ == "__main__":
    main()
