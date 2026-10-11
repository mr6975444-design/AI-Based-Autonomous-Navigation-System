
class Robot:
    def __init__(self, start):
        self.position = start
        self.path = []
        self.path_index = 0

    def set_path(self, path):
        self.path = path
        self.path_index = 0

    def move_one_step(self):
        if self.path_index >= len(self.path):
            return False

        self.position = self.path[self.path_index]
        self.path_index += 1
        return True

    def reached_goal(self):
        return (
            self.path_index >= len(self.path)
            and len(self.path) > 0
        )
