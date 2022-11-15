def get_chars_probabilities(file):
    with open(file=file, mode="r") as f:
        all_chars_count = 0
        characters_counts = {}
        for line in f.readlines():
            for c in line:
                all_chars_count += 1
                if c in characters_counts:
                    characters_counts[c] += 1
                else:
                    characters_counts[c] = 1
    return {k: v / all_chars_count for k, v in characters_counts.items()}


def get_x_chars_probabilities(file, x):
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
    return {k: v / all_x_chars_count for k, v in x_chars_counts.items()}


def get_words_probabilities(file):
    with open(file=file, mode="r") as f:
        all_words_count = 0
        words_counts = {}
        for line in f.readlines():
            words_list = line.split()
            for word in words_list:
                all_words_count += 1
                if word in words_counts:
                    words_counts[word] += 1
                else:
                    words_counts[word] = 1
    return {k: v / all_words_count for k, v in words_counts.items()}


def get_x_words_probabilities(file, x):
    with open(file=file, mode="r") as f:
        all_words_groups_count = 0
        x_words_groups_counts = {}
        for line in f.readlines():
            words_list = line.split()
            for index, word in enumerate(words_list):
                if index < x - 1:
                    continue
                preceding_words = str(words_list[index - x + 1: index + 1])
                all_words_groups_count += 1
                if preceding_words in x_words_groups_counts:
                    x_words_groups_counts[preceding_words] += 1
                else:
                    x_words_groups_counts[preceding_words] = 1
    return {k: v / all_words_groups_count for k, v in x_words_groups_counts.items()}

# def get_letter_probabilities_after_x_chars(file, x):
#     with open(file=file, mode="r") as f:
#         all_chars_count = 0
#         characters_counts_with_x_preceding_chars = {}
#         for line in f.readlines():
#             for index, c in enumerate(line):
#                 if index < x:
#                     continue
#                 preceding_chars = line[index - x: index]
#                 key = preceding_chars + "/" + c
#                 all_chars_count += 1
#                 if key in characters_counts_with_x_preceding_chars:
#                     characters_counts_with_x_preceding_chars[key] += 1
#                 else:
#                     characters_counts_with_x_preceding_chars[key] = 1
#     return {k: v / all_chars_count for k, v in characters_counts_with_x_preceding_chars.items()}
