import heapq


class AStarPlanner:

    def __init__(self, environment):
        self.environment = environment

    def heuristic(self, current, goal):
        x1, y1 = current
        x2, y2 = goal

        return abs(x1 - x2) + abs(y1 - y2)

    def get_neighbors(self, position):
        x, y = position

        possible_moves = [
            (x + 1, y),
            (x - 1, y),
            (x, y + 1),
            (x, y - 1)
        ]

        neighbors = []

        for neighbor in possible_moves:
            if self.environment.is_valid(neighbor):
                neighbors.append(neighbor)

        return neighbors

    def reconstruct_path(self, came_from, current):
        path = [current]

        while current in came_from:
            current = came_from[current]
            path.append(current)

        path.reverse()

        return path

    def find_path(self, start, goal):

        open_set = []

        heapq.heappush(open_set, (0, start))

        came_from = {}

        g_score = {
            start: 0
        }

        f_score = {
            start: self.heuristic(start, goal)
        }

        while open_set:

            _, current = heapq.heappop(open_set)

            if current == goal:
                return self.reconstruct_path(
                    came_from,
                    current
                )

            for neighbor in self.get_neighbors(current):

                tentative_g_score = (
                    g_score[current] + 1
                )

                if (
                    neighbor not in g_score
                    or tentative_g_score < g_score[neighbor]
                ):

                    came_from[neighbor] = current

                    g_score[neighbor] = tentative_g_score

                    f_score[neighbor] = (
                        tentative_g_score
                        + self.heuristic(
                            neighbor,
                            goal
                        )
                    )

                    heapq.heappush(
                        open_set,
                        (
                            f_score[neighbor],
                            neighbor
                        )
                    )

        return None