import math
import quantities


# H(X)
def get_entropy(probabilities: list):
    return -sum(map(lambda p: p * math.log(p, 2), probabilities))


# H(X/Y) for letters
def get_conditional_entropy_chars(file, level):
    (all_chunks_quantities, all_chunks_count) = quantities.get_x_chars_quantities(file, level + 1)
    (preceding_chunks_quantities, preceding_chunks_count) = quantities.get_x_chars_quantities(file, level)
    entropy = 0
    for chunk, quantity in all_chunks_quantities.items():
        joint_probability = quantity / all_chunks_count
        conditional_probability = quantity / preceding_chunks_quantities[chunk[0:-1]]
        entropy -= joint_probability * math.log(conditional_probability, 2)
    return entropy


# H(X/Y) for words
def get_conditional_entropy_words(file, level):
    (all_words_quantities, all_words_groups_count) = quantities.get_x_words_quantities(file, level + 1)
    (preceding_words_quantities, preceding_words_count) = quantities.get_x_words_quantities(file, level)
    entropy = 0
    for words, quantity in all_words_quantities.items():
        joint_probability = quantity / all_words_groups_count
        conditional_probability = quantity / preceding_words_quantities[words[0:-1]]
        entropy -= joint_probability * math.log(conditional_probability, 2)
    return entropy
