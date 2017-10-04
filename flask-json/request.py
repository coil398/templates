import json
import requests


def main():
    headers = {'Content-Type': 'application/json'}

    string = {
        'name': 'pepper',
        'ip' : '192.168.100.100',
        'alProxy': 'ALSystem',
        'method': 'reboot',
        'arguments': ''
        }

    r = requests.post('http://192.168.100.62:8000/api', headers=headers, data=json.dumps(string))
    print(r.json())


if __name__ == '__main__':
    main()
