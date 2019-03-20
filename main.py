import os
import time
from slackclient import SlackClient
from operator import itemgetter

def main():

    slack_token = os.getenv("SLACK_TOKEN")
    client = SlackClient(slack_token)

    channel_jsn = channel_list(client)

    # nameに応じてソート
    channel_jsn.sort(key=itemgetter('name'))

    list_txt = ''
    for jsn_key in channel_jsn:
        if jsn_key['is_archived'] == False:

            if jsn_key['topic']['value'] != '':
                topic = '[Topic: ' + jsn_key['topic']['value'] + ']'
            else:
                topic = ''
            txt = '<#' + jsn_key['id'] + '> `' + jsn_key['purpose']['value'] + topic + '`' + '\n'
            list_txt += txt


    send_message(list_txt)

def send_message(txt):

    slack_token_whale = os.getenv('SLACK_TOKEN_WHALE')
    sc = SlackClient(slack_token_whale)

    if sc.rtm_connect():
        sc.rtm_send_message("test", txt)
    else:
        print("Connection Failed, invalid token?")

def channel_list(client):

    channels = client.api_call("channels.list")
    if channels['ok']:
        return channels['channels']
    else:
        return None

if __name__ == "__main__":
    main()
