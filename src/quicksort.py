

def quicksort(array: list):
    pivot: int
    left: list = []
    middle: list = []
    right: list = []

    if len(array) <= 1:
        return array, None

    pivot = array[(len(array) // 2 )]

    for x in array:
        if isinstance(x, (int, float)):
            if x < pivot:
                left.append(x)
            elif x == pivot:
                middle.append(x)
            else:
                right.append(x)
        else:
            return None, Exception("Als Eingabe dürfen nur Zahlen verwendet werden!")

    left, leftErr = quicksort(left)
    right, rightErr = quicksort(right)
    return (left +  middle + right), None