import numpy as np
# todo:
# replace list with np array
# median of three
# insertion sort on sorted parts


def quicksort(array: list) -> list:
    pivot: int

    for x in array:
        if not isinstance(x, int) and not isinstance(x, float):
            raise Exception("Als Eingabe dürfen nur Zahlen verwendet werden!")

    if len(array) <= 1:
        return array

    pivot = array[(len(array) // 2 )]

    return (quicksort([x for x in array if x <  pivot]) +
            [x for x in array if x == pivot] +
            quicksort([x for x in array if x >  pivot]))