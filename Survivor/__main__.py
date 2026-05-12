from recursive_solution import experiment_recursive_fixed_depth, experiment_recursive_fixed_island_size
from plot_results import Plot 

def main():
    fixed_island_size = experiment_recursive_fixed_island_size(size=3, max_depth=10)
    fixed_depth = experiment_recursive_fixed_depth(10, 10)
    plot = Plot()
    plot.plot_island_depth(sizes=range(2, 11), times=fixed_depth)
    plot.plot_island_size(depths=range(1, 11), times=fixed_island_size)
    plot.show()

if __name__ == "__main__": main()