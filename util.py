import math


def get_entropy(probabilities):
    return -sum(map(lambda p: p * math.log(p, 2), probabilities))


def get_letters_probabilities(file):
    with open(file=file, mode="r") as f:
        all_chars_count = 0
        characters_counts = {}
        for line in f.readlines():
            for c in line:
                all_chars_count += 1
                if c in characters_counts:
                    characters_counts[c] += 1
                else:
                    characters_counts[c] = 1
    return {k: v / all_chars_count for k, v in characters_counts.items()}
