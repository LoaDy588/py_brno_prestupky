"""Join the cleaned raw data, offense-group data and address-geolocation data."""
import csv


def load_address(file_location):
    """Load address-geolocation data into dict."""
    address_dict = {}
    empty_count = 0  # counter for counting address without geolocation.
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
    """Load offense-group data into dict."""
    offense_dict = {}
    offense_file = open(file_location, "r", encoding="cp1250")
    csv_reader = csv.reader(offense_file, delimiter=";", quoting=csv.QUOTE_NONNUMERIC)
    for row in csv_reader:
        offense_dict[row[0]] = row[1]
    offense_file.close()
    return offense_dict


def main():
    # load the data
    address_dict = load_address("data/address_coords.csv")
    offense_dict = load_offense("data/offense_groups.csv")
    data = open("raw/joined_clean.csv", "r", encoding="cp1250")
    csv_reader = csv.reader(data, delimiter=";", quoting=csv.QUOTE_NONNUMERIC)
    # prepare output
    output = open("data/data.csv", "w", encoding="cp1250")
    csv_writer = csv.writer(output, delimiter=";", quoting=csv.QUOTE_NONNUMERIC)
    # go every joined data line and process
    for row in csv_reader:
        # change date format to alphabetically sortable format
        date = row[0].split(".")
        if len(date) >= 3:
            date_new = date[2]+"-"+date[1]+"-"+date[0]
        else:
            date_new = "0000-00-00"
        # find matching geolocation
        if row[1] in address_dict:
            location = address_dict[row[1]]
        else:
            newline = ["0", "0"]
        # find matching offense group
        if row[2] in offense_dict:
            group = offense_dict[row[2]]
        else:
            group = "jine"
        # create new line and write it
        newline = [date_new, row[1], location[0], location[1], group]
        csv_writer.writerow(newline)
    data.close()
    output.close()


if __name__ == "__main__":
    main()
