# Practical: Vacuum Cleaner World
environment = {"A": "Dirty", "B": "Dirty"}
location = "A"


def vacuum_agent(location, status):
  if status == "Dirty":
    return "SUCK"
  elif location == "A":
    return "RIGHT"
  else:
    return "LEFT"


for step in range(5):
  status = environment[location]
  action = vacuum_agent(location, status)
  print(f"\nStep: {step + 1}")
  print(f"Location: {location}")
  print(f"Status: {status}")
  print(f"Action: {action}")

  if action == "SUCK":
    environment[location] = "Clean"
  elif action == "RIGHT":
    location = "B"
  elif action == "LEFT":
    location = "A"
  print("Environment:", environment)

print("\nFinal Environment:", environment)