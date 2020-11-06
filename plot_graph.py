import matplotlib.pyplot as plt


def plot(data, align, width, fontsize,
         xlabel, ylabel, title, plot_qty='all', rotation=0):
    '''
    use to plot graph. data: contain dict data type, \
    align: align name on x-axis, width: width of bar chart, \
    fontsize: variable size on x-axis, xlabel: name of x-axis, \
    ylabel: name of y-axis, title: title of chart, \
    plot_qty: take only limited data, rotation: take degree of rotation.
    '''
    if plot_qty == 'all':
        plot_qty = len(data.keys())
    x, y = zip(* sorted(data.items(),
               key=lambda i: i[1],
               reverse=True)[:plot_qty])

    plt.bar(x, y, align=align, width=width)
    plt.xticks(rotation=rotation, fontsize=fontsize)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()
