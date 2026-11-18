# Block world - ABC
from collections import deque


start = (("C", "A"), ("B",))
goal = (("C", "B", "A"),)


def canonical(state):
    """Return a consistent representation by sorting stacks."""
    return tuple(sorted(tuple(stack) for stack in state))


def bfs():
    start_state = canonical(start)
    queue = deque([(start_state, [start_state])])
    visited = {start_state}

    while queue:
        state, path = queue.popleft()

        if state == goal:
            print("Goal State Reached!\n")
            for step, arrangement in enumerate(path):
                print("Step", step, ":", arrangement)
            return

        # Find the top block of every stack.
        for i in range(len(state)):
            block = state[i][-1]

            # Remove the top block.
            remaining = [list(stack) for stack in state]
            remaining[i].pop()
            if not remaining[i]:
                remaining.pop(i)

            # Possible destinations: the table or another stack.
            destinations = [None] + list(range(len(remaining)))
            for dest in destinations:
                new_state = [stack[:] for stack in remaining]

                if dest is None:
                    new_state.append([block])
                else:
                    new_state[dest].append(block)

                new_state = canonical(new_state)
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, path + [new_state]))

    print("No Solution Found")


bfs()
