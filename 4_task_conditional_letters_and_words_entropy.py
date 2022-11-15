import entropies
import probabilities
import matplotlib.pyplot as plt
import numpy as np

conditional_entropy_levels = [1, 2, 3, 4]


def show_plot(type, file, data):
    plt.plot(data)
    plt.xlabel("levels")
    plt.ylabel("entropies")
    plt.title(f"{type} entropies for {file}")
    plt.xticks(np.arange(len(data)), np.arange(1, len(data) + 1))
    ax = plt.gca()
    ax.set_xlim([conditional_entropy_levels[0], conditional_entropy_levels[-1]])
    ax.set_ylim([550_000, -50])
    plt.show()


files = [
    "data/norm_wiki_eo.txt",
    "data/norm_wiki_en.txt",
    "data/norm_wiki_et.txt",
    "data/norm_wiki_la.txt",
    "data/norm_wiki_ht.txt",
    "data/norm_wiki_nv.txt",
    "data/norm_wiki_so.txt",
    "data/sample0.txt",
    "data/sample1.txt",
    "data/sample2.txt",
    "data/sample3.txt",
    "data/sample4.txt",
    "data/sample5.txt"
]
for file in files:
    # chars entropies
    char_entropies_results = list(
        (entropies.get_conditional_entropy_chars(
            char_probabilities_dict=probabilities.get_chars_probabilities(file),
            x_preceding_chars_probabilities_dict=probabilities.get_x_chars_probabilities(file, level),
            file=file,
            x=level
        ) for level in conditional_entropy_levels)
    )
    print("char", file, char_entropies_results)
    show_plot("char", file, char_entropies_results)

    # words entropies
    words_entropies_results = list(
        (entropies.get_conditional_entropy_words(
            words_probabilities_dict=probabilities.get_words_probabilities(file),
            x_preceding_words_probabilities_dict=probabilities.get_x_words_probabilities(file, level),
            file=file,
            x=level
        ) for level in conditional_entropy_levels)
    )
    print("word", file, words_entropies_results)
    show_plot("word", file, words_entropies_results)
