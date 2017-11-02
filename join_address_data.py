def load_address(file_location):
    address_dict = {}
    address_file = open(file_location, "r", encoding="cp1250")
    for line in address_file:
        line_data = line.split(";")
        address_dict[line_data[0]] = (line_data[1], line_data[2][:-1])
    address_file.close()
    return address_dict


def create_line(data, location):
    newline = data[0]+";"+data[1]+";"
    newline += location[0]+";"+location[1]+";"
    newline += data[2]
    return newline


def main():
    address_dict = load_address("data/address_coords.csv")
    data = open("raw/joined_clean.csv", "r", encoding="cp1250")
    output = open("data/data.csv", "w", encoding="cp1250")
    for line in data:
        line_data = line.split(";")
        newline = ""
        if line_data[1] in address_dict:
            newline = create_line(line_data, address_dict[line_data[1]])
        else:
            newline = create_line(line_data, (str(0), str(0)))
        output.write(newline)
    data.close()
    output.close()


if __name__ == "__main__":
    main()
