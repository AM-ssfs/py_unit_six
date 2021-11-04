def get_numbers():
    '''
    takes a number as a parameter and returns a list starting at 2 up to and including the number.
    :return: 
    '''
    condition = False
    while not condition:
        length = int(input("how high do you want to check for primes? "))
        if length >= 2:
            condition = True
        else:
            print("please enter a whole number greater than 1")
    numbers = []
    for x in range(2, length+1):
        numbers.append(x)
    return numbers


# everything until here  works


def get_primes(numbers):
    primes = []
    while True:
        checking = numbers[0]
        primes.append(checking)
        x = 0
        while x < len(numbers):
            if numbers[x] % checking == 0:
                numbers.remove(numbers[x])
            else:
                x += 1
        print(numbers)
        if len(numbers) == 0:
            return primes


def main():
    numbers = get_numbers()
    primes = get_primes(numbers)
    print(primes)


if __name__ == '__main__':
    main()