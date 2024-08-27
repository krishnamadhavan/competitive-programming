from typing import List


def has_even_digits(num: int) -> bool:
    digits_count = 0
    while num > 0:
        num //= 10
        digits_count += 1

    return digits_count & 1 == 0


def find_numbers_with_even_digits(nums: List[int]) -> int:
    counter = 0
    for num in nums:
        if has_even_digits(num):
            counter += 1

    return counter


if __name__ == '__main__':
    assert find_numbers_with_even_digits([12, 345, 2, 6, 7896]) == 2
    assert find_numbers_with_even_digits([555, 901, 482, 1771]) == 1
