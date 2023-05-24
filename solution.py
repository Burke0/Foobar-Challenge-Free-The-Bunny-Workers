from itertools import combinations


def solution(num_buns, num_required):
    # If no keys are required, return list of empty key lists
    if num_required == 0:
        return [[] for _ in range(num_buns)]
    # If the number of bunnies equals the number of required keys,
    # then each bunny gets a unique key
    if num_buns == num_required:
        return [[i] for i in range(num_required)]

    # Create an empty list of keys for each bunny
    bunnies = [[] for _ in range(num_buns)]

    # Calculate how many copies of each key will be made. Each key should be
    # held by a number of bunnies such that removing any single bunny still
    # leaves every key in the possession of at least one bunny. Hence, each key
    # is copied num_buns - num_required + 1 times.
    copies_of_each_key = num_buns - num_required + 1

    # Generate all combinations of bunnies to assign keys to
    for key, bunnies_with_key in enumerate(
        combinations(range(num_buns), copies_of_each_key)
    ):
        # For each combination, assign the key to the bunnies in that combination
        for bunny in bunnies_with_key:
            bunnies[bunny].append(key)

    # Return the distribution of keys among the bunnies
    return bunnies
