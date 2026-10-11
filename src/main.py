
from pathlib import Path

from environment import Environment
from astar import AStarPlanner
from robot import Robot
from visualization import draw_environment


def main():
    print("=" * 45)
    print("AI-BASED AUTONOMOUS NAVIGATION SYSTEM")
    print("=" * 45)

    environment = Environment(width=30, height=20)

    start = (2, 2)
    goal = (27, 17)

    print("Environment created.")
    print("Start:", start)
    print("Goal:", goal)

    planner = AStarPlanner(environment)
    path = planner.find_path(start, goal)

    if path is None:
        print("No path found!")
        return

    print("Path found!")
    print("Number of positions:", len(path))

    robot = Robot(start)
    robot.set_path(path)

    while robot.move_one_step():
        pass

    print("Robot final position:", robot.position)
    print("Goal reached:", robot.position == goal)

    project_root = Path(__file__).resolve().parent.parent
    output_directory = project_root / "outputs"
    output_directory.mkdir(exist_ok=True)

    image_path = output_directory / "navigation_result.png"

    draw_environment(
        environment=environment,
        start=start,
        goal=goal,
        path=path,
        robot_position=robot.position,
        save_path=str(image_path)
    )


if __name__ == "__main__":
    main()
