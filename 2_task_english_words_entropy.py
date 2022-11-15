from util import get_entropy
from util import get_words_probabilities

probabilities = get_words_probabilities(file="data/norm_wiki_en.txt")
for item in list(probabilities.items())[0:10]:
    print(item)
print(get_entropy(probabilities.values()))
