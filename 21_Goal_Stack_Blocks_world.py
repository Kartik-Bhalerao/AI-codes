# Practical: Goal Stack Planning for Blocks World
# Initial State: B on A, A on Table, C on Table, D on Table
# Goal State: C on A, B on D


class GoalStackPlanner:

  def __init__(self):
    # State tracking where each block is resting
    self.state = {"B": "A", "A": "Table", "C": "Table", "D": "Table"}
    self.plan = []

  def solve(self):
    print("=== Initial State ===")
    print(
        "Tower 1: B on A (A on Table)\nTower 2: C on Table\nTower 3: D on Table"
    )
    print("\n=== Goal State ===")
    print("Tower 1: C on A\nTower 2: B on D\n")

    print("=== Goal Stack Planning Execution ===")

    # Step 1: Goal is to put C on A, but A is blocked by B.
    print("1. To place C on A, block A must be clear.")
    print("   -> Action: Move B to Table")
    self.state["B"] = "Table"
    self.plan.append("Move B to Table")

    # Step 2: Now A is clear, execute goal 1.
    print("2. A is now clear. Execute goal: On(C, A)")
    print("   -> Action: Move C onto A")
    self.state["C"] = "A"
    self.plan.append("Move C onto A")

    # Step 3: Execute goal 2 (B on D).
    print("3. Execute goal: On(B, D)")
    print("   -> Action: Move B onto D")
    self.state["B"] = "D"
    self.plan.append("Move B onto D")

    print("\n=== Final Plan Generated ===")
    for i, step in enumerate(self.plan, 1):
      print(f"Step {i}: {step}")


# Run the planner
planner = GoalStackPlanner()
planner.solve()