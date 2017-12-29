"""Count address, date and groups in data."""
import csv


def save_data(file_location, data):
    """Save data to a file in key;value format."""
    output = open(file_location, "w", encoding="cp1250")
    csv_writer = csv.writer(output, delimiter=";", quoting=csv.QUOTE_NONNUMERIC)
    for key, value in data.items():
        csv_writer.writerow([key, value])
    output.close()

def main():
    # open data
    data = open("data/data.csv", "r", encoding="cp1250")
    csv_reader = csv.reader(data, delimiter=";", quoting=csv.QUOTE_NONNUMERIC)
    # dicts for storing count data
    address_count = {}
    date_count = {}
    group_count = {}
    # go through every line and add to counting dicts
    for row in csv_reader:
        if row[0] in date_count:
            date_count[row[0]] += 1
        else:
            date_count[row[0]] = 1

        if row[1] in address_count:
            address_count[row[1]] += 1
        else:
            address_count[row[1]] = 1

        if row[4] in group_count:
            group_count[row[4]] += 1
        else:
            group_count[row[4]] = 1
    # save data
    save_data("data/address_count.csv", address_count)
    save_data("data/date_count.csv", date_count)
    save_data("data/group_count.csv", group_count)


if __name__ == "__main__":
    main()
