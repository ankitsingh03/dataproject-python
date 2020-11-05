import csv
import matplotlib.pyplot as plt


# collect all the data, batsman name and total runs over the history of IPL.
def data_collection():
    top_batsman = {}
    duplicate = set()

    # open the csv file and clean data
    with open('deliveries.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            if line[0] == 'match_id':
                continue
            if line[2] == "Royal Challengers Bangalore":
                if line[6] not in duplicate:
                    duplicate.add(line[6])
                    top_batsman[line[6]] = int(line[-6])
                else:
                    top_batsman[line[6]] = top_batsman[line[6]] + int(line[-6])

    return top_batsman


def plot_graph(data):
    top_batsman = []
    top_runs = []
    sorted_data = sorted(data.items(), key=lambda i: i[1], reverse=True)

    # collect top 10 data
    for i in range(10):
        top_batsman.append(sorted_data[i][0])
        top_runs.append(sorted_data[i][1])

    x = top_batsman
    y = top_runs

    # plot details
    plt.bar(x, y, align='center', width=0.7)
    plt.xticks(fontsize=15)
    plt.xlabel('Top Batsman')
    plt.ylabel('Total Runs Scored')
    plt.title("Top Batsman Of Royal Challengers Bangalore")
    plt.show()


if __name__ == "__main__":
    data = data_collection()
    plot_graph(data)
