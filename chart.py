import matplotlib.pyplot as plt


class Chart:
    def __init__(self, data, title):
        self.data = data
        self.title = title

    def show(self):
        plt.hist(self.data, 20, (self.data[0], self.data[len(self.data)-1]), color='green',
                 histtype='bar', rwidth=0.8)
        plt.title(self.title)
        plt.show()
