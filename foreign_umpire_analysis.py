import csv
from collections import defaultdict
from plot_graph import plot


def data_collection():
    '''
    collect all the data, country and number \
    of umpire over the history of IPL.
    '''
    umpire_count = defaultdict(int)
    with open('umpire_data.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        csv_reader.__next__()
        for line in csv_reader:
            if line[1] == "India":
                continue
            umpire_count[line[1]] += 1

    return umpire_count


if __name__ == "__main__":
    data = data_collection()
    # plot_graph(data)
    plot(data, 'center',
         0.7, 15, 'Country',
         'Number Of Umpires',
         "Foreign Umpire Analysis"
         )
