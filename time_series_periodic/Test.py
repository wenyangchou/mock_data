from matplotlib import pyplot as plt

from time_series_periodic.gen import gen_data

if __name__ == '__main__':
    count = 10000
    data = gen_data(count,3)
    x = [i for i in range(count)]
    plt.plot(x,data)
    plt.show()