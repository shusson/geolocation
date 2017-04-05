import json


def parse_location(location):
    return {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [location["longitude"], location["latitude"]]
        },
        "properties": {
            "name": location["city"]
        }
    }


def main():
    with open('locations.json', 'r') as f:
        read_data = ''.join(f.readlines())
        locations = json.loads(read_data)
        u_locations = {}
        geo_locations = {
            "type": "FeatureCollection",
            "features": []
        }
        for location in locations:
            if not location['city']:
                continue
            elif location['city'] in u_locations:
                u_locations[location['city']]['count'] += 1
                geo_locations["features"].append(parse_location(location))
            else:
                location['count'] = 1
                u_locations[location['city']] = location
                geo_locations["features"].append(parse_location(location))

        fw = open('u_locations.json', 'w')

        fw.write(json.dumps(u_locations, sort_keys=True, indent=4))
        fw.close()

        fg = open('geo_locations.json', 'w')

        fg.write(json.dumps(geo_locations, sort_keys=False, indent=4))
        fg.close()


if __name__ == "__main__":
    main()