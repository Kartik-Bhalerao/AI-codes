# Practical: 08 BFS 8-Puzzle

from collections import deque


start = (7, 2, 4, 5, 0, 6, 8, 3, 1)
goal = (0, 1, 2, 3, 4, 5, 6, 7, 8)


def bfs():
    queue = deque([(start, [])])
    visited = {start}

    while queue:
        state, path = queue.popleft()

        if state == goal:
            print("Goal Reached!")
            print("Total Moves:", len(path))

            for s in path + [state]:
                for i in range(0, 9, 3):
                    print(s[i:i + 3])
                print()

            return

        zero = state.index(0)
        row, col = divmod(zero, 3)

        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in moves:
            r = row + dr
            c = col + dc

            if 0 <= r < 3 and 0 <= c < 3:
                pos = r * 3 + c
                new_state = list(state)
                new_state[zero], new_state[pos] = (
                    new_state[pos],
                    new_state[zero],
                )
                new_state = tuple(new_state)

                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, path + [new_state]))

    print("No solution found")


bfs()
