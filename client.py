#!/usr/bin/env python3

import sys
import os

import requests


SERVER_IP = str(os.environ.get('SERVER'))
PORT = 8000


def get_message(mess_id):
    payload = {'lookup': mess_id}
    r = requests.get(SERVER_IP + '/messages', params=payload)
    return r.status_code, r.text


def send_message(message):
    payload = {'send': message}
    r = requests.post(SERVER_IP + '/messages', params=payload)
    return r.status_code, r.text


def main():
    if sys.argv[0] == 'send':
        message = input("Message: ")
        status, mess_id = send_message(message)
        print("Message id: {}. Status: {}".format(mess_id, status))
    elif sys.argv[0] == 'get':
        mess_id = input("Message id? ")
        status, message = get_message(mess_id)
        print("Message:", message)


if __name__ == '__main__':
    print(SERVER_IP)
    main()
