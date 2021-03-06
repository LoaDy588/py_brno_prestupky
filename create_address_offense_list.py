"""Create lists of unique addresses and offenses."""
import csv


def main():
    # setup files
    data = open("raw/joined_clean.csv", "r", encoding="cp1250")
    output_address = open("raw/address.csv", "w", encoding="cp1250")
    output_offense = open("raw/offense.csv", "w", encoding="cp1250")
    csv_reader = csv.reader(data, delimiter=";", quoting=csv.QUOTE_NONNUMERIC)
    # setup lists
    address_list = []
    offense_list = []
    # go through data and add every unique offense or address to the lists
    for row in csv_reader:
        if not row[1] in address_list:
            print(row[1])
            address_list.append(row[1])
        if not row[2] in offense_list:
            print(row[2])
            offense_list.append(row[2])
    data.close()
    # write the address and offense lists to file
    for address in address_list:
        output_address.write(address + "\n")
    for offense in offense_list:
        output_offense.write(offense + "\n")
    output_address.close()
    output_offense.close()


if __name__ == "__main__":
    main()
