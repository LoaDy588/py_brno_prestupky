"""Create crude google maps heatmaps from data. Uses gmplot lib."""
import csv
import gmplot


def plot(items, invert, output):
    """plot specified groups from data. Outputs html website."""
    data = open("data/data.csv", "r", encoding="cp1250")
    csv_reader = csv.reader(data, delimiter=";", quoting=csv.QUOTE_NONNUMERIC)
    lats = []
    lons = []

    # go through data and filter it according to the "rules"
    for row in csv_reader:
        if invert:
            if row[2] != "0" and row[4] not in items:
                lats.append(float(row[2]))
                lons.append(float(row[3]))
        else:
            if row[2] != "0" and row[4] in items:
                lats.append(float(row[2]))
                lons.append(float(row[3]))
    data.close()

    # create the .html with the map
    # parameters needs to be edited afterwards in .html for better visuals
    gmap = gmplot.GoogleMapPlotter.from_geocode("Brno")
    gmap.heatmap(lats, lons, threshold=1, radius=0.01, opacity=0.6, dissipating=False)
    gmap.draw(output)


# create different maps
plot([], True, "websites/total.html")
plot(["doprava"], False, "websites/traffic.html")
plot(["parkovani"], False, "websites/parking.html")
plot(["parkovani", "doprava"], True, "websites/other.html")
