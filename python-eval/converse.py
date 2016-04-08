from time import sleep
from slackclient import SlackClient

def get_messages (client):
    msgs = client.rtm_read ()
    while len(msgs) == 0:
        sleep (1)
        msgs = client.rtm_read ()
    return msgs

token = 'xoxb-25048547013-hJlRqzBJTW6lhFOrSesERqSU'
sc = SlackClient (token)
if sc.rtm_connect ():
    print "Found the following channels:"
    print repr(sc.server.channels)
    while True:
        msgs = get_messages (sc)
        for msg in msgs:
            print "recv: "+ repr(msg)

        sc.rtm_send_message ('C0R07U3C5', 'I got that')
else:
    print "Connection failed"
