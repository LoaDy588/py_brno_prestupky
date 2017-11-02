def main():
    data = open("raw/joined_clean.csv", "r", encoding="cp1250")
    output = open("raw/address.csv", "w", encoding="cp1250")
    address_list = []
    for line in data:
        line_split = line.split(";")
        if not line_split[1] in address_list:
            print(line_split[1])
            address_list.append(line_split[1])
    data.close()
    for address in address_list:
        output.write(address + "\n")
    output.close()


if __name__ == "__main__":
    main()
