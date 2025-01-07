import numpy as np


def quicksort(array: list) -> list:
    pivot: int
    left: list
    right: list
    middle: list

    if len(array) <= 1:
        return array

    pivot = array[(len(array) // 2 )]

    left   = [x for x in array if x <  pivot]
    middle = [x for x in array if x == pivot]
    right  = [x for x in array if x >  pivot]
    print(left + middle + right)
    return quicksort(left) + quicksort(middle) + quicksort(right)