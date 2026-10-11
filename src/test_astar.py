from environment import Environment
from astar import AStarPlanner


environment = Environment(
    width=30,
    height=20
)

start = (2, 2)
goal = (27, 17)

planner = AStarPlanner(environment)

path = planner.find_path(
    start,
    goal
)

if path is None:
    print("No path found.")

else:
    print("Path found!")
    print("Number of positions:", len(path))
    print()
    print("Path:")
    print(path)