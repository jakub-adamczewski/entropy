import math
import numpy as np


# H(X)
def get_entropy(probabilities):
    return -sum(map(lambda p: p * math.log(p, 2), probabilities))


# H(X,Y)
def get_joint_entropy(char_probabilities_dict, x_preceding_chars_probabilities_dict, file, x):
    multiplied_probabilities = []
    with open(file=file, mode="r") as f:
        for line in f.readlines():
            for index, c in enumerate(line):
                if index < x:
                    continue
                preceding_chars = line[index - x: index]
                p_x_y = char_probabilities_dict[c] * x_preceding_chars_probabilities_dict[preceding_chars]
                multiplied_probabilities.append(p_x_y)
    return -sum(map(lambda p: p * math.log(p, 2), multiplied_probabilities))


# H(X/Y)
def get_conditional_entropy(char_probabilities_dict, x_preceding_chars_probabilities_dict: dict, file, x):
    joint_x_y_entropy = get_joint_entropy(
        char_probabilities_dict=char_probabilities_dict,
        x_preceding_chars_probabilities_dict=x_preceding_chars_probabilities_dict,
        file=file,
        x=x
    )
    y_entropy = get_entropy(
        probabilities=list(x_preceding_chars_probabilities_dict.values())
    )
    return joint_x_y_entropy - y_entropy


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


def get_x_chars_probabilities(file, x):
    with open(file=file, mode="r") as f:
        all_x_chars_count = 0
        x_chars_probabilities = {}
        for line in f.readlines():
            for index, c in enumerate(line):
                if index < x - 1:
                    continue
                x_chars = line[index - x + 1: index + 1]
                all_x_chars_count += 1
                if x_chars in x_chars_probabilities:
                    x_chars_probabilities[x_chars] += 1
                else:
                    x_chars_probabilities[x_chars] = 1
    return {k: v / all_x_chars_count for k, v in x_chars_probabilities.items()}


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
