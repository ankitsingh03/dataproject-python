import csv
import matplotlib.pyplot as plt


# collect all the data, team name and total runs over the history of IPL.
def data_collection():
    teams_runs = {}
    duplicate = set()

    # open the csv file and clean data
    with open('deliveries.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            if line[0] == 'match_id':
                continue
            if line[2] not in duplicate:
                duplicate.add(line[2])
                teams_runs[line[2]] = int(line[-4])
            else:
                teams_runs[line[2]] = teams_runs[line[2]] + int(line[-4])
    return teams_runs


# plot details
def plot_graph(data):
    teams = []
    runs = []
    for i in sorted(data.items(), key=lambda i: (i[1], i[0]), reverse=True):
        teams.append(i[0])
        runs.append(i[1])
    x = teams
    y = runs

    plt.bar(x, y, align='center', width=0.8)
    plt.xticks(rotation="20", fontsize=10)
    plt.ylabel('Total runs scored')
    plt.title('Total Runs Scored By Team')
    plt.show()


if __name__ == "__main__":
    data = data_collection()
    plot_graph(data)
