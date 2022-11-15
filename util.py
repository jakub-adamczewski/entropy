import math
import numpy as np


def get_entropy(probabilities):
    return -sum(map(lambda p: p * math.log(p, 2), probabilities))


def joint_entropy(X, Y):
    probs = []
    for c1 in set(X):
        for c2 in set(Y):
            probs.append(np.mean(np.logical_and(X == c1, Y == c2)))

    return np.sum(-p * np.log2(p) for p in probs)


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


def get_letter_probabilities_after_x_chars(file, x):
    with open(file=file, mode="r") as f:
        all_chars_count = 0
        characters_counts_with_x_preceding_chars = {}
        for line in f.readlines():
            for index, c in enumerate(line):
                if index < x:
                    continue
                preceding_chars = line[index - x: index]
                key = preceding_chars + "/" + c
                all_chars_count += 1
                if key in characters_counts_with_x_preceding_chars:
                    characters_counts_with_x_preceding_chars[key] += 1
                else:
                    characters_counts_with_x_preceding_chars[key] = 1
    return {k: v / all_chars_count for k, v in characters_counts_with_x_preceding_chars.items()}


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
