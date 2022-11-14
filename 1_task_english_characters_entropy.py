from util import get_entropy
from util import get_letters_probabilities

probabilities = get_letters_probabilities(file="data/norm_wiki_en.txt")
print(probabilities)
print(get_entropy(probabilities.values()))
