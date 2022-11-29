import quantities
import entropies
import plots


def test_x_chars_quantities():
    assert quantities.get_x_chars_quantities("data/bananas.txt", 1) == ({'b': 1, 'a': 3, 'n': 2, 's': 1}, 7)
    assert quantities.get_x_chars_quantities("data/bananas.txt", 2) == ({'ba': 1, 'an': 2, 'na': 2, 'as': 1}, 6)
    assert quantities.get_x_chars_quantities("data/bananas.txt", 3) == ({'ban': 1, 'ana': 2, 'nan': 1, 'nas': 1}, 5)


if __name__ == "__main__":
    # test_x_chars_quantities()
    # print(entropies.get_conditional_entropy_chars("data/bananas.txt", 1))
    # print(entropies.get_conditional_entropy_chars("data/bananas.txt", 2))
    #
    # print(quantities.get_x_words_quantities("data/words_banana.txt", 2))
    lst = [0,1,2,3]
    print(lst)
    print(lst[0:-1])
    plots.save_plot([1,2],[1,2],"test","test.txt_char.pdf")

