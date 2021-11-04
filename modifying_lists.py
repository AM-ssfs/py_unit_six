
def create_list(starting, ending):
    """
    Ex. create_list(4, 10) would return [4, 5, 6, 7, 8, 9, 10]
    :param starting: an integer number
    :param ending: A number greater than the starting number
    :return: list of numbers starting with the first number and going up to and including the second number
    """
    new_list = []
    for x in range(starting, ending+1):
        new_list.append(x)
    return new_list



def find_odds(numbers):
    """
    Ex. find_odds([13, 2, 9, 14, 16, 18, 9, 11, 21]) would return [13, 9, 9, 11, 21]
    :param numbers: a list of numbers
    :return: a new list consisting of only the odd numbers from the original list
    """
    odd_list = []
    for x in range(0, len(numbers)-1):
        if numbers[x] % 2 != 0:
            odd_list.append(numbers[x])
    return odd_list


def remove_duplicates(numbers):
    """
    Ex. remove_duplicates([1, 2, 3, 3, 4, 5, 6, 6, 7, 7, 7])  would return  [1, 2, 3, 4, 5, 6, 7]
    remove_duplicates9[‘apple’, ‘banana’, ‘banana’, ‘cherry’]) would return [‘apple’, ‘banana’, ‘cherry’]
    :param numbers:
    :return:
    """

    no_dupe = []
    for x in range(0, len(numbers)):
        if not numbers[x] in no_dupe:
            no_dupe.append(numbers[x])
    return no_dupe