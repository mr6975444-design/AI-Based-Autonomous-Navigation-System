
# AI-Based Autonomous Navigation System 🤖

## Project Overview

The AI-Based Autonomous Navigation System is a Python-based project that simulates a virtual robot navigating through a 2D environment containing obstacles.

The system uses the A* (A-Star) path-planning algorithm to calculate a route from a starting position to a destination while avoiding obstacles. The robot then follows the calculated path, and Matplotlib visualizes the navigation environment.

This project provides a foundation for learning autonomous robotics, path planning, and simulation without requiring physical robot hardware.

## Features

- 2D grid-based environment simulation
- Obstacle creation and detection
- A* path-planning algorithm
- Virtual robot movement
- Start and goal position configuration
- Navigation path visualization
- Animated robot simulation

## Technologies Used

- Python
- NumPy
- Matplotlib
- OpenCV

## Project Structure

```text
AI-Autonomous-Navigation-System/
├── src/
│   ├── environment.py
│   ├── astar.py
│   ├── robot.py
│   ├── visualization.py
│   ├── simulation.py
│   ├── main.py
│   ├── test_environment.py
│   ├── test_astar.py
│   └── test_robot.py
├── outputs/
│   └── navigation_result.png
├── screenshots/
├── videos/
├── docs/
├── notebooks/
├── models/
├── data/
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation and Setup

### 1. Install Python

Install Python 3 and verify the installation:

```bash
python3 --version
```

### 2. Clone or Open the Project

Open the project folder in Visual Studio Code.

### 3. Create a Virtual Environment

```bash
python3 -m venv venv
```

Activate the environment on macOS or Linux:

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## How to Run

Run these commands from the main project folder.

### Run the Navigation System

```bash
python src/main.py
```

This calculates a path, moves the virtual robot through the planned positions, and displays the navigation environment.

The resulting visualization is saved to:

```text
outputs/navigation_result.png
```

### Run the Animated Simulation

```bash
python src/simulation.py
```

This opens a Matplotlib animation of the virtual robot following its planned path.

## How the System Works

1. **Environment Creation:** A 2D grid represents free space and obstacles.
2. **Path Planning:** The A* algorithm searches for a valid path from the start to the goal.
3. **Robot Movement:** The virtual robot follows the positions in the calculated path.
4. **Visualization:** Matplotlib displays the map, obstacles, route, start, and destination.
5. **Result Verification:** The program checks whether the robot reaches the goal.

## A* Path Planning

The A* algorithm evaluates possible routes using the following cost function:

**f(n) = g(n) + h(n)**

Where:

- `g(n)` is the cost of travelling from the start to the current position.
- `h(n)` is the estimated cost from the current position to the goal.
- `f(n)` is the total estimated cost.

This implementation uses Manhattan distance as its heuristic and allows movement in four directions: up, down, left, and right.

## Example Configuration

```python
start = (2, 2)
goal = (27, 17)

environment = Environment(width=30, height=20)
```

The program has successfully found a 41-position path for this configuration in the current test environment.

## Current Project Status

- [x] Virtual environment setup
- [x] 2D environment creation
- [x] Obstacle representation
- [x] A* path planning
- [x] Virtual robot movement
- [x] Navigation visualization
- [ ] Verify animated simulation
- [ ] Add project screenshots
- [ ] Publish project on GitHub
- [ ] Implement advanced obstacle avoidance

## Future Improvements

- Dynamic obstacle avoidance
- OpenCV-based image processing
- Camera-based perception
- Object detection using a lightweight model
- Improved robot movement and control
- Integration with ROS or CARLA
- Testing in a more realistic simulation environment
- Optional physical robot implementation

## Learning Outcomes

This project demonstrates practical experience with:

- Python programming
- Search algorithms and path planning
- Grid-based environment modelling
- Basic autonomous robot simulation
- Data visualization
- Software project organization

## Author

**Your Name**

Add your project links here after publishing:

- GitHub: Your GitHub profile URL
- Project Repository: Your repository URL
