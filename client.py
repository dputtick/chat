#!/usr/bin/env python3

import os

import requests


SERVER_IP = str(os.environ.get('SERVER'))
PORT = 8000


class MessageSession(requests.Session):

    @property
    def server_url(self):
        return "http://{}:{}/messages".format(SERVER_IP, PORT)

    def get_message(self):
        r = self.get(self.server_url)
        return r.status_code, r.text

    def send_message(self, message):
        payload = {'message': message}
        r = self.post(self.server_url, params=payload)
        return r.status_code, r.text

    def run(self):
        while True:
            next_action = input('Next action: ')
            if next_action == 'get':
                status, message = self.get_message()
                print("Message:", message)
            else:
                message = input("Message: ")
                status, mess_id = self.send_message(message)
                print("Message id: {}. Status: {}".format(mess_id, status))


if __name__ == '__main__':
    print(SERVER_IP)
    session = MessageSession()
    session.run()
