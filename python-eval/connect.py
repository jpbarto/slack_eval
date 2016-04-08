from slackclient import SlackClient
from json import dumps
from time import time

msg = {u'text': u'are you there?', u'ts': u'1457744613.000004', u'user': u'U0R09KE3S', u'team': u'T0R0BS0SV', u'type': u'message', u'channel': u'D0R1GD7A6'}
msg['ts'] = str(time ())

token = 'xoxb-26045948005-a4ZOZIyWsF5yWAYv5SH2BPjJ'
sc = SlackClient (token)
if sc.rtm_connect ():
    print "connected"
