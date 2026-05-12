from tqdm import trange
import time 

# recursive solution
def chance_of_life_recursive(x, y, n, island_size: int):
    if x < 0 or x >= island_size or y < 0 or y >= island_size: return 0
    elif n == 0: return 1
    return 0.25 * (chance_of_life_recursive(x - 1, y, n - 1, island_size) + chance_of_life_recursive(x + 1, y, n - 1, island_size) + chance_of_life_recursive(x, y - 1, n - 1, island_size) + chance_of_life_recursive(x, y + 1, n - 1, island_size))

# test correctness
def test_chance_recursive():
    assert chance_of_life_recursive(0, 0, 1, 2) == 0.5
    assert chance_of_life_recursive(1, 1, 1, 3) == 1
    assert chance_of_life_recursive(0, 0, 3, 3) == 0.25

# determine time usage of the recursive solution with increasing depth but fixed island size
def experiment_recursive_fixed_island_size(size: int=2, max_depth: int=10):
    assert size >= 2
    times = []
    for depth in trange(1, max_depth + 1):
        # get the average time required 
        temp = 0
        for x in range(size):
            for y in range(size):
                start = time.perf_counter()
                chance_of_life_recursive(x, y, depth, size)
                temp += time.perf_counter() - start 
        times.append(temp / (size ** 2))
    return times

# determine time usage of the recursive solution with 'fixed depth' being a fixed amount of steps
def experiment_recursive_fixed_depth(steps, max_island_size=100):
    times = []
    for size in trange(2, max_island_size + 1):
        temp = 0
        for x in range(size):
            for y in range(size):
                start = time.perf_counter()
                chance_of_life_recursive(x, y, steps, size)
                end = time.perf_counter()
                temp += end - start 
        times.append(temp / (size ** 2))    
    return times