import matplotlib.pyplot as plt
import numpy as np


def save_plot(type: str, file: str, data, y_max=None, y_min=None):
    plt.plot(data)
    plt.xlabel("levels")
    plt.ylabel("entropies")
    plt.title(f"{type} entropies for {file}")
    plt.xticks(np.arange(len(data)), np.arange(1, len(data) + 1))
    if y_min is not None and y_max is not None:
        ax = plt.gca()
        ax.set_ylim([y_min, y_max])

    new_filename = file.replace("data", "plots").replace(".txt", "")
    plt.savefig(f"{new_filename}-{type}.pdf")
