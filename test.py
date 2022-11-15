def get_x_words_probabilities(text, x):
    all_words_groups_count = 0
    x_words_groups_counts = {}
    words_list = text.split()
    for index, word in enumerate(words_list):
        if index < x - 1:
            continue
        preceding_words = str(words_list[index - x + 1: index + 1])
        all_words_groups_count += 1
        if preceding_words in x_words_groups_counts:
            x_words_groups_counts[preceding_words] += 1
        else:
            x_words_groups_counts[preceding_words] = 1
    return {k: v / all_words_groups_count for k, v in x_words_groups_counts.items()}

