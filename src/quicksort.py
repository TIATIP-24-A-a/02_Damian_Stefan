import numpy as np
from fontTools.misc.cython import returns


def quicksort(array: list) -> list:
    if len(array) <= 1:
        return array
    pivot = array[(len(array) // 2 )]

    return array