def count_positive_numbers(nums):
    count = 0
    for num in nums:
        if num >= 0:
            count += 1

    return count

def test_count_positive_numbers():
    assert count_positive_numbers([-2, -1, 0, 1, 2]) == 3
    assert count_positive_numbers([-2, -1]) == 0

def logical_errors():
    test_count_positive_numbers()
#logical_errors()
#print(f"debug: All tests passed : count possitive number was -1, resturn: {count_positive_numbers([-1])}")