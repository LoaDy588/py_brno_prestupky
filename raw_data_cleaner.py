"""
Clean up the files(delete empty or short/incomplete lines),
change the formatting a bit and join  the files together.
"""
import csv


def join_files(files, out_file):
    """Join two files together."""
    # setup output file
    file_out = open(out_file, "w", encoding="cp1250")
    csv_writer = csv.writer(file_out, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)

    # go through input files and write them to output
    for item in files:
        file_in = open(item, "r", encoding="cp1250")
        csv_reader = csv.reader(file_in, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
        for row in csv_reader:
            csv_writer.writerow(row)
        file_in.close()
    file_out.close()


def clean_file(in_file, out_file):
    """Clean in_file and write to to out_file."""
    # setup in/out files
    file_in = open(in_file, "r", encoding="cp1250")
    file_out = open(out_file, "w", encoding="cp1250")
    csv_writer = csv.writer(file_out, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
    # go through every every line and "clean it"
    for line in file_in:
        if len(line) >= 60:  # dont process lines shorter than 60 symbols
            data = line.split(";")  # split line
            if data[2][-2:] == "\n\n":  # remove double newline
                clean = [data[0], data[1], data[2][:-2]]
            elif data[2][-1:] == "\n":  # remove newline
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
    # go through every raw data file
    for index, item in enumerate(files):
        clean_file(item, files_clean[index])
    # join them
    join_files(files_clean, "raw/joined_clean.csv")


if __name__ == "__main__":
    main()
