import entropies
import plots
from final_calculations import calculate_all_entropies_for_files

# sprawdzone odp
files = [
    "data/sample0.txt",  # nie zawiera
    "data/sample1.txt",  # zawiera
    "data/sample2.txt",  # nie zawiera
    "data/sample3.txt",  # zawiera
    "data/sample4.txt",  # nie zawiera
    "data/sample5.txt",  # nie zawiera
]

levels = [1, 2, 3, 4]


def create_plots_with_already_calculated_conditional_entropies():
    char_entropies = [[2.9158942162629677, 2.0003594568493464, 1.5392820427984704, 1.4385819746138613],
                      [3.2391501954800406, 2.8612798881409267, 2.326684943904885, 1.8135102123783182],
                      [3.050439544594746, 2.4676604975534184, 1.9397725879224512, 1.7020328355856251],
                      [3.1844672773090807, 2.6278959197207907, 2.023991698764425, 1.5342435534779935],
                      [4.229101526820833, 4.226829033749153, 4.178535244136844, 3.7661316118107164],
                      [3.523098231686726, 3.2506209602496376, 2.8342715912186827, 2.172440895611472]]
    word_entropies = [[7.486392862851711, 4.406704594406155, 0.5950087061871917, 0.01206212769881263],
                      [5.372245318605186, 1.5747393031025305, 0.5075112949819727, 0.29345806693802967],
                      [7.34862444868417, 3.781937332780256, 0.8595059631118873, 0.08199123582449071],
                      [5.950221966394711, 2.6308074182196752, 1.264091423924473, 0.41432739497180254],
                      [3.4442538962882017, 0.23407601703789896, 0.0032274276117648156, 7.608894145064654e-06],
                      [9.356255905249239e-07, 9.356262173114716e-07, 9.356268440988591e-07, 9.356274708870863e-07]]

    plots.save_big_plot(levels=levels, files=files, entropies=char_entropies, category_title='char_entropies',
                        task_nr=5)
    plots.save_big_plot(levels=levels, files=files, entropies=word_entropies, category_title='word_entropies',
                        task_nr=5)


if __name__ == "__main__":
    calculate_all_entropies_for_files(files=files, levels=levels)
    # create_plots_with_already_calculated_conditional_entropies()
