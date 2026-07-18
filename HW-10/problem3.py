#  Chapter 10

import matplotlib.pyplot as plt


def count_letters(filename):

    counts = {}

    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        counts[letter] = 0


    file = open(filename, "r", encoding="utf-8")

    text = file.read()

    file.close()


    text = text.upper()


    for character in text:

        if character in counts:
            counts[character] += 1


    return counts


def create_percentages(counts):

    total = 0

    for letter in counts:
        total += counts[letter]


    percentages = {}


    for letter in counts:

        if total > 0:
            percentages[letter] = (counts[letter] / total) * 100

        else:
            percentages[letter] = 0


    return percentages



def display_graph(percentages):

    letters = list(percentages.keys())

    values = list(percentages.values())


    plt.figure(figsize=(10,5))

    plt.bar(letters, values)


    plt.xlabel("Letters")
    plt.ylabel("Percent")
    plt.title("Letter Frequency Analysis")


    plt.show()



def main():

    filename = input("Enter text file name: ")


    counts = count_letters(filename)


    percentages = create_percentages(counts)


    print()

    for letter in percentages:

        print(letter, ":", round(percentages[letter], 2), "%")


    display_graph(percentages)



main()