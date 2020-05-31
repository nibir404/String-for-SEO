with open("hemlet.txt", mode="r") as h_file:
    words_all = []
    unique_words = []
    for line in h_file.readlines():
        words = line.strip().split(" ")
        words_all += words

    unique_words = set(words_all)
    print(len(words_all))
    print(len(unique_words))


    with open("unique_words.txt",mode="w") as write_files:
        for item in sorted( unique_words):
            write_files.write(item)
            write_files.write("\n")