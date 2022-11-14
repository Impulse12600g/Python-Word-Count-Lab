import re
from typing import TextIO
import ssl

import nltk


def initialize():
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context

    nltk.downloader.download('stopwords')
    nltk.downloader.download('punkt')


def count_line_words(line, word_count: dict):
    all_stopwords = nltk.corpus.stopwords.words("english")
    all_stopwords += "br"
    line.lower()  # too lower case
    tokenized = nltk.tokenize.word_tokenize(line)  # tokenize the line being called
    words_wo_stopwords = [word for word in tokenized if word not in all_stopwords if
                          (re.fullmatch("[A-Z]*[a-z]*", word))]  # for loop to pull in words

    for word in words_wo_stopwords:
        word_count[word] = word_count.get(word, 0) + 1


def display_word_dictionary(word_count: dict, top=15):
    print(f"{'Word':^20} - {'Qty':>15}")
    for word, amount in sorted(list(word_count.items()), key=lambda x: x[1], reverse=True)[:top]:
        print(f"{word:^20} - {amount:>15}")
        # if counter == top:
        #     break
        # counter += 1

    # for word, count in (word_count[0:top]):
    #     print(f"{word:^20} - {count:>15}")


def process_file(filename: str):
    word_count = {}
    file: TextIO
    with open(filename, mode="r") as file:
        while line := file.readline():
            count_line_words(line, word_count)
    return word_count
