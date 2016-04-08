from time import sleep
from slackclient import SlackClient

token = 'xoxb-26045948005-a4ZOZIyWsF5yWAYv5SH2BPjJ'
sc = SlackClient (token)
if sc.rtm_connect ():
    sc.rtm_send_message ('#general', 'generally speaking I am here')
    msgs = sc.rtm_read ()
    while len(msgs) == 0:
        sleep (1)
        msgs = sc.rtm_read ()
    for msg in msgs:
        print repr(msg)
else:
    print "Connection failed"
