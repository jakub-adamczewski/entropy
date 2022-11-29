import entropies

file = "data/norm_wiki_en.txt"
level = 1
first_level_entropy = entropies.get_conditional_entropy_chars(file=file, level=level)
print("First level (one preceding letter) conditional entropy in English:", first_level_entropy)
