# Practical: Minimax Algorithm for Game-Playing Agent
# Tree structure matching the chit diagram


def minimax(depth, node_index, is_max_player, scores):
  # Base case: leaf node reached (depth 2)
  if depth == 2:
    return scores[node_index]

  if is_max_player:
    best = -float("inf")
    for i in range(3):
      val = minimax(depth + 1, node_index * 3 + i, False, scores)
      best = max(best, val)
    return best

  else:
    best = float("inf")
    for i in range(3):
      val = minimax(depth + 1, node_index * 3 + i, True, scores)
      best = min(best, val)
    return best


# Leaf node utility values from the image diagram:[cite: 2]
# A1 children: [3, 12, 8]
# A2 children: [2, 4, 6]
# A3 children: [14, 5, 2]
leaf_scores = [3, 12, 8, 2, 4, 6, 14, 5, 2]

print("--- Minimax Algorithm Execution ---")
print("Leaf Node Scores:", leaf_scores)

# Evaluate each branch explicitly for clear output display
a1_val = min(leaf_scores[0:3])  # min(3, 12, 8) = 3
a2_val = min(leaf_scores[3:6])  # min(2, 4, 6) = 2
a3_val = min(leaf_scores[6:9])  # min(14, 5, 2) = 2

print(f"Branch A1 (MIN evaluated): {a1_val}")
print(f"Branch A2 (MIN evaluated): {a2_val}")
print(f"Branch A3 (MIN evaluated): {a3_val}")

optimal_value = max(a1_val, a2_val, a3_val)  # max(3, 2, 2) = 3
print(f"\nRoot MAX Optimal Decision Value: {optimal_value}")