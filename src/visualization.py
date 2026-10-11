
import matplotlib.pyplot as plt


def draw_environment(environment, start, goal, path=None,
                     robot_position=None, save_path=None):

    fig, ax = plt.subplots(figsize=(12, 8))

    ax.imshow(
        environment.grid,
        cmap="gray_r",
        origin="upper",
        vmin=0,
        vmax=1
    )

    if path:
        path_x = [point[0] for point in path]
        path_y = [point[1] for point in path]

        ax.plot(
            path_x,
            path_y,
            color="blue",
            linewidth=2.5,
            label="Planned Path"
        )

    ax.scatter(
        start[0], start[1],
        color="green",
        s=150,
        marker="o",
        label="Start"
    )

    ax.scatter(
        goal[0], goal[1],
        color="red",
        s=180,
        marker="*",
        label="Goal"
    )

    if robot_position is not None:
        ax.scatter(
            robot_position[0],
            robot_position[1],
            color="orange",
            s=150,
            marker="s",
            label="Robot"
        )

    ax.set_title("AI-Based Autonomous Navigation System")
    ax.set_xlabel("X Position")
    ax.set_ylabel("Y Position")

    ax.set_xticks(range(environment.width))
    ax.set_yticks(range(environment.height))
    ax.grid(True, alpha=0.25)
    ax.legend()
    ax.set_aspect("equal")

    fig.tight_layout()

    if save_path:
        fig.savefig(save_path, dpi=200, bbox_inches="tight")
        print("Image saved to:", save_path)

    plt.show()
    plt.close(fig)
