# from plots import show_plot
# from util import flatten
#
# results = [
#     ("char", "data/norm_wiki_eo.txt", [641422.3088719152, 117860.47964614401, 33673.80536387017, 11781.066317232164]),
#     ("word", "data/norm_wiki_eo.txt",
#      [3727.1000968508265, 12.890832743289227, -15.854103163783066, -18.840747405709628]),
#     ("char", "data/norm_wiki_en.txt", [340810.9099565836, 55821.40257272295, 15563.053788267263, 6411.192609171893]),
#     (
#         "word", "data/norm_wiki_en.txt",
#         [963.7762306023135, -8.997070443430905, -19.070099721158154, -20.244968079879893]),
#     ("char", "data/norm_wiki_et.txt", [321114.67206740694, 48494.839129780456, 9219.362660901785, 2340.4956139799756]),
#     ("word", "data/norm_wiki_et.txt",
#      [15.257536801177274, -18.826705774957762, -19.990145928869687, -20.123396720483342]),
#     ("char", "data/norm_wiki_la.txt", [502375.66732713266, 79655.83271767586, 19409.37471218313, 7647.990544884897]),
#     ("word", "data/norm_wiki_la.txt", [576.263510672316, 241.4315475142962, 161.53266620265916, 146.37506052255566]),
#     ("char", "data/norm_wiki_ht.txt", [209762.96124365026, 45037.82328956487, 18771.726685907655, 11451.552353138668]),
#     ("word", "data/norm_wiki_ht.txt", [4197.2227041822025, 1326.4260399894426, 857.517330928328, 394.08907294314264]),
#     ("char", "data/norm_wiki_nv.txt", [51616.20661197426, 11530.788771315945, 3621.142028772283, 1501.7371798178046]),
#     ("word", "data/norm_wiki_nv.txt", [203.9643221341459, 17.61392072912414, 0.8957036942866807, -6.306796805178127]),
#     ("char", "data/norm_wiki_so.txt", [255901.0507934555, 46898.69385006569, 11273.369237903384, 3605.812404298173]),
#     (
#         "word", "data/norm_wiki_so.txt",
#         [150.69555856112697, -9.603039910587844, -17.897640882634654, -18.86020350544193]),
#     ("char", "data/sample0.txt", [222878.00221387632, 48435.6157113467, 18514.200983079885, 10680.872751841402]),
#     ("word", "data/sample0.txt", [1486.3729839358743, 7.430652888063504, -19.093235899724153, -19.97112561217408]),
#     ("char", "data/sample1.txt", [267461.832809685, 55474.50636520082, 13833.236723126904, 5130.038374991425]),
#     ("word", "data/sample1.txt", [304.57701460305213, 33.522555365697315, -2.4852612710530373, -15.797557783027601]),
#     ("char", "data/sample2.txt", [247027.18422705878, 52424.72513062627, 16461.046472077946, 5800.049004791921]),
#     ("word", "data/sample2.txt", [3898.5676257543014, 99.9772768745937, -15.690442243755932, -19.460016338974434]),
#     ("char", "data/sample3.txt", [343137.9687287138, 75365.39284999273, 24732.675744876953, 10510.043274382297]),
#     ("word", "data/sample3.txt", [1638.2670558931895, 155.25635060306954, 14.139629264289134, 1.007796971779932]),
#     ("char", "data/sample4.txt", [482591.27340074367, 48908.49408140505, 4409.368509824216, 359.5293904278849]),
#     ("word", "data/sample4.txt", [28.35829288033558, -20.445018694268782, -20.770611507058703, -20.773989181119774]),
#     ("char", "data/sample5.txt", [391419.7920239989, 65126.20574695023, 12531.1826719727, 3028.4125461419003]),
#     ("word", "data/sample5.txt", [-16.503864936718564, -16.503864909434466, -16.50386488214569, -16.50386485486013])
# ]
#
# char_results = list(filter(lambda result: result[0] == "char", results))
# all_char_values = flatten(list(map(lambda char_res: char_res[2], char_results)))
# plots_char_max = max(all_char_values)
# plots_char_min = min(min(all_char_values), 0)
# print(plots_char_max)
# print(plots_char_min)
#
# word_results = list(filter(lambda result: result[0] == "word", results))
# all_word_values = flatten(list(map(lambda word_res: word_res[2], word_results)))
# plots_word_max = max(all_word_values)
# plots_word_min = min(min(all_word_values), 0)
# print(plots_word_max)
# print(plots_word_min)
#
# print(len(char_results))
# print(len(word_results))
# print(len(results))
#
# for result in char_results:
#     show_plot(type="char", file=result[1], data=result[2], y_max=plots_char_max, y_min=plots_char_min)
#
# for result in word_results:
#     show_plot(type="word", file=result[1], data=result[2], y_max=plots_word_max, y_min=plots_word_min)

import multiprocessing
import probabilities


def worker(procnum, return_dict):
    """worker function"""
    print(str(procnum) + " represent!")
    return_dict[procnum] = procnum


if __name__ == "__main__":
    print("a")
