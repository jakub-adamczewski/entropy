import matplotlib.pyplot as plt
import math
import util


def save_plot(x: list, y: list, title: str, plot_name: str):
    plt.plot(x, y)
    plt.title(title)
    plt.xlabel('entropies')
    plt.ylabel('levels')
    plt.subplot()
    plt.savefig(plot_name)


def save_big_plot(levels: list, files: list, entropies: list, category_title: str, task_nr: int):
    plt.rcParams["figure.autolayout"] = True
    plt.subplots()

    n_cols = 3
    n_rows = math.ceil(len(files) / n_cols)

    x_min = min(levels)
    x_max = max(levels)
    flat_entropies = util.flatten(entropies)
    y_min = min(flat_entropies) - 0.5
    y_max = max(flat_entropies) + 0.5

    for i, file in enumerate(files):
        plt.subplot(n_rows, n_cols, i + 1)
        plt.plot(levels, entropies[i])
        plt.title(f'{file}')

        plt.xscale('linear')
        plt.xlabel('level')

        plt.yscale('linear')
        plt.ylabel('entropy')

        ax = plt.gca()
        ax.set_xlim([x_min, x_max])
        ax.set_ylim([y_min, y_max])

        plt.grid(True)

    plt.savefig(f'plots/task_{task_nr}/{category_title}.pdf')
