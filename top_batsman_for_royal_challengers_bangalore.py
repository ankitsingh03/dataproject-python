import csv
from collections import defaultdict
from plot_graph import plot


def data_collection():
    '''
    collect all the data, batsman name and total runs over the history of IPL.
    '''

    top_batsman = defaultdict(int)
    # open the csv file and clean data
    with open('deliveries.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        csv_reader.__next__()
        for line in csv_reader:
            name = line[6]
            run = int(line[-6])
            top_batsman[name] += int(run)

    return top_batsman


if __name__ == "__main__":
    data = data_collection()
    plot(data, 'center',
         0.7, 15,
         'Top Batsman', 'Total Runs Scored',
         "Top Batsman Of Royal Challengers Bangalore", 10
         )
