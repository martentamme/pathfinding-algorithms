import os


class Helper:
    _BASE_PATH = os.path.dirname(os.path.abspath(__file__))

    @staticmethod
    def get_neighbours(current_coordinates: tuple, map_matrix: list) -> list[tuple]:
        """
        Find the coordinates on the map where we can move next.
        "*" means there is a wall or other blocker on the map where we can't step.
        """
        neighbours = list()
        row = current_coordinates[0]
        col = current_coordinates[1]
        map_height = len(map_matrix)
        map_width = len(map_matrix[row])

        # Upper
        if row - 1 >= 0 and map_matrix[row - 1][col] != "*":
            neighbours.append((row - 1, col))
        # Left
        if col - 1 >= 0 and map_matrix[row][col - 1] != "*":
            neighbours.append((row, col - 1))
        # Lower
        if row + 1 < map_height and map_matrix[row + 1][col] != "*":
            neighbours.append((row + 1, col))
        # Right
        if col + 1 < map_width and map_matrix[row][col + 1] != "*":
            neighbours.append((row, col + 1))

        return neighbours

    @staticmethod
    def get_path(came_from: dict, goal: tuple) -> list:
        """
        Find a path from the starting point to the goal.
        """
        path = list()
        path.append(goal)
        stop = goal

        while came_from[stop] is not None:
            stop = came_from[stop]
            path.append(stop)

        return list(reversed(path))

    @staticmethod
    def create_line(came_from: dict, goal: tuple, map_matrix: list) -> None:
        """
        This method helps to:
        1. Add the found path to the map.
        2. Save the map with the found path to a file.
        """

        # Add the found path to the map
        next_point = came_from[goal]
        while came_from[next_point] is not None:
            map_matrix[next_point[0]] = str(map_matrix[next_point[0]][:next_point[1]]) + "." \
                                        + str(map_matrix[next_point[0]][next_point[1] + 1:])
            next_point = came_from[next_point]

    @staticmethod
    def manhattan_heuristic(next_point: tuple, goal: tuple) -> int:
        return abs(goal[0] - next_point[0]) + abs(goal[1] - next_point[1])

    @staticmethod
    def chebyshev_heuristic(next_point: tuple, goal: tuple) -> int:
        return max(abs(next_point[0] - goal[0]), abs(next_point[1] - goal[1]))

    @staticmethod
    def write_result_in_file(filename: str, result_map: list) -> None:
        """
        this method writes the map in the file.
        """
        path = f"{Helper._BASE_PATH}/result_maps/{filename}.txt"
        f = open(path, "w")
        f.writelines([f"{line}\n" for line in result_map])

    @staticmethod
    def read_input_map(filename: str) -> list:
        path = f"{Helper._BASE_PATH}/input_maps/{filename}.txt"
        with open(path) as f:
            map_data = [line.strip() for line in f.readlines() if len(line) > 1]
            return map_data

    @staticmethod
    def get_test_map():
        test_map = [
            "*********************************",
            "*     **********************    *",
            "*   *******   D    **********   *",
            "*   *******                     *",
            "* ****************    ***********",
            "************          ********  *",
            "*            ********************",
            "* ********    *******************",
            "*********                   *****",
            "******       ************       *",
            "****               *********    *",
            "**      ******      *************",
            "******************       ********",
            "****      ****            ***** *",
            "*                               *",
            "*                s              *",
            "*********************************"
        ]

        return test_map
