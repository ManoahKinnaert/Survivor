def chance_of_life_recursive(x, y, n, island_size: int):
    if x < 0 or x >= island_size or y < 0 or y >= island_size: return 0
    elif n == 0: return 1
    return 0.25 * (chance_of_life_recursive(x - 1, y, n - 1, island_size) + chance_of_life_recursive(x + 1, y, n - 1, island_size) + chance_of_life_recursive(x, y - 1, n - 1, island_size) + chance_of_life_recursive(x, y + 1, n - 1, island_size))

def test_chance_recursive():
    assert chance_of_life_recursive(0, 0, 1, 2) == 0.5
    assert chance_of_life_recursive(1, 1, 1, 3) == 1
    assert chance_of_life_recursive(0, 0, 3, 3) == 0.25

if __name__ == "__main__":
    test_chance_recursive()