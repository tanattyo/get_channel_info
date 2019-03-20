import os
from slackclient import SlackClient
from operator import itemgetter

def main():
    slack_token = os.getenv("SLACK_TOKEN")
    client = SlackClient(slack_token)

    channel_jsn = channel_list(client)

    # nameに応じてソート
    channel_jsn.sort(key=itemgetter('name'))

    for jsn_key in channel_jsn:
        if jsn_key['is_archived'] == False:

            if jsn_key['topic']['value'] != '':
                topic = '[Topic: ' + jsn_key['topic']['value'] + ']'
            else:
                topic = ''
            print('#' + jsn_key['name'] + ' `' + jsn_key['purpose']['value'] + topic + '`')

def channel_list(client):
    channels = client.api_call("channels.list")
    if channels['ok']:
        return channels['channels']
    else:
        return None

if __name__ == "__main__":
    main()
