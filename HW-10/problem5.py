#  Chapter 10


import urllib.request
import matplotlib.pyplot as plt



def create_counter():

    counts = {}

    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        counts[letter] = 0

    return counts



def download_text(url):

    response = urllib.request.urlopen(url)

    data = response.read()

    text = data.decode("utf-8")


    return text



def count_letters(text):

    counts = create_counter()


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



def save_results(counts, filename):

    file = open(filename, "w")


    for letter in counts:

        file.write(letter + " " + str(counts[letter]) + "\n")


    file.close()



def display_graph(percentages):

    letters = list(percentages.keys())

    values = list(percentages.values())


    plt.figure(figsize=(10,5))


    plt.bar(letters, values)


    plt.xlabel("Letters")

    plt.ylabel("Percent")

    plt.title("Internet Text Frequency Analysis")


    plt.show()



def main():

    print("Choose a Gutenberg text file.")

    print("Example:")
    print("https://gutenberg.org/cache/epub/100/pg100.txt")


    url = input("Enter URL: ")


    output_file = input("Enter output file name: ")


    print()

    print("Downloading file...")


    text = download_text(url)


    print("Analyzing text...")


    counts = count_letters(text)


    percentages = create_percentages(counts)


    save_results(counts, output_file)


    print()

    print("Letter counts saved to", output_file)


    display_graph(percentages)



main()