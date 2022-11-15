from util import get_entropy
from util import get_letters_probabilities
from scipy.stats import entropy

probabilities = get_letters_probabilities(file="data/norm_wiki_en.txt")
print(probabilities)
prob_list = list(probabilities.values())
print("My entropy:", get_entropy(prob_list))
print("Lib entropy", entropy(prob_list, base=2))
