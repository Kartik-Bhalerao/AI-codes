# Practical: Model-Based Intelligent Agent for Grid Environment with Obstacles


class ModelBasedGridAgent:

  def __init__(self, grid):
    self.grid = grid  # 0: Free path, 1: Obstacle, 2: Dirty/Goal
    self.rows = len(grid)
    self.cols = len(grid[0])
    self.x, self.y = 0, 0  # Starting position
    self.visited = set()
    self.internal_state = {}  # Internal model tracking world state

  def perceive(self):
    # Perceive current cell status
    return self.grid[self.x][self.y]

  def update_state(self, percept):
    # Update internal state and memory of visited nodes
    self.visited.add((self.x, self.y))
    self.internal_state[(self.x, self.y)] = percept

  def choose_action(self):
    percept = self.perceive()
    self.update_state(percept)

    if percept == 2:  # If cell is dirty
      return "SUCK"

    # Possible movements: Right, Down, Left, Up
    moves = [(0, 1, "RIGHT"), (1, 0, "DOWN"), (0, -1, "LEFT"), (-1, 0, "UP")]

    # First, prioritize unvisited, obstacle-free neighboring cells
    for dx, dy, action in moves:
      nx, ny = self.x + dx, self.y + dy
      if (
          0 <= nx < self.rows
          and 0 <= ny < self.cols
          and self.grid[nx][ny] != 1
          and (nx, ny) not in self.visited
      ):
        return action

    # Fallback: move to any valid adjacent free cell if already visited
    for dx, dy, action in moves:
      nx, ny = self.x + dx, self.y + dy
      if 0 <= nx < self.rows and 0 <= ny < self.cols and self.grid[nx][ny] != 1:
        return action

    return "IDLE"

  def execute_action(self, action):
    if action == "SUCK":
      self.grid[self.x][self.y] = 0  # Clean the cell
      print(f"Action: SUCK at position ({self.x}, {self.y})")
    elif action == "RIGHT":
      self.y += 1
      print(f"Action: Moved RIGHT to ({self.x}, {self.y})")
    elif action == "DOWN":
      self.x += 1
      print(f"Action: Moved DOWN to ({self.x}, {self.y})")
    elif action == "LEFT":
      self.y -= 1
      print(f"Action: Moved LEFT to ({self.x}, {self.y})")
    elif action == "UP":
      self.x -= 1
      print(f"Action: Moved UP to ({self.x}, {self.y})")


# Grid Legend: 0 = Free, 1 = Obstacle, 2 = Dirty
grid_env = [[0, 2, 1, 0], [1, 0, 0, 2], [0, 0, 1, 0], [0, 2, 0, 0]]

agent = ModelBasedGridAgent(grid_env)

print("--- Model-Based Grid Agent Simulation ---\n")
for step in range(10):
  print(f"Step {step + 1}: Current Position = ({agent.x}, {agent.y})")
  action = agent.choose_action()
  if action == "IDLE":
    print("Agent is IDLE. Exploration complete.")
    break
  agent.execute_action(action)
  print()