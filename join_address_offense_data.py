import csv


def load_address(file_location):
    address_dict = {}
    empty_count = 0
    address_file = open(file_location, "r", encoding="cp1250")
    csv_reader = csv.reader(address_file, delimiter=";", quoting=csv.QUOTE_NONNUMERIC)
    for row in csv_reader:
        address_dict[row[0]] = (row[1], row[2])
        if row[1] == "0":
            empty_count += 1
    address_file.close()
    print("Null address:" + str(empty_count))
    return address_dict


def load_offense(file_location):
    return "foobar"


def main():
    address_dict = load_address("data/address_coords.csv")
    data = open("raw/joined_clean.csv", "r", encoding="cp1250")
    csv_reader = csv.reader(data, delimiter=";", quoting=csv.QUOTE_NONNUMERIC)
    output = open("data/data.csv", "w", encoding="cp1250")
    csv_writer = csv.writer(output, delimiter=";", quoting=csv.QUOTE_NONNUMERIC)
    for row in csv_reader:
        if row[1] in address_dict:
            location = address_dict[row[1]]
            newline = [row[0], row[1], location[0], location[1], row[2]]
        else:
            newline = [row[0], row[1], "0", "0", row[2]]
        csv_writer.writerow(newline)
    data.close()
    output.close()


if __name__ == "__main__":
    main()
