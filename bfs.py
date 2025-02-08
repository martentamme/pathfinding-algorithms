from queue import Queue

from helper import Helper


class BFS:

    def __init__(self, input_map: list, start_coordinates: tuple, goal_coordinates: tuple, result_filename: str = None):
        self.map = input_map
        self.start = start_coordinates
        self.goal = goal_coordinates
        self.result_filename = result_filename
        self.result_map = self.map.copy()

    def run_algorithm(self):
        iteration = 0
        queue = Queue()

        # Add a starting point
        queue.put(self.start)
        came_from: dict[tuple, tuple | None] = {self.start: None}

        while not queue.empty():
            iteration += 1
            current = queue.get()

            # Goal found
            if current == self.goal:
                # It returns:
                # 1. Number of iterations
                # 2. Path (list of coordinates starting with the start point and ending with the goal)
                # 2.1. It also saves a file that includes the map and the path

                # Visualize the result
                if self.result_filename:
                    Helper.create_line(came_from, self.goal, self.result_map)
                    Helper.write_result_in_file(self.result_filename, self.result_map)

                path = Helper.get_path(came_from, self.goal)
                return iteration, path

            # Find the next steps (depth)
            neighbours = Helper.get_neighbours(current, self.map)
            for neighbour in neighbours:
                # Avoid visiting neighbors you have already visited
                if neighbour not in came_from:
                    came_from[neighbour] = current
                    queue.put(neighbour)

        # The entire map has been traversed, but the goal has not been found.
        return "There is no solution!"


if __name__ == '__main__':
    test_map = Helper.get_test_map()
    start = (15, 17)
    goal = (2, 14)
    search = BFS(
        input_map=test_map,
        start_coordinates=start,
        goal_coordinates=goal,
        result_filename="test_map_bfs"
    )
    iterations, path = search.run_algorithm()
    print(f"Iterations: {iterations}")
    print(f"Path: {path}")
