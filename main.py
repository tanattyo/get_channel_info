import os
import pprint
import json
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
            print('#' + jsn_key['name'] + '\n' + '```' + jsn_key['purpose']['value'])
            if jsn_key['topic']['value'] != '':
                print('topic: ' +jsn_key['topic']['value'])
            print('```')

def channel_list(client):
    channels = client.api_call("channels.list")
    if channels['ok']:
        return channels['channels']
    else:
        return None

if __name__ == "__main__":
    main()
