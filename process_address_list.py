"""
Geocode the unique address list.

Uses LocationIQ API for geocoding the address. Can save the position in file
and be started again. This is because of LocationIQ API limit(10k requests/day)
"""
import time
import requests
import json
import csv


def load_save():
    """Load the save file."""
    save = open("save", "r")
    content = save.readlines()
    return int(content[0]), int(content[1])


def save_position(position, step):
    """Save current position."""
    save = open("save", "w")
    save.write(str(position) + "\n")
    save.write(str(step) + "\n")
    save.close()


def get_response(query):
    """Get response from the LocationIQ API."""
    url = "http://locationiq.org/v1/search.php"
    querystring = {"key": "API-KEY", "format": "json", "q": query}
    response = requests.request("GET", url, params=querystring)
    return response.text


def extract_location(response):
    """Extract location from the response of API, only accept Brno locations."""
    data = json.loads(response)
    for location in data:
        if "Brno-město" in location["display_name"]:
            return location["lat"], location["lon"]
        if "Brno" in location["display_name"]:
            return location["lat"], location["lon"]
    return str(0), str(0)


def get_location(data):
    """Get geo(lat, lon) location of an address."""
    response = get_response(data)
    return extract_location(response)


def main():
    # load saved position and number of steps to do.
    position, step = load_save()
    # Load address data
    data = open("raw/address.csv", "r", encoding="cp1250")
    data_lines = data.readlines()
    data.close()
    # prepare output
    output = open("data/address_coords.csv", "a", encoding="cp1250")
    csv_writer = csv.writer(output, delimiter=";", quoting = csv.QUOTE_NONNUMERIC)
    for i in range(step):
        # check if not at end of file
        if position < len(data_lines):
            # get address and geocode it
            line = data_lines[position]
            lat, lon = get_location(line)
            # write the address - geolocation data to output file
            newline = [line[:-1], lat, lon]
            csv_writer.writerow(newline)
            position += 1
            time.sleep(1) # wait a bit to not get rate limited
            print("Progress:" + str(i/step))
        else:
            break
    # save current position
    save_position(position+1, step)
    output.close()


if __name__ == "__main__":
    main()
