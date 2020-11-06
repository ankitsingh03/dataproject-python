import csv
from collections import defaultdict
import matplotlib.pyplot as plt
from operator import add


def data_collection():
    """
    collect all the data according to this form \
    {season: {team: number of matches played in one season}} \
    and list of teams
    """
    season = defaultdict(list)
    teams = set()
    with open('matches.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        csv_reader.__next__()
        # creating dict {season: list of teams name}
        for line in csv_reader:
            season[line[1]].extend([line[4], line[5]])
            teams.update({line[4], line[5]})

    # creating dict {season: {team: number of matches played in one season}}
    total = {}
    for p, q in season.items():
        for i in q:
            total[p] = {i: q.count(i) for i in q}

    return total, list(teams)


def plot_graph(data, teams):
    year = sorted(data.keys())

    # create dict according to {team: [number of matches per season]}
    team_data = defaultdict(list)
    for i in teams:
        for j in year:
            team_data[i].append(data[j].get(i, 0))

    plot = []
    plot.append(plt.bar(year, team_data[teams[0]]))
    sum = team_data[teams[0]]
    for i in range(1, len(teams)):
        if i > 1:
            sum = list(map(add, sum, team_data[teams[i-1]]))
        plot.append(plt.bar(year, team_data[teams[i]], bottom=sum))

    plt.ylabel('Scores')
    plt.title('Matches Played By Team By Season')
    plt.xticks(year)
    plt.yticks(range(0, 210, 10))
    plt.legend((i[0] for i in plot), (teams))

    plt.show()


if __name__ == "__main__":
    data, teams = data_collection()
    plot_graph(data, teams)
