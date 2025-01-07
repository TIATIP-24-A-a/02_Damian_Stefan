import numpy as np


def quicksort(array: list) -> list:
    pivot: int

    if len(array) <= 1:
        return array

    pivot = array[(len(array) // 2 )]

    return (quicksort([x for x in array if x <  pivot]) +
            [x for x in array if x == pivot] +
            quicksort([x for x in array if x >  pivot]))