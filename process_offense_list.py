"""Go through unique offenses and let user input their groups."""
import csv


def load_offense(file_location):
    """Load the unique offense list file."""
    data = open(file_location, "r", encoding="cp1250")
    offense_list = []
    for line in data:
        offense_list.append(line[:-1])
    return offense_list


def main():
    """Let user input the offense groups."""
    # prepare list and output dict
    offense_list = load_offense("raw/offense.csv")
    offense_dict = {}
    # prepare file output
    output = open("data/offense_groups.csv", "w", encoding="cp1250")
    csv_writer = csv.writer(output, delimiter=";", quoting=csv.QUOTE_NONNUMERIC)
    # go through every offense and let user input the group
    for offense in offense_list:
        print(offense)
        group = input("Group:  ")
        offense_dict[offense] = group
    # write the offense - group pairs to output file
    for key, value in offense_dict.items():
        csv_writer.writerow([key, value])
    output.close()

if __name__ == "__main__":
    main()
