import multiprocessing

import entropies
import plots
from task_1_english_characters_entropy import get_chars_entropy
from task_2_english_words_entropy import get_words_entropy


def calculate_all_entropies_for_files(files: list, levels: list):
    char_entropies = []
    word_entropies = []

    manager = multiprocessing.Manager()
    return_dict = manager.dict()
    jobs = []

    for i, file in enumerate(files):
        p = multiprocessing.Process(target=calculate_entropies_for_file, args=(file, levels, return_dict))
        jobs.append(p)
        p.start()

    for p in jobs:
        p.join()

    for file in files:
        (char_entropy, words_entropy, char_conditional_entropies, word_conditional_entropies) = return_dict[file]
        print(file)
        print(f"Entropia znaków:")
        print(char_entropy)
        print(f"Entropia słów:")
        print(words_entropy)
        print(f"Etropie warunkowe znaków dla rzędów {levels}:")
        print(char_conditional_entropies)
        print(f"Etropie warunkowe słów dla rzędów {levels}:")
        print(word_conditional_entropies)
        char_entropies.append(char_conditional_entropies)
        word_entropies.append(word_conditional_entropies)

    print("all char:")
    print(char_entropies)
    print("all word:")
    print(word_entropies)


def calculate_entropies_for_file(file, levels, result):
    print(f"Calculation for {file} started.")

    print(f"{file} 1.")
    char_entropy = get_chars_entropy(file)

    print(f"{file} 2.")
    words_entropy = get_words_entropy(file)

    print(f"{file} 3.")
    char_conditional_entropies: list = [entropies.get_conditional_entropy_chars(file=file, level=level)
                                        for level in levels]

    print(f"{file} 4.")
    word_conditional_entropies: list = [entropies.get_conditional_entropy_words(file=file, level=level)
                                        for level in levels]

    result[file] = (char_entropy, words_entropy, char_conditional_entropies, word_conditional_entropies)
    print(f"Calculation for {file} finished.")
