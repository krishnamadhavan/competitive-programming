from typing import List


def construct_2d_array(original: List[int], m: int, n: int) -> List[List[int]]:
    if m * n != len(original):
        return []

    result_array = [[0] * n for _ in range(m)]

    index = 0

    for i in range(m):
        for j in range(n):
            result_array[i][j] = original[index]
            index += 1

    return result_array


if __name__ == '__main__':
    assert construct_2d_array([1,2,3,4], 2, 2) == [[1, 2], [3, 4]]
    assert construct_2d_array([1,2,3], 1, 3) == [[1, 2, 3]]
    assert construct_2d_array([1, 2], 1, 1) == []
