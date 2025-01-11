from logging import exception

import numpy as np
from requests.cookies import extract_cookies_to_jar


# todo:
# replace list with np array
# median of three
# insertion sort on sorted parts


def quicksort(array: list) -> tuple[list | None, Exception | None]:
    pivot: int
    left: list = []
    middle: list = []
    right: list = []
    if len(array) <= 1:
        return array, None

    pivot = array[(len(array) // 2 )]
    for x in array:
        if isinstance(x, int | float):
            if x < pivot:
                left.append(x)
            elif x == pivot:
                middle.append(x)
            else:
                right.append(x)
        else:
            return None, Exception("Als Eingabe dürfen nur Zahlen verwendet werden!")

        return (quicksort(left) +  middle + quicksort(right)), None