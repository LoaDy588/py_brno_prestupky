def save_data(file_location, data):
    output = open(file_location, "w", encoding="cp1250")
    for key, value in data.items():
        output.write(key+";"+str(value)+"\n")


def main():
    data = open("data/data.csv", "r", encoding="cp1250")
    address_count = {}
    date_count = {}
    for line in data:
        line_data = line.split(";")
        if line_data[0] in date_count:
            date_count[line_data[0]] += 1
        else:
            date_count[line_data[0]] = 1

        if line_data[1] in address_count:
            address_count[line_data[1]] += 1
        else:
            address_count[line_data[1]] = 1
    save_data("data/address_count.csv", address_count)
    save_data("data/date_count.csv", date_count)


if __name__ == "__main__":
    main()
