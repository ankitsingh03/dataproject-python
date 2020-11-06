import csv
from collections import defaultdict
import matplotlib.pyplot as plt
from operator import add


def data_collection():
    season = defaultdict(list)
    teams = set()
    with open('matches.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        csv_reader.__next__()
        for line in csv_reader:
            season[line[1]].extend([line[4], line[5]])
            teams.update({line[4], line[5]})

    total = {}
    for p, q in season.items():
        for i in q:
            total[p] = {i: q.count(i) for i in q}

    return total, teams


def plot_graph(data, team):
    year = sorted(data.keys())
    team = list(team)

    team_data = defaultdict(list)
    for i in team:
        for j in year:
            team_data[i].append(data[j].get(i, 0))

    plot = []
    plot.append(plt.bar(year, team_data[team[0]]))
    sum = team_data[team[0]]
    for i in range(1, len(team)):
        if i > 1:
            sum = list(map(add, sum, team_data[team[i-1]]))
        plot.append(plt.bar(year, team_data[team[i]], bottom=sum))

    plt.ylabel('Scores')
    plt.title('Matches Played By Team By Season')
    plt.xticks(year)
    plt.yticks(range(0, 210, 10))
    plt.legend((i[0] for i in plot), (team))

    plt.show()


if __name__ == "__main__":
    data, teams = data_collection()
    plot_graph(data, teams)
