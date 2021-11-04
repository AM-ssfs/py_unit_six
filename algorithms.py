
def add_numbers(numbers):
    """
    Ex. add_numbers([9, 5, 11, 6, 1, 15]) returns 47
    :param numbers: a list of numbers
    :return: the sum of all the numbers in the list
    """
    total = 0
    for x in range(0, len(numbers)):
        total += numbers[x]
    return total


def get_max(numbers):
    """
    Ex. get_max([45, 23, 99, 34, 67, 98, 0]) returns 99
    :param numbers: a list of numbers
    :return: The largest number in the list
    """
    high = numbers[0]
    for x in range(len(numbers)):
        if numbers[x] > high:
            high = numbers[x]
    return high


def get_min(numbers):
    """
    Ex. get_min([45, 23, 99, 34, 67, 98, 0]) returns 0
    :param numbers: a list of numbers
    :return: The smallest number in the list
    """
    low = numbers[0]
    for x in range(len(numbers)):
        if numbers[x] < low:
            low = numbers[x]
    return low


def merge(list1, list2):
    """
    Ex. merge([3, 4, 7, 9], [1, 5, 8, 11]) return [1, 3, 4, 5, 7, 8, 9, 11]
    :param list1: a list in sorted order
    :param list2: a second list in sorted order
    :return: a single list consisting of both smaller lists combined in sorted order.
    """
    combined = []
    while True:
        if list1 != [] and list2 != []:
            if list1[0] <= list2[0]:
                combined.append(list1.pop(0))
            else:
                combined.append(list2.pop(0))
        elif list1 == [] and list2 != []:
            for x in range(len(list2)):
                combined.append(list2[x])
            list2 = []
        elif list1 != [] and list2 == []:
            for x in range(len(list1)):
                combined.append(list1[x])
            list1 = []
        if list1 == [] and list2 == []:
            break
    return combined

# if left is bigger than right, swap them, then check next
# keep doing that until no more swap


def evaluate(num1, num2):
    if num1 > num2:
        return [num2, num1, 1]
    else:
        return [num1, num2, 0]


def bubble_sort(list1):
    print(list1)
    while True:
        condition = False
        for x in range(len(list1)-1):
            placeholder = evaluate(list1[x], list1[x+1])
            list1[x] = placeholder[0]
            list1[x+1] = placeholder[1]
            if placeholder[2] == 1:
                condition = True
        if condition:
            bubble_sort(list1)
        else:
            return list1


eeeee = [2, 1, 5, 6, 2, 9, 2, 5, 8, 1, 4, 2, 5]
bubble_sort(eeeee)

