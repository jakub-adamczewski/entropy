import plots
from util import flatten
import probabilities
import entropies
from threading import Thread

def test:


def final_calculations_for_files(files):
    char_entropies = []
    word_entropies = []

    for file in files:
        print("thread finished...exiting")
        print(file)
        print(f"Entropia znaków: {entropies.get_entropy(list(probabilities.get_chars_probabilities(file).values()))}")
        print(f"Entropia słów: {entropies.get_entropy(list(probabilities.get_words_probabilities(file).values()))}")

        char_conditional_entropies = entropies.get_char_conditional_entropies(file)
        print(f"Entropie warunkowe znaków kolejnych rzędów: {char_conditional_entropies}")
        char_entropies.append(char_conditional_entropies)

        word_conditional_entropies = entropies.get_word_conditional_entropies(file)
        print(f"Entropie warunkowe słów kolejnych rzędów: {word_conditional_entropies}")
        word_entropies.append(word_conditional_entropies)

    char_y_max = max(flatten(char_entropies))
    char_y_min = min(min(flatten(char_entropies)), 0)

    word_y_max = max(flatten(word_entropies))
    word_y_min = min(min(flatten(word_entropies)), 0)

    for i in range(len(files)):
        plots.save_plot(type="char", file=files[i], data=char_entropies[i], y_max=char_y_max, y_min=char_y_min)
        plots.save_plot(type="word", file=files[i], data=word_entropies[i], y_max=word_y_max, y_min=word_y_min)


def calculate_entropies_for_file(file):
