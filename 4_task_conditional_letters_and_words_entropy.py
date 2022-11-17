from final_calculations import final_calculations_for_files

files = [
    "data/norm_wiki_eo.txt",
    "data/norm_wiki_en.txt",
    "data/norm_wiki_et.txt",
    "data/norm_wiki_la.txt",
    "data/norm_wiki_ht.txt",
    "data/norm_wiki_nv.txt",
    "data/norm_wiki_so.txt",
]

if __name__ == "__main__":
    final_calculations_for_files(files)

"""
Wyniki:
data/norm_wiki_eo.txt
Etropia znaków:
4.176788490262166
Etropia słów:
11.560529950317907
Etropie warunkowe znaków kolejnych rzędów:
[4714765.719936727, 641422.3088719152, 117860.47964614401, 33673.80536387017, 11781.066317232164]
Etropie warunkowe słów kolejnych rzędów:
[178539.6331574457, 3727.1000968508265, 12.890832743289227, -15.854103163783066, -18.840747405709628]
data/norm_wiki_en.txt
Etropia znaków:
4.288221453845133
Etropia słów:
11.543993773635416
Etropie warunkowe znaków kolejnych rzędów:
[2619026.900754158, 340810.9099565836, 55821.40257272295, 15563.053788267263, 6411.192609171893]
Etropie warunkowe słów kolejnych rzędów:
[74497.51297935277, 963.7762306023135, -8.997070443430905, -19.070099721158154, -20.244968079879893]
data/norm_wiki_et.txt
Etropia znaków:
4.169833224728489
Etropia słów:
13.746243545091751
Etropie warunkowe znaków kolejnych rzędów:
[2373384.5401527886, 321114.67206740694, 48494.839129780456, 9219.362660901785, 2340.4956139799756]
Etropie warunkowe słów kolejnych rzędów:
[17402.349526513135, 15.257536801177274, -18.826705774957762, -19.990145928869687, -20.123396720483342]
data/norm_wiki_la.txt
Etropia znaków:
4.228247465746813
Etropia słów:
11.969194044355133
Etropie warunkowe znaków kolejnych rzędów:
[3813543.8446966857, 502375.66732713266, 79655.83271767586, 19409.37471218313, 7647.990544884897]
Etropie warunkowe słów kolejnych rzędów:
[53697.67218602549, 576.263510672316, 241.4315475142962, 161.53266620265916, 146.37506052255566]
data/norm_wiki_ht.txt
Etropia znaków:
4.146385764101037
Etropia słów:
8.166919505035342
Etropie warunkowe znaków kolejnych rzędów:
[1314986.7661005238, 209762.96124365026, 45037.82328956487, 18771.726685907655, 11451.552353138668]
Etropie warunkowe słów kolejnych rzędów:
[92506.05413116998, 4197.2227041822025, 1326.4260399894426, 857.517330928328, 394.08907294314264]
data/norm_wiki_nv.txt
Etropia znaków:
3.8749372588209434
Etropia słów:
9.15401183080255
Etropie warunkowe znaków kolejnych rzędów:
[285740.5430215714, 51616.20661197426, 11530.788771315945, 3621.142028772283, 1501.7371798178046]
Etropie warunkowe słów kolejnych rzędów:
[11026.745756276883, 203.9643221341459, 17.61392072912414, 0.8957036942866807, -6.306796805178127]
data/norm_wiki_so.txt
Etropia znaków:
4.040113860382521
Etropia słów:
11.731104737245332
Etropie warunkowe znaków kolejnych rzędów:
[1502521.4404663334, 255901.0507934555, 46898.69385006569, 11273.369237903384, 3605.812404298173]
Etropie warunkowe słów kolejnych rzędów:
[22478.237663442065, 150.69555856112697, -9.603039910587844, -17.897640882634654, -18.86020350544193]
"""
