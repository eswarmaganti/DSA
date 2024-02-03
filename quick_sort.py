from typing import List

def quick_sort(array:List[int]):
    if len(array) <= 1:
        return array

    # assign pivot
    pivot = array[0]

    left = [x for x in array[1:] if x < pivot]
    right = [x for x in array[1:] if x > pivot]

    return quick_sort(left)+[pivot]+quick_sort(right)


if __name__ == "__main__":
    data = [1,5,2,10,11,6,19]
    print(quick_sort(data))