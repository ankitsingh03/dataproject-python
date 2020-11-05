import csv
import matplotlib.pyplot as plt


# collect all the data, country and noumber of umpire over the history of IPL.
def data_collection():
    umpire_name = []
    with open('umpire_data.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            if line[0] == "Umpire":
                continue
            if line[1] != 'India':
                umpire_name.append(line[1])

    umpire_count = {}
    duplicate = set()
    for i in umpire_name:
        if i not in duplicate:
            umpire_count[i] = umpire_name.count(i)
            duplicate.add(i)

    return umpire_count


# plot details
def plot_graph(data):
    umpire_country = []
    umpire_count = []

    # sort according to country
    for i in sorted(data.items()):
        umpire_country.append(i[0])
        umpire_count.append(i[1])

    x = umpire_country
    y = umpire_count

    plt.bar(x, y, align='center', width=0.7)
    plt.xticks(fontsize=15)
    plt.xlabel('Country')
    plt.ylabel('Number Of Umpires')
    plt.title("Foreign Umpire Analysis")
    plt.show()


if __name__ == "__main__":
    data = data_collection()
    plot_graph(data)
