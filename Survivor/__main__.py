from recursive_solution import experiment_recursive_fixed_depth, experiment_recursive_fixed_island_size

if __name__ == "__main__":
    times = experiment_recursive_fixed_depth(2)
    times2 = experiment_recursive_fixed_island_size(10, 5)
    print(times2)