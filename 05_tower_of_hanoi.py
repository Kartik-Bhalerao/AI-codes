# Practical: Tower of Hanoi
from collections import deque


def solve_hanoi(n):
  start = tuple([0] * n)
  goal = tuple([2] * n)
  queue = deque([(start, [])])
  visited = {start}
  while queue:
    state, path = queue.popleft()
    if state == goal:
      print("Solution Found!")
      print("Total Moves:", len(path))
      for move in path:
        print(move)
      return
    for peg in range(3):
      disks = [i for i in range(n) if state[i] == peg]
      if not disks:
        continue
      disk = min(disks)
      for target in range(3):
        if target == peg:
          continue
        target_disks = [i for i in range(n) if state[i] == target]
        if target_disks and min(target_disks) < disk:
          continue
        new_state = list(state)
        new_state[disk] = target
        new_state = tuple(new_state)
        if new_state not in visited:
          visited.add(new_state)
          new_path = path + [
              f"Move disk {disk + 1} from Rod {peg + 1} to Rod {target + 1}"
          ]
          queue.append((new_state, new_path))


solve_hanoi(4)