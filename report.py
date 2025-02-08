import time

from a_star import A_star
from bfs import BFS
from greedy import Greedy
from helper import Helper


class Report:

    @staticmethod
    def get_map_statistics(map_name: str, start, goal):
        map_data = Helper.read_input_map(map_name)

        # BFS
        algorithm_name = "bfs"
        bfs = BFS(map_data, start, goal, result_filename=f"{map_name}_{algorithm_name}")
        report._get_algorithm_statistics(bfs, algorithm_name)

        # Greedy
        algorithm_name = "greedy"
        greedy = Greedy(map_data, start, goal, result_filename=f"{map_name}_{algorithm_name}")
        report._get_algorithm_statistics(greedy, algorithm_name)

        # A*
        algorithm_name = "astar"
        a_star = A_star(map_data, start, goal, result_filename=f"{map_name}_{algorithm_name}")
        report._get_algorithm_statistics(a_star, algorithm_name)

    @staticmethod
    def _get_algorithm_statistics(algorithm, algorithm_name: str):
        print(algorithm_name.upper())
        start_time = time.time()
        iterations, path = algorithm.run_algorithm()
        end_time = time.time()

        print(f"Iterations: {iterations}")
        print(f"Path length: {len(path)}")
        elapsed_time = end_time - start_time
        print(f"The algorithm took {elapsed_time} seconds to run.")


if __name__ == '__main__':
    report = Report()

    # 300 x 300 map
    print("MAP 300 x 300")
    map_name = "300x300_map"
    start = (2, 2)
    goal = (295, 256)
    report.get_map_statistics(map_name, start, goal)
    print(" ")

    # 600 x 600 map
    print("MAP 600 x 600")
    map_name = "600x600_map"
    start = (2, 2)
    goal = (598, 595)
    report.get_map_statistics(map_name, start, goal)
    print(" ")

    # 900 x 900 map
    print("MAP 900 x 900")
    map_name = "900x900_map"
    start = (2, 2)
    goal = (898, 895)
    report.get_map_statistics(map_name, start, goal)


