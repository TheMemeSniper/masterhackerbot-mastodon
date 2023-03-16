import masterhackerbot
from mastodon import Mastodon
import re
import time

def striphtml(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)

print("Logging in")
mastodon = Mastodon(client_id='pytooter_clientcred.secret')
mastodon.log_in(
    'getyourown@fucking.account',
    'itsnothard22',
    to_file='pytooter_usercred.secret'
)
print("Logged in")


mastodon.status_post(masterhackerbot.generate_jargon(masterhackerbot.skidquestion()))
print("Posted")