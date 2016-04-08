from time import sleep
from slackclient import SlackClient

token = 'xoxb-25048547013-hJlRqzBJTW6lhFOrSesERqSU'
sc = SlackClient (token)
if sc.rtm_connect ():
    while True:
        msgs = sc.rtm_read ()
        while len(msgs) == 0:
            sleep (1)
            msgs = sc.rtm_read ()
        for msg in msgs:
            print repr(msg)
else:
    print "Connection failed"
