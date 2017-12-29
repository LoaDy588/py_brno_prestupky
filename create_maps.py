import csv
import gmplot


def plot_total():
    data = open("data/data.csv", "r", encoding="cp1250")
    csv_reader = csv.reader(data, delimiter=";", quoting=csv.QUOTE_NONNUMERIC)
    lats = []
    lons = []
    for row in csv_reader:
        if row[2] != "0":
            lats.append(float(row[2]))
            lons.append(float(row[3]))
    data.close()
    gmap = gmplot.GoogleMapPlotter.from_geocode("Brno")
    gmap.heatmap(lats, lons, threshold=1, radius=0.01, opacity=0.6, dissipating=False)
    gmap.draw("websites/total.html")


def plot_traffic():
    data = open("data/data.csv", "r", encoding="cp1250")
    csv_reader = csv.reader(data, delimiter=";", quoting=csv.QUOTE_NONNUMERIC)
    lats = []
    lons = []
    for row in csv_reader:
        if row[2] != "0" and row[4] == "doprava":
            lats.append(float(row[2]))
            lons.append(float(row[3]))
    data.close()
    gmap = gmplot.GoogleMapPlotter.from_geocode("Brno")
    gmap.heatmap(lats, lons, threshold=1, radius=0.01, opacity=0.6, dissipating=False)
    gmap.draw("websites/traffic.html")


def plot_parking():
    data = open("data/data.csv", "r", encoding="cp1250")
    csv_reader = csv.reader(data, delimiter=";", quoting=csv.QUOTE_NONNUMERIC)
    lats = []
    lons = []
    for row in csv_reader:
        if row[2] != "0" and row[4] == "parkovani":
            lats.append(float(row[2]))
            lons.append(float(row[3]))
    data.close()
    gmap = gmplot.GoogleMapPlotter.from_geocode("Brno")
    gmap.heatmap(lats, lons, threshold=1, radius=0.01, opacity=0.6, dissipating=False)
    gmap.draw("websites/parking.html")


def plot_other():
    data = open("data/data.csv", "r", encoding="cp1250")
    csv_reader = csv.reader(data, delimiter=";", quoting=csv.QUOTE_NONNUMERIC)
    lats = []
    lons = []
    for row in csv_reader:
        if row[2] != "0" and row[4] != "doprava" and row[4] != "parkovani":
            lats.append(float(row[2]))
            lons.append(float(row[3]))
    data.close()
    gmap = gmplot.GoogleMapPlotter.from_geocode("Brno")
    gmap.heatmap(lats, lons, threshold=1, radius=0.01, opacity=0.6, dissipating=False)
    gmap.draw("websites/other.html")


plot_total()
plot_traffic()
plot_parking()
plot_other()
