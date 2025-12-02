

def find_two_smallest(numbers):
    """
    Получает список целых чисел и возвращает два наименьших.
    Ничего не печатает, только возвращает (min1, min2).
    """
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")

    
    nums = numbers.copy()
    nums.sort()
    return nums[0], nums[1]
