def get_x_chars_quantities(file, x):
    with open(file=file, mode="r") as f:
        all_x_chars_count = 0
        x_chars_counts = {}
        for line in f.readlines():
            for index, c in enumerate(line):
                if index < x - 1:
                    continue
                x_chars = line[index - x + 1: index + 1]
                all_x_chars_count += 1
                if x_chars in x_chars_counts:
                    x_chars_counts[x_chars] += 1
                else:
                    x_chars_counts[x_chars] = 1
    return x_chars_counts, all_x_chars_count


def get_x_words_quantities(file, x):
    with open(file=file, mode="r") as f:
        all_words_groups_count = 0
        x_words_groups_counts = {}
        for line in f.readlines():
            words_list = line.split()
            for index, word in enumerate(words_list):
                if index < x - 1:
                    continue
                preceding_words = tuple(words_list[index - x + 1: index + 1])
                all_words_groups_count += 1
                if preceding_words in x_words_groups_counts:
                    x_words_groups_counts[preceding_words] += 1
                else:
                    x_words_groups_counts[preceding_words] = 1
    return x_words_groups_counts, all_words_groups_count
