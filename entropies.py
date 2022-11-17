import math
import probabilities


# H(X)
def get_entropy(probabilities):
    return -sum(map(lambda p: p * math.log(p, 2), probabilities))


# H(X,Y)
def get_joint_entropy_letters(char_probabilities_dict, x_preceding_chars_probabilities_dict, file, x):
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


# H(X,Y)
def get_joint_entropy_words(words_probabilities_dict, x_preceding_words_probabilities_dict, file, x):
    multiplied_probabilities = []
    with open(file=file, mode="r") as f:
        for line in f.readlines():
            words_list = line.split()
            for index, word in enumerate(words_list):
                if index < x:
                    continue
                preceding_words = str(words_list[index - x: index])
                p_x_y = words_probabilities_dict[word] * x_preceding_words_probabilities_dict[preceding_words]
                multiplied_probabilities.append(p_x_y)
    return -sum(map(lambda p: p * math.log(p, 2), multiplied_probabilities))


# H(X/Y) for letters
def get_conditional_entropy_chars(char_probabilities_dict, x_preceding_chars_probabilities_dict: dict, file, x):
    joint_x_y_entropy = get_joint_entropy_letters(
        char_probabilities_dict=char_probabilities_dict,
        x_preceding_chars_probabilities_dict=x_preceding_chars_probabilities_dict,
        file=file,
        x=x
    )
    y_entropy = get_entropy(
        probabilities=list(x_preceding_chars_probabilities_dict.values())
    )
    return joint_x_y_entropy - y_entropy


# H(X/Y) for words
def get_conditional_entropy_words(words_probabilities_dict, x_preceding_words_probabilities_dict: dict, file, x):
    joint_x_y_entropy = get_joint_entropy_words(
        words_probabilities_dict=words_probabilities_dict,
        x_preceding_words_probabilities_dict=x_preceding_words_probabilities_dict,
        file=file,
        x=x
    )
    y_entropy = get_entropy(
        probabilities=list(x_preceding_words_probabilities_dict.values())
    )
    return joint_x_y_entropy - y_entropy


def get_char_conditional_entropies(file, conditional_entropy_levels=(1, 2, 3, 4)):
    return list(
        (get_conditional_entropy_chars(
            char_probabilities_dict=probabilities.get_chars_probabilities(file),
            x_preceding_chars_probabilities_dict=probabilities.get_x_chars_probabilities(file, level),
            file=file,
            x=level
        ) for level in conditional_entropy_levels)
    )


def get_word_conditional_entropies(file, conditional_entropy_levels=(1, 2, 3, 4)):
    return list(
        (get_conditional_entropy_words(
            words_probabilities_dict=probabilities.get_words_probabilities(file),
            x_preceding_words_probabilities_dict=probabilities.get_x_words_probabilities(file, level),
            file=file,
            x=level
        ) for level in conditional_entropy_levels)
    )
