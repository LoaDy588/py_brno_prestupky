import csv


def main():
    data = open("raw/joined_clean.csv", "r", encoding="cp1250")
    output = open("raw/address.csv", "w", encoding="cp1250")
    csv_reader = csv.reader(data, delimiter=";", quoting=csv.QUOTE_NONNUMERIC)
    address_list = []
    for row in csv_reader:
        if not row[1] in address_list:
            print(row[1])
            address_list.append(row[1])
    data.close()
    for address in address_list:
        output.write(address + "\n")
    output.close()


if __name__ == "__main__":
    main()
