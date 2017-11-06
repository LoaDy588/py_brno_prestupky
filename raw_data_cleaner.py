import csv


def join_files(files, out_file):
    file_out = open(out_file, "w", encoding="cp1250")
    csv_writer = csv.writer(file_out, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
    for item in files:
        file_in = open(item, "r", encoding="cp1250")
        csv_reader = csv.reader(file_in, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
        for row in csv_reader:
            csv_writer.writerow(row)
        file_in.close()
    file_out.close()


def clean_file(in_file, out_file):
    file_in = open(in_file, "r", encoding="cp1250")
    file_out = open(out_file, "w", encoding="cp1250")
    csv_writer = csv.writer(file_out, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
    for line in file_in:
        if len(line) >= 60:
            data = line.split(";")
            if data[2][-2:] == "\n\n":
                clean = [data[0], data[1], data[2][:-2]]
            elif data[2][-1:] == "\n":
                clean = [data[0], data[1], data[2][:-1]]
            else:
                clean = [data[0], data[1], data[2]]
            csv_writer.writerow(clean)
        else:
            continue
    file_in.close()
    file_out.close()


def main():
    files = ["raw/prestupky1.txt", "raw/prestupky2.txt", "raw/prestupky3.txt"]
    files_clean = ["raw/clean1.csv", "raw/clean2.csv", "raw/clean3.csv"]
    for index, item in enumerate(files):
        clean_file(item, files_clean[index])

    join_files(files_clean, "raw/joined_clean.csv")


if __name__ == "__main__":
    main()
