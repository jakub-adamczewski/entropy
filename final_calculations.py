import plots
from util import flatten
import probabilities
import entropies
import multiprocessing


def final_calculations_for_files(files):
    char_entropies = []
    word_entropies = []

    manager = multiprocessing.Manager()
    return_dict = manager.dict()
    jobs = []

    for i in range(len(files)):
        p = multiprocessing.Process(target=calculate_entropies_for_file, args=(files[i], return_dict))
        jobs.append(p)
        p.start()

    for p in jobs:
        p.join()

    for file in files:
        (chars_entropy, words_entropy, char_conditional_entropies, word_conditional_entropies) = return_dict[file]
        print(file)
        print("Etropia znaków:")
        print(chars_entropy)
        print("Etropia słów:")
        print(words_entropy)
        print("Etropie warunkowe znaków kolejnych rzędów:")
        print(char_conditional_entropies)
        print("Etropie warunkowe słów kolejnych rzędów:")
        print(word_conditional_entropies)
        char_entropies.append(char_conditional_entropies)
        word_entropies.append(word_conditional_entropies)

    char_y_max = max(flatten(char_entropies))
    char_y_min = min(min(flatten(char_entropies)), 0)

    word_y_max = max(flatten(word_entropies))
    word_y_min = min(min(flatten(word_entropies)), 0)

    for i in range(len(files)):
        plots.save_plot(type="char", file=files[i], data=char_entropies[i], y_max=char_y_max, y_min=char_y_min)
        plots.save_plot(type="word", file=files[i], data=word_entropies[i], y_max=word_y_max, y_min=word_y_min)


def calculate_entropies_for_file(file, result):
    print(f"Calculation for {file} started.")

    print(f"{file} 1.")
    chars_entropy = entropies.get_entropy(list(probabilities.get_chars_probabilities(file).values()))

    print(f"{file} 2.")
    words_entropy = entropies.get_entropy(list(probabilities.get_words_probabilities(file).values()))

    print(f"{file} 3.")
    char_conditional_entropies = entropies.get_char_conditional_entropies(file)

    print(f"{file} 4.")
    word_conditional_entropies = entropies.get_word_conditional_entropies(file)

    result[file] = (chars_entropy, words_entropy, char_conditional_entropies, word_conditional_entropies)
    print(f"Calculation for {file} finished.")
