import masterhackerbot
from mastodon import Mastodon

print("Logging in")
mastodon = Mastodon(client_id='pytooter_clientcred.secret')
mastodon.log_in(
    'getyourown@fucking.account',
    'itsnothard22',
    to_file='pytooter_usercred.secret'
)
print("Logged in")

question = masterhackerbot.skidquestion()

print(f"Question: {question}\n\nResponse: {masterhackerbot.generate_jargon(question)}")