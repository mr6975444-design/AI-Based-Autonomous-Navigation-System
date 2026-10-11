
from environment import Environment
from astar import AStarPlanner
from robot import Robot

environment = Environment(width=30, height=20)

start = (2, 2)
goal = (27, 17)

planner = AStarPlanner(environment)
path = planner.find_path(start, goal)

if path is None:
    print("No path found. Robot cannot move.")
else:
    robot = Robot(start)
    robot.set_path(path)

    print("Robot starting position:", robot.position)

    while robot.move_one_step():
        print("Robot moved to:", robot.position)

    print("Robot final position:", robot.position)
    print("Goal reached:", robot.position == goal)
