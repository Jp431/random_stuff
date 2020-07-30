import os
import praw
from datetime import datetime

start_time = datetime.now()

USER = "r00"
PWD = "your_password"
FILE_NAME = f"{USER}'s subreddit"
CLIENT_ID = "your_reddit_client_id"
CLIENT_SECRET = "your_secret_key"


print('Fetching your data')
reddit = praw.Reddit(client_id=f'{CLIENT_ID}',
                     client_secret=f'{CLIENT_SECRET}',
                     password=f'{PWD}',
                     user_agent=f'testscript by /u/{USER}',
                     username=f'{USER}').user.subreddits(limit=5000)

subreddit_list = []
subscribed_count = 0
for subreddit in reddit:
    subreddit_list.append(subreddit.display_name)
    subscribed_count += 1

f = open(f"{FILE_NAME}.txt", "w+")
f.write(f"""You are subscribed to {subscribed_count} subreddits\n
Here is the list\n""")

for subreddit in sorted(subreddit_list):
    f.write(f"{subreddit}\n")
end_time = datetime.now() - start_time

f.close()
print(f"Time to fetch your data {end_time}")
os.startfile(f"{FILE_NAME}.txt")
