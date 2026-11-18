# Practical: Alpha Beta Pruning
def alphabeta(node, depth, alpha, beta, maximizing):
  if isinstance(node, int):
    return node
  if maximizing:
    best = float("-inf")
    for child in node:
      value = alphabeta(child, depth + 1, alpha, beta, False)
      best = max(best, value)
      alpha = max(alpha, best)
      if beta <= alpha:
        print("Pruned:", node)
        break
    return best
  else:
    best = float("inf")
    for child in node:
      value = alphabeta(child, depth + 1, alpha, beta, True)
      best = min(best, value)
      beta = min(beta, best)
      if beta <= alpha:
        print("Pruned:", node)
        break
    return best


tree = [[[2, 3], [5, 9]], [[0, 1], [7, 5]]]
result = alphabeta(tree, 0, float("-inf"), float("inf"), True)
print("Optimal Value:", result)