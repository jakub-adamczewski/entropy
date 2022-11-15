from entropies import get_entropy
from probabilities import get_words_probabilities
from scipy.stats import entropy

probabilities = get_words_probabilities(file="data/norm_wiki_en.txt")
for item in list(probabilities.items())[0:10]:
    print(item)

prob_list = list(probabilities.values())
print("My entropy:", get_entropy(prob_list))
print("Lib entropy", entropy(prob_list, base=2))
