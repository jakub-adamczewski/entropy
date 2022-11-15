from entropies import get_entropy
from probabilities import get_chars_probabilities
from scipy.stats import entropy

probabilities = get_chars_probabilities(file="data/norm_wiki_en.txt")
print(probabilities)
prob_list = list(probabilities.values())
print("My entropy:", get_entropy(prob_list))
print("Lib entropy", entropy(prob_list, base=2))
