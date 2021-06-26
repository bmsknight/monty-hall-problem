import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from src.contestant import Contestant
from src.host import Host

N_GAMES = 1000000
N_DOORS = 3

sns.set_style('darkgrid')
colors = sns.color_palette('deep')


def single_round(host, contestant):
    total_doors = host.present_doors()
    first_choice = contestant.select_door(total_doors)
    remaining_door = host.eliminate_others_and_present_one_door(first_choice)
    final_choice = contestant.wanna_switch(remaining_door)
    won = host.reveal_if_winner(final_choice)
    return won


def plot_two_lists(list1, list2):
    l = np.ones(N_GAMES + 1)
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(list1, color=colors[2], linewidth=2)
    ax.plot(list2, color=colors[3], linewidth=2)
    ax.plot(l * 0.666667, color=colors[2], linestyle='dotted', linewidth=5, alpha=0.5)
    ax.plot(l * 0.333333, color=colors[3], linestyle='dotted', linewidth=5, alpha=0.5)
    plt.legend(['Empirical win probability if you switch',
                'Empirical win probability if you do not switch',
                'Theoretical win probability if you switch',
                'Theoretical win probability if you do not switch'
                ], fontsize=14)
    ax.set_xscale('log')
    plt.ylim([0, 1])
    plt.xlim([1, N_GAMES])
    fig.set_size_inches(12, 9)
    plt.tight_layout(pad=4.0)
    plt.savefig("convergence_plot.png", dpi=400)


if __name__ == '__main__':

    host = Host(door_count=N_DOORS)
    contestant_1 = Contestant(switch=True)
    contestant_2 = Contestant(switch=False)

    c1_times_won = 0
    c2_times_won = 0
    c1_percentage = np.zeros(N_GAMES + 1)
    c2_percentage = np.zeros(N_GAMES + 1)

    for k in range(1, N_GAMES + 1):
        c1_won = single_round(host, contestant_1)
        c2_won = single_round(host, contestant_2)

        if c1_won:
            c1_times_won += 1
        if c2_won:
            c2_times_won += 1

        c1_percentage[k] = c1_times_won / k
        c2_percentage[k] = c2_times_won / k

    # print(c1_percentage)
    # print(c2_percentage)
    plot_two_lists(c1_percentage, c2_percentage)
