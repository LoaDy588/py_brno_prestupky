import csv


def load_offense(file_location):
    data = open(file_location, "r", encoding="cp1250")
    offense_list = []
    for line in data:
        offense_list.append(line[:-1])
    return offense_list

def main():
    offense_list = load_offense("raw/offense.csv")
    offense_dict = {}
    output = open("data/offense_groups.csv", "w", encoding="cp1250")
    csv_writer = csv.writer(output, delimiter=";", quoting=csv.QUOTE_NONNUMERIC)
    for offense in offense_list:
        print(offense)
        group = input("Group:  ")
        offense_dict[offense] = group

    for key, value in offense_dict.items():
        csv_writer.writerow([key, value])
    output.close()

if __name__ == "__main__":
    main()
