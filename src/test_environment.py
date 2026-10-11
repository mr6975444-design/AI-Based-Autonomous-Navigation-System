from environment import Environment


environment = Environment()

print("Environment created successfully!")
print("Width:", environment.width)
print("Height:", environment.height)

print(
    "Free position:",
    environment.is_valid((2, 2))
)

print(
    "Obstacle position:",
    environment.is_valid((6, 6))
)