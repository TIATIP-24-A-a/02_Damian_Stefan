import pytest
import numpy as np
from quicksort import quicksort

@pytest.mark.parametrize("n", [10, 100, 1000, 10000, 100000, 1000000 ])
def test_quicksort_benchmark(benchmark, n):
    random_array = np.random.randint(0, 100000, n, int).tolist()
    result, error = benchmark(quicksort, random_array)
    assert error is None
    assert np.array_equal(result, np.sort(random_array))