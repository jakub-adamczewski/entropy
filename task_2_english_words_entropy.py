from entropies import get_entropy
import quantities
from scipy.stats import entropy


def get_words_entropy(file, log=False):
    (words_quantities, all_words_count) = quantities.get_x_words_quantities(file="data/norm_wiki_en.txt", x=1)
    prob_list = list(map(lambda x: x / all_words_count, words_quantities.values()))
    my_entropy = get_entropy(prob_list)
    if log:
        print(words_quantities)
        print(all_words_count)
        print("My entropy:", my_entropy)
        print("Lib entropy", entropy(prob_list, base=2))
    return my_entropy


if __name__ == '__main__':
    get_words_entropy(file="data/norm_wiki_en.txt", log=True)
