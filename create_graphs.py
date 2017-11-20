import matplotlib.pyplot as plt
import csv


def load_into_dict(file_location):
    data_dict = {}
    data = open(file_location, "r", encoding="cp1250")
    csv_reader = csv.reader(data, delimiter=";", quoting=csv.QUOTE_NONNUMERIC)
    for row in csv_reader:
        data_dict[row[0]] = row[1]
    return data_dict


def main():
    date_dict = load_into_dict("data/date_count.csv")
    dates = list(date_dict.keys())
    dates_sorted = sorted(dates)[1:]
    values_sorted = []
    print(len(dates_sorted))
    for i in range(len(dates_sorted)):
        values_sorted.append(date_dict[dates_sorted[i]])
    days = [0, 0, 0, 0, 0, 0, 0]
    for i in range(len(values_sorted)):
        days[i % 7] += values_sorted[i]
    print(days)
    plt.plot(values_sorted)
    plt.show()


if __name__ == "__main__":
    main()
