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

filename = "processed_mentions.txt"
while True:
    with open(filename, "a+") as f:
        f.seek(0)
        processed_ids = set(line.strip() for line in f.readlines())

        mentions = mastodon.notifications()
        for mention in mentions:
            if mention['type'] == 'mention' and mention['id'] not in processed_ids and mention['account']['username'] != 'masterhackerbot':
                try:
                    in_reply_to_id = mention['in_reply_to_id']
                except KeyError:
                    in_reply_to_id = None
                if in_reply_to_id:
                    ipost = mastodon.status(in_reply_to_id)
                else:
                    ipost = mention
                status_id = mention["status"]["id"]
                ipost_text = striphtml(ipost['status']['content'])
                mastodon.status_post(masterhackerbot.generate_jargon(ipost_text), in_reply_to_id=status_id)
                print("Posted")
                f.write(f"{mention['id']}\n")
            mastodon.notifications_dismiss(mention['id'])
        print("Round complete")
        time.sleep(60)
