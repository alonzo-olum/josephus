#!/bin/env python3

def knapsack(
        weights: list, values: list, items: int, max_weight: int, index: int
        ) -> int:
    
    """
    >>> knapsack([3,4,5], [10,9,8], 3, 25, 0)
    27
    """
    if index == items: return 0

    result = knapsack(weights, values, items, max_weight, index+1)
    if weights[index] <= max_weight:
        rec_result = values[index] + knapsack(
                weights, values, items, max_weight - weights[index], index+1
                )
    return max(result, rec_result)

if __name__ == '__main__':
    import doctest

    doctest.testmod()
