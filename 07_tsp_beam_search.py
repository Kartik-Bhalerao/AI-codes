# Practical: Traveling Salesman Problem
cities = {"A": (0, 0), "B": (2, 3), "C": (5, 4), "D": (6, 1), "E": (3, 0)}


def distance(a, b):
  x1, y1 = cities[a]
  x2, y2 = cities[b]
  return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def cost(path):
  total = 0
  for i in range(len(path)):
    total += distance(path[i], path[(i + 1) % len(path)])
  return total


def beam_search(k=3, iterations=100):
  beam = [list(cities.keys())]
  for _ in range(iterations):
    candidates = []
    for path in beam:
      for i in range(1, len(path)):
        for j in range(i + 1, len(path)):
          new_path = path.copy()
          new_path[i], new_path[j] = new_path[j], new_path[i]
          candidates.append(new_path)
    candidates.sort(key=cost)
    beam = candidates[:k]
  best = min(beam, key=cost)
  print("Best Path:", best + [best[0]])
  print("Minimum Distance:", round(cost(best), 2))


beam_search()