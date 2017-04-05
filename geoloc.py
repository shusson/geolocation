import requests
import json
import re

def main():
    with open('sgc_ips.json', 'r') as f:
        read_data = ''.join(f.readlines())
        v = re.sub(r'[^\x00-\x7f]', r'', read_data)
        users = json.loads(v)
        locations = []
        for user in users:
            url = 'http://freegeoip.net/json/' + user['ip']
            r = requests.get(url)
            locations.append(r.json())

        fw = open('locations.json', 'w')

        fw.write(json.dumps(locations, sort_keys=True, indent=4))
        fw.close()

if __name__ == "__main__":
    main()