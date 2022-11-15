# text = "Hello"
# x = 2
# for index, c in enumerate(text):
#     if index < x:
#         continue
#     preceding_chars = text[index - x: index]
#     key = preceding_chars + "/" + c
#     print(key)
from util import get_letter_probabilities_after_x_chars
from util import get_entropy


def get_entropy_for_num(num):
    probs = get_letter_probabilities_after_x_chars(file="data/norm_wiki_en.txt", x=num)
    return get_entropy(list(probs.values()))


print(list(map(get_entropy_for_num, [0, 1, 2, 3, 4])))
