import os
import string
from collections import Counter


def create_sample_file():
    with open("sample.txt", "w") as file:
        paragraph = input("Enter a paragraph to create 'sample.txt': ")
        file.write(paragraph)


def read_file(file_path):
    if not os.path.exists(file_path):
        create_sample_file()
    with open(file_path, "r") as file:
        return file.read()


def count_word_frequency(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    return Counter(words)


def display_top_words(word_counts, top_n=5):
    total_words = sum(word_counts.values())
    print(f"Total words: {total_words}")
    print(f"Top {top_n} most common words:")
    for word, count in word_counts.most_common(top_n):
        print(f"{word} - {count} times")


def save_report(word_counts, total_words, top_n=5):
    with open("word_count_report.txt", "w") as file:
        file.write("Word Count Report\n")
        file.write(f"Total Words: {total_words}\n")
        file.write(f"Top {top_n} Words:\n")
        for word, count in word_counts.most_common(top_n):
            file.write(f"{word} - {count}\n")


def main():
    file_path = "sample.txt"
    text = read_file(file_path)
    word_counts = count_word_frequency(text)
    total_words = sum(word_counts.values())

    top_n = input("Enter the number of top common words to display (default is 5): ")
    if not top_n.isdigit():
        top_n = 5
    else:
        top_n = int(top_n)

    display_top_words(word_counts, top_n)
    save_report(word_counts, total_words, top_n)


if __name__ == "__main__":
    main()
