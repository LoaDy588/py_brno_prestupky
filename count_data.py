import csv


def save_data(file_location, data):
    output = open(file_location, "w", encoding="cp1250")
    csv_writer = csv.writer(output, delimiter=";", quoting=csv.QUOTE_NONNUMERIC)
    for key, value in data.items():
        csv_writer.writerow([key, value])


def main():
    data = open("data/data.csv", "r", encoding="cp1250")
    csv_reader = csv.reader(data, delimiter=";", quoting=csv.QUOTE_NONNUMERIC)
    address_count = {}
    date_count = {}
    for row in csv_reader:
        if row[0] in date_count:
            date_count[row[0]] += 1
        else:
            date_count[row[0]] = 1

        if row[1] in address_count:
            address_count[row[1]] += 1
        else:
            address_count[row[1]] = 1
    save_data("data/address_count.csv", address_count)
    save_data("data/date_count.csv", date_count)


if __name__ == "__main__":
    main()
