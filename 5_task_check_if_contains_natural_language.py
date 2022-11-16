import entropies
import probabilities
import plots

files = [
    "data/sample0.txt",
    "data/sample1.txt",
    "data/sample2.txt",
    "data/sample3.txt",
    "data/sample4.txt",
    "data/sample5.txt"
]

for file in files:
    print(file)
    print(f"Entropia znaków: {entropies.get_entropy(list(probabilities.get_chars_probabilities(file).values()))}")
    print(f"Entropia słów: {entropies.get_entropy(list(probabilities.get_words_probabilities(file).values()))}")
    char_conditional_entropies = entropies.get_char_conditional_entropies(file)
    print(f"Entropie warunkowe znaków kolejnych rzędów: {char_conditional_entropies}")
    plots.save_plot("char", file, char_conditional_entropies, 700_000, 0)
    print(f"Entropie warunkowe słów kolejnych rzędów: {entropies.get_word_conditional_entropies(file)}")
