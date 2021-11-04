def main():

    # The list below will be used for all of the exercises below:
    names = ["Abigail", "Brenda", "Chad", "Doug", "Emma", "Francis", "George", "Harold", "Imogen”",
    "Jackie", "Kurt", "Linda"]

    # Example: print the first three names from the list
    # Answer print(names[0:3])

    print(names[3:5])
    # 1. Print ['Doug', 'Emma']

    print(names[1:6])
    # 2. Print [‘Brenda’, ‘Chad’, ‘Doug’, ‘Emma’, ‘Francis’]

    print(names[5:12])
    # 3. [‘Francis’, ‘George’, ‘Harold’, ‘Imogen’, ‘Jackie’, ‘Kurt’, ‘Linda’] (using two numbers in the slice)

    print(names[5:])
    # 4. [‘Francis’, ‘George’, ‘Harold’, ‘Imogen’, ‘Jackie’, ‘Kurt’, ‘Linda’] (using one number in the slice)

    print(names[11::])
    # 5. [‘Linda’] (using a positive number)

    print(names[:10:-1])
    # 6. [‘Linda’] (using a negative number)

    print(names[1:9:2])
    # 7. [‘Brenda’, ‘Doug’, ‘Francis’, ‘Harold’]


    print(names[::2])
    # 8. [‘Abigail’, ‘Chad’, ‘Emma’, ‘George’, ‘Imogen’, ‘Kurt’]


    print(names[0::2])
    # 9. [‘Abigail’, ‘Chad’, ‘Emma’, ‘George’, ‘Imogen’, ‘Kurt’] (using a different way than above.
    # HINT: If you leave a slice number blank, the default is either the beginning or the end of the list,
    # depending on which side of the colon is blank.

    print(names[:8:-1])
    # 10. [‘Linda’, ‘Kurt’, ‘Jackie’]

    print(names[::-1])
    # 11. ['Linda', 'Kurt', 'Jackie', 'Imogen', 'Harold', 'George', 'Francis', 'Emma', 'Doug', 'Chad', 'Brenda', 'Abigail']


    print(names[11::-1])
    # 12. ['Linda', 'Kurt', 'Jackie', 'Imogen', 'Harold', 'George', 'Francis', 'Emma', 'Doug', 'Chad', 'Brenda', 'Abigail']
    # (in a different way than 11. See hint for 9 for help.)





if __name__ == '__main__':
    main()