import math


def get_entropy(probabilities):
    return -sum(map(lambda p: p * math.log(p, 2), probabilities))


def get_letters_probabilities(file):
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
