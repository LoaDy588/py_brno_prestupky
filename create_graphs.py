"""Create graphs from data."""
import matplotlib.pyplot as plt
import csv
import collections


def load_into_dict(file_location):
    """Load data into dict."""
    data_dict = {}
    data = open(file_location, "r", encoding="cp1250")
    csv_reader = csv.reader(data, delimiter=";", quoting=csv.QUOTE_NONNUMERIC)
    for row in csv_reader:
        data_dict[row[0]] = row[1]
    data.close()
    return data_dict


def sort_date_values(date_dict):
    """Sort date values chronologically - date must be in YYYY-MM-DD format."""
    dates = list(date_dict.keys())
    dates_sorted = sorted(dates)[1:]
    values_sorted = []
    for i in range(len(dates_sorted)):
        values_sorted.append(date_dict[dates_sorted[i]])
    return values_sorted


def normalize(data, data_sum):
    """Normalize data, can be normalized against external sum."""
    normalized = []
    for item in data:
        normalized.append((item/data_sum*100))
    return normalized


def graph_days(date_values):
    days = [0, 0, 0, 0, 0, 0, 0]
    for i in range(len(date_values)):
        # shift days by 3, 2016 didn't start on monday.
        days[(i % 7)-3] += date_values[i]

    plt.figure(figsize=(10, 10), dpi=240)
    plt.title("Poměr přestupků na den")
    x = (1, 2, 3, 4, 5, 6, 7)
    plt.bar(x, normalize(days, sum(days)), 0.75)
    plt.ylabel("Procento přestupků")
    plt.xlabel("Den v týdnu")
    plt.xticks(x, ("pondělí", "úterý", "středa", "čtvrtek",
               "pátek", "sobota", "neděle"))
    plt.savefig("graphs/days.png", bbox_inches="tight")
    plt.close()


def graph_weeks(date_values):
    weeks = []
    week = 0
    for i in range(len(date_values)):
        if i % 7 == 0:
            weeks.append(week)
            week = date_values[i]
        else:
            week += date_values[i]

    plt.figure(figsize=(20, 10), dpi=240)
    plt.title("Přestupky za týden")
    x_labels = (0, 26, 53)
    plt.plot(weeks)
    plt.ylabel("Počet přestupků")
    plt.xticks(x_labels, ("1.1.2016", "1.7.2016", "1.1.2017"), rotation=45)
    plt.savefig("graphs/weeks.png", bbox_inches="tight")
    plt.close()


def graph_groups(groups_dict):
    groups = []
    # sort groups into bigger groups - no need for that much detail.
    groups.append(groups_dict["doprava"])
    groups.append(groups_dict["parkovani"])
    groups.append(groups_dict["poradek"]+groups_dict["souziti"]+groups_dict["majetek"])
    groups.append(groups_dict["vyhlasky"]+groups_dict["navykove"]
                  + groups_dict["krive"] + groups_dict["jine"])

    plt.figure(figsize=(10, 10), dpi=240)
    plt.title("Typ přestupků")
    x = (1, 2, 3, 4)
    plt.bar(x, normalize(groups, sum(groups)), 0.9)
    plt.xticks(x, ("Dopravní", "Parkování", "Pořádkové", "Jiné"))
    plt.ylabel("Procento přestupků")
    plt.xlabel("Typ")
    plt.savefig("graphs/groups.png", bbox_inches="tight")
    plt.close()


def graph_address(address_dict):
    # sort address_dict into ordered dict
    address_dict_sorted = collections.OrderedDict(sorted(address_dict.items(),
                                                  key=lambda t: t[1]))
    address = []
    values = []
    # get top 25 addresses
    for i in range(25):
        addr, val = address_dict_sorted.popitem()
        address.append(addr.split(", ")[0])
        values.append(val)

    plt.figure(figsize=(9, 6), dpi=240)
    plt.title("Top50 adres")
    x = [x+1 for x in range(25)]
    plt.bar(x, normalize(values, sum(address_dict.values())), 0.5)
    plt.xticks(x, tuple(address), rotation="vertical")
    plt.ylabel("Procento přestupků")
    plt.xlabel("Adresa")
    plt.savefig("graphs/address.png", bbox_inches="tight")
    plt.close()


def main():
    date_dict = load_into_dict("data/date_count.csv")
    groups_dict = load_into_dict("data/group_count.csv")
    address_dict = load_into_dict("data/address_count.csv")
    date_values_sorted = sort_date_values(date_dict)
    graph_days(date_values_sorted)
    graph_weeks(date_values_sorted)
    graph_groups(groups_dict)
    graph_address(address_dict)


if __name__ == "__main__":
    main()
