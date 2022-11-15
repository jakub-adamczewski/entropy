from entropies import get_conditional_entropy
from probabilities import get_chars_probabilities, get_x_chars_probabilities

file = "data/norm_wiki_en.txt"
level = 1
first_level_entropy = get_conditional_entropy(
    char_probabilities_dict=get_chars_probabilities(file),
    x_preceding_chars_probabilities_dict=get_x_chars_probabilities(file, level),
    file=file,
    x=level
)
print("First level (one preceding letter) conditional entropy in English:", first_level_entropy)
