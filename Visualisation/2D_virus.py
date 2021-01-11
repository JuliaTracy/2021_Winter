import matplotlib.pyplot as plt
import datetime
def show():
    num = [
        291, 440, 571, 830, 1287, 1975, 2744, 4535, 5597, 7736, 9720, 11821,
        14111, 17238, 20471, 24363, 28060, 31211, 34598, 37251, 40235
    ]
    x = [
        datetime.datetime.now() + datetime.timedelta(days=i-1)
        for i in range(-len(num), 0)
    ]

    plt.plot(x, num)
    plt.gcf().autofmt_xdate()
    plt.xlabel("Date")
    plt.ylabel("Number")
    plt.title("Confirmed Novel Coronavirus Patients")
    plt.show()
show()
