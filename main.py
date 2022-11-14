import lab4

if __name__ == "__main__":
    lab4.initialize()
    word_count = lab4.process_file("src/data/a1.txt")
    lab4.display_word_dictionary(word_count, 20)


