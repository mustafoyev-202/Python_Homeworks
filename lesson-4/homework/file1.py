def uncommon_elements(list1, list2):
    from collections import Counter

    counter1 = Counter(list1)
    counter2 = Counter(list2)

    result = []

    for element in counter1:
        if element not in counter2:
            result.extend([element] * counter1[element])

    for element in counter2:
        if element not in counter1:
            result.extend([element] * counter2[element])

    return result


# Example usage:
list1 = [1, 1, 2]
list2 = [2, 3, 4]
print(uncommon_elements(list1, list2))  # Output: [1, 1, 3, 4]

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(uncommon_elements(list1, list2))  # Output: [1, 2, 3, 4, 5, 6]

list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]
print(uncommon_elements(list1, list2))  # Output: [2, 2, 5]
