from json import dumps

from httplib2 import Http
import sys

def main(status):
    """Hangouts Chat incoming webhook quickstart."""
    url = 'https://chat.googleapis.com/v1/spaces/AAAABvIHllo/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=0NMrJ0M4iFQe30VsuNABmBvbK8Wm3tPsCgFStSnQn2E%3D'
    bot_message = {
        'text': status}
    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}
    http_obj = Http()
    response = http_obj.request(
        uri=url,
        method='POST',
        headers=message_headers,
        body=dumps(bot_message),
    )
    print(response)


if __name__ == '__main__':
    main(sys.argv[1])
