#!/bin/env python3

# an illustration of 0-1 Knapsack problem
def knapsack(capacity: int, weights: list[int], values: list[int], counter: int) -> int:

    # trivial scenario with initial index or no cap
    if counter == 0 or capacity == 0: return 0

    # If weight of item is gt capacity, exclude item
    if weights[counter-1] > capacity:
        return knapsack(capacity, weights, values, counter-1)
    else:
        # else return the max of the nth item or not included item
        rem_cap = capacity - weights[counter-1]
        new_val = values[counter-1] + knapsack(
                rem_cap, weights, values, counter-1
                )
        without_new_val = knapsack(capacity, weights, values, counter-1)
        return max(new_val, without_new_val)

if __name__ == '__main__':
    values = [60, 100, 120]
    print(knapsack(50, [10, 20, 30], values, len(values)))
