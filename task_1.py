import random
import time
import numpy as np

from matplotlib import pyplot as plt
from algo.deterministic_quick_sort import deterministic_quick_sort
from algo.randomized_quick_sort import randomized_quick_sort


def measure_time(func, *args):
    start_time = time.time()
    func(*args)
    return time.time() - start_time


def visualization(randomized, deterministic, sizes):
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, randomized, label="Randomized QuickSort", marker="o")
    plt.plot(sizes, deterministic, label="Deterministic QuickSort", marker="s")
    plt.xlabel("Array size")
    plt.ylabel("Runtime (seconds)")
    plt.title("QuickSort runtime comparison")
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == "__main__":
    sizes = [10000, 50000, 100000, 500000]
    randomized_times = []
    deterministic_times = []

    for size in sizes:
        arr = [random.randint(0, 1000) for _ in range(size)]

        randomized_time = np.mean(
            [measure_time(randomized_quick_sort, arr) for _ in range(5)]
        )
        deterministic_time = np.mean(
            [measure_time(deterministic_quick_sort, arr) for _ in range(5)]
        )

        randomized_times.append(randomized_time)
        deterministic_times.append(deterministic_time)

        print(f"Array size: {size}")
        print(f"Randomized QuickSort: {randomized_time:.4f} секунд")
        print(f"Deterministic QuickSort: {deterministic_time:.4f} секунд")

    visualization(randomized_times, deterministic_times, sizes)
