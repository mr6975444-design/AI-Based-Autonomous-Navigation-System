
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from environment import Environment
from astar import AStarPlanner
from robot import Robot


def main():
    environment = Environment(width=30, height=20)

    start = (2, 2)
    goal = (27, 17)

    planner = AStarPlanner(environment)
    path = planner.find_path(start, goal)

    if path is None:
        print("No valid path found!")
        return

    robot = Robot(start)
    robot.set_path(path)

    fig, ax = plt.subplots(figsize=(12, 8))

    ax.imshow(
        environment.grid,
        cmap="gray_r",
        origin="upper",
        vmin=0,
        vmax=1
    )

    path_x = [point[0] for point in path]
    path_y = [point[1] for point in path]

    ax.plot(
        path_x,
        path_y,
        color="blue",
        linewidth=2,
        label="Planned Path"
    )

    ax.scatter(
        *start,
        color="green",
        s=150,
        label="Start"
    )

    ax.scatter(
        *goal,
        color="red",
        s=180,
        marker="*",
        label="Goal"
    )

    robot_marker, = ax.plot(
        [], [],
        marker="s",
        color="orange",
        markersize=12,
        linestyle="None",
        label="Robot"
    )

    status_text = ax.set_title("Autonomous Navigation: Starting")

    ax.set_xlabel("X Position")
    ax.set_ylabel("Y Position")
    ax.set_xticks(range(environment.width))
    ax.set_yticks(range(environment.height))
    ax.grid(True, alpha=0.25)
    ax.legend()
    ax.set_aspect("equal")

    def update(frame):
        if frame < len(path):
            robot.position = path[frame]

        x, y = robot.position

        robot_marker.set_data([x], [y])

        if robot.position == goal:
            status_text.set_text(
                f"Goal Reached! Position: {robot.position}"
            )
        else:
            status_text.set_text(
                f"Robot Position: {robot.position}"
            )

        return robot_marker, status_text

    animation = FuncAnimation(
        fig,
        update,
        frames=len(path),
        interval=250,
        repeat=False,
        blit=False
    )

    # Keep a reference so the animation stays active.
    fig._navigation_animation = animation

    plt.tight_layout()
    plt.show()

    print("Simulation finished.")
    print("Goal reached:", robot.position == goal)


if __name__ == "__main__":
    main()
