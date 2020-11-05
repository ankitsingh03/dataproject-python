import csv
import matplotlib.pyplot as plt
from operator import add


def data_collection():
    season = {}
    duplicate = set()
    list_team = set()
    # open the csv file
    with open('matches.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        # filtering data
        for line in csv_reader:
            if line[0] == 'id':
                continue
            if line[1] not in duplicate:
                duplicate.add(line[1])
                season[line[1]] = []
                season[line[1]].append(line[4])
                season[line[1]].append(line[5])
                list_team.add(line[4])
                list_team.add(line[5])

            else:
                season[line[1]].append(line[4])
                season[line[1]].append(line[5])
                list_team.add(line[4])
                list_team.add(line[5])

    total = {}
    for p, q in season.items():
        total[p] = {i: q.count(i) for i in q}

    return total, list_team


def plot_graph(data, team):
    year = sorted(data.keys())
    team = list(team)

    team_data = {}
    for i in team:
        lst = []
        for j in year:
            lst.append(data[j].get(i, 0))
        team_data[i] = lst

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
    data, team = data_collection()
    plot_graph(data, team)
