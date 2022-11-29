from final_calculations import calculate_all_entropies_for_files
import plots

files = [
    "data/norm_wiki_eo.txt",
    "data/norm_wiki_en.txt",
    "data/norm_wiki_et.txt",
    "data/norm_wiki_la.txt",
    "data/norm_wiki_ht.txt",
    "data/norm_wiki_nv.txt",
    "data/norm_wiki_so.txt",
]
levels = [1, 2, 3, 4]


def create_plits_with_already_calculated_conditional_entropies():
    char_entropies = [[3.340005253797392, 2.8718268762428507, 2.392625077657027, 1.991510128286644],
                      [3.516604933316685, 3.0183193251147657, 2.4815660537461874, 2.021185065043691],
                      [3.5069583101344235, 3.13440626696733, 2.6108658073128597, 2.1114424274106742],
                      [3.4501261536143852, 2.823492106530299, 2.1520314314204265, 1.6427638701364686],
                      [3.1138607714802373, 2.2735251221458084, 1.4921527491425781, 1.0521435299646493],
                      [2.9472686229701526, 2.3675810981660974, 1.7952643889941493, 1.3415979250332555],
                      [3.299566136299429, 2.844371887070636, 2.3743108553306147, 1.945032742557818]]
    word_entropies = [[6.5576792566557955, 2.484719598290749, 0.6336182904549443, 0.16165828758929832],
                      [6.389175861627316, 2.176460456201819, 0.48467886887154094, 0.1096531537240352],
                      [5.424183898904879, 0.9047414819244088, 0.11619701011997018, 0.02364729988548377],
                      [4.400026106166727, 1.1668837096581777, 0.38803540854204, 0.20646889313686384],
                      [3.1931145053383356, 1.3113269628663495, 0.8122283061617945, 0.6205735855268225],
                      [3.8639409744048634, 1.7188136325870265, 0.899260834298287, 0.5385767433847521],
                      [5.398739370479995, 1.6086239389585326, 0.4096065365721172, 0.11661094741552007]]

    plots.save_big_plot(levels=levels, files=files, entropies=char_entropies, category_title='char_entropies',
                        task_nr=4)
    plots.save_big_plot(levels=levels, files=files, entropies=word_entropies, category_title='word_entropies',
                        task_nr=4)


if __name__ == "__main__":
    # calculate_all_entropies_for_files(files=files, levels=levels)
    create_plits_with_already_calculated_conditional_entropies()
