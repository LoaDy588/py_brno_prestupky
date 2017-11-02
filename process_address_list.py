import time
import requests
import json


def load_save():
    save = open("save", "r")
    content = save.readlines()
    return int(content[0]), int(content[1])


def save_position(position, step):
    save = open("save", "w")
    save.write(str(position) + "\n")
    save.write(str(step) + "\n")


def get_response(query):
    url = "http://locationiq.org/v1/search.php"
    querystring = {"key": "9cc7a3b0a8465b", "format": "json", "q": query}
    response = requests.request("GET", url, params=querystring)
    return response.text


def extract_location(response):
    data = json.loads(response)
    for location in data:
        if "Brno-město" in location["display_name"]:
            return location["lat"], location["lon"]
        if "Brno" in location["display_name"]:
            return location["lat"], location["lon"]
    return str(0), str(0)


def get_location(data):
    response = get_response(data)
    lat, lon = extract_location(response)
    return data[:-1]+";"+lat+";"+lon+"\n"


def main():
    position, step = load_save()
    data = open("raw/address.csv", "r", encoding="cp1250")
    data_lines = data.readlines()
    data.close()
    output = open("data/address_coords.csv", "a", encoding="cp1250")
    for i in range(step):
        if position < len(data_lines):
            line = data_lines[position]
            newline = get_location(line)
            output.write(newline)
            position += 1
            time.sleep(1)
            print("Progress:" + str(i/step))
        else:
            break
    save_position(position+1, step)
    output.close()


if __name__ == "__main__":
    main()
