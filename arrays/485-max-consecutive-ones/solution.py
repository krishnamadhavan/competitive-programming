def max_consecutive_ones(nums: list) -> int:
    max_ones = 0
    counter = 0
    for num in nums:
        if num == 1:
            counter += 1
            max_ones = max(max_ones, counter)
        else:
            counter = 0
    return max_ones


if __name__ == '__main__':
    assert max_consecutive_ones([1, 0, 1, 1, 0, 1]) == 2
    assert max_consecutive_ones([1, 0, 1, 1, 1, 0]) == 3
