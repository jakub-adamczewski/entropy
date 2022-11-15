from util import get_conditional_entropy
from util import get_letters_probabilities
from util import get_x_chars_probabilities


def get_entropy_for_num(num):
    file = "data/norm_wiki_en.txt"
    return get_conditional_entropy(
        char_probabilities_dict=get_letters_probabilities(file),
        x_preceding_chars_probabilities_dict=get_x_chars_probabilities(file, num),
        file=file,
        x=num
    )


print(list(map(get_entropy_for_num, [0, 1, 2, 3, 4])))
