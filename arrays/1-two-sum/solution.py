from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    hashmap = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap:
            return [i, hashmap[complement]]
        hashmap[nums[i]] = i


if __name__ == '__main__':
    assert two_sum([2, 7, 11, 15], 9) == [0, 1] or [1, 0]
    assert two_sum([3, 2, 4], 6) == [1, 2] or [2, 1]
    assert two_sum([3, 3], 6) == [0, 1] or [1, 0]
