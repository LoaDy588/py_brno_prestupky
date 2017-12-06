import matplotlib.pyplot as plt
import csv


def load_into_dict(file_location):
    data_dict = {}
    data = open(file_location, "r", encoding="cp1250")
    csv_reader = csv.reader(data, delimiter=";", quoting=csv.QUOTE_NONNUMERIC)
    for row in csv_reader:
        data_dict[row[0]] = row[1]
    data.close()
    return data_dict


def sort_dates(date_dict):
    dates = list(date_dict.keys())
    dates_sorted = sorted(dates)[1:]
    values_sorted = []
    for i in range(len(dates_sorted)):
        values_sorted.append(date_dict[dates_sorted[i]])
    return dates_sorted, values_sorted


def normalize(data):
    total = sum(data)
    normalized = []
    for item in data:
        normalized.append((item/total*100))
    return normalized


def graph_days(days):
    plt.title("Poměr přestupků na den")
    x = (1, 2, 3, 4, 5, 6, 7)
    plt.bar(x, normalize(days), 0.35)
    plt.ylabel("Procento přestupků")
    plt.xlabel("Den v týdnu")
    plt.xticks(x, ("pondělí", "úterý", "středa", "čtvrtek",
               "pátek", "sobota", "neděle"))
    plt.savefig("graphs/days.png", bbox_inches="tight")
    plt.close()


def graph_weeks(weeks):
    plt.title("Přestupky za týden")
    x_labels = (0, 26, 53)
    plt.plot(weeks)
    plt.ylabel("Počet přestupků")
    plt.xticks(x_labels, ("1.1.2016", "1.7.2016", "1.1.2017"), rotation=45)
    plt.savefig("graphs/weeks.png", bbox_inches="tight")
    plt.close()


def graph_groups(groups):
    plt.title("Typ přestupků")
    x = (1, 2, 3, 4)
    plt.bar(x, normalize(groups), 0.9)
    plt.xticks(x, ("Dopravní", "Parkování", "Pořádkové", "Jiné"))
    plt.ylabel("Procento přestupků")
    plt.xlabel("Typ")
    plt.savefig("graphs/groups.png", bbox_inches="tight")
    plt.close()


def main():
    date_dict = load_into_dict("data/date_count.csv")
    groups_dict = load_into_dict("data/group_count.csv")
    groups = []
    groups.append(groups_dict["doprava"])
    groups.append(groups_dict["parkovani"])
    groups.append(groups_dict["poradek"]+groups_dict["souziti"]+groups_dict["majetek"])
    groups.append(groups_dict["vyhlasky"]+groups_dict["navykove"]
                  + groups_dict["krive"] + groups_dict["jine"])
    dates_sorted, values_sorted = sort_dates(date_dict)
    days = [0, 0, 0, 0, 0, 0, 0]
    for i in range(len(values_sorted)):
        days[(i % 7)-3] += values_sorted[i]
    weeks = []
    week = 0
    for i in range(len(values_sorted)):
        if i % 7 == 0:
            weeks.append(week)
            week = values_sorted[i]
        else:
            week += values_sorted[i]
    graph_days(days)
    graph_weeks(weeks)
    graph_groups(groups)


if __name__ == "__main__":
    main()
