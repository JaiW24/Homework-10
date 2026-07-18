# Chapter 10


import os
import matplotlib.pyplot as plt



def create_counter():

    counts = {}

    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        counts[letter] = 0

    return counts



def read_python_files(folder):

    counts = create_counter()


    for filename in os.listdir(folder):

        if filename.endswith(".py"):


            file_path = os.path.join(folder, filename)


            file = open(file_path, "r", encoding="utf-8")

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

    plt.title("Python Program Frequency Analysis")


    plt.show()



def main():

    folder = input("Enter folder name: ")


    counts = read_python_files(folder)


    percentages = create_percentages(counts)


    print()


    for letter in percentages:

        print(letter, ":", round(percentages[letter], 2), "%")


    display_graph(percentages)



main()