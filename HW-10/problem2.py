#  Chapter 10


import random
import string


def clean_message(message):
    return message.upper().replace(" ", "")


def create_grid(message, rows, cols):

    while len(message) < rows * cols:
        message += random.choice(string.ascii_uppercase)

    grid = []

    index = 0

    for r in range(rows):
        row = []

        for c in range(cols):
            row.append(message[index])
            index += 1

        grid.append(row)

    return grid


def read_path(filename):

    file = open(filename, "r")

    path = eval(file.read())

    file.close()

    return path


def encrypt(grid, path):

    encrypted = ""

    for location in path:

        row = location[0]
        col = location[1]

        encrypted += grid[row][col]

    return encrypted


def decrypt(cipher, path, rows, cols):

    grid = []

    for r in range(rows):
        grid.append([""] * cols)


    index = 0

    reverse_path = path[::-1]


    for location in reverse_path:

        row = location[0]
        col = location[1]

        grid[row][col] = cipher[index]

        index += 1


    message = ""

    for row in grid:

        for letter in row:
            message += letter


    return message


def print_grid(grid):

    print()

    for row in grid:
        print(" ".join(row))

    print()


def main():

    message = input("Enter message: ")

    path_file = input("Enter path file name: ")

    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))


    message = clean_message(message)


    path = read_path(path_file)


    grid = create_grid(message, rows, cols)


    print("\nMessage Grid")
    print_grid(grid)


    encrypted = encrypt(grid, path)

    print("Encrypted Message:")
    print(encrypted)


    decrypted = decrypt(encrypted, path, rows, cols)

    print("\nDecrypted Message:")
    print(decrypted)



main()