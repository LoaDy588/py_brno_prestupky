def join_files(files, out_file):
    file_out = open(out_file, "w", encoding="cp1250")
    for item in files:
        file_in = open(item, "r", encoding="cp1250")
        for line in file_in:
            file_out.write(line)
        file_in.close()
    file_out.close()


def clean_file(in_file, out_file):
    file_in = open(in_file, "r", encoding="cp1250")
    file_out = open(out_file, "w", encoding="cp1250")
    for line in file_in:
        if len(line) >= 60:
            clean = clean_line(line)
            if clean[-2:] == "\n\n":
                file_out.write(clean[:-1])
            else:
                file_out.write(clean)
    file_in.close()
    file_out.close()


def clean_line(line):
    data = line.split(";")
    new = data[0]+";"+data[1]+";"+data[2]+"\n"
    return new


def main():
    files = ["raw/prestupky1.txt", "raw/prestupky2.txt", "raw/prestupky3.txt"]
    files_clean = ["raw/clean1.csv", "raw/clean2.csv", "raw/clean3.csv"]
    for index, item in enumerate(files):
        clean_file(item, files_clean[index])

    join_files(files_clean, "raw/joined_clean.csv")


if __name__ == "__main__":
    main()
