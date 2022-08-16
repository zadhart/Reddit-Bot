import praw
import json
import datetime
import time
import requests
import random
import os.path

reddit = praw.Reddit(
    client_id="",
    client_secret="",
    user_agent="",
    password="",
    username="",
)

save_path = "files/"

reddit.read_only = True

print(reddit.read_only)

target = ["Animemes", "eu_nvr", "4chan", "goodanimemes", "anime_irl", "porramauricio", "animecirclejerk"]

dados = {}

while True:

    with open("database.json", "rb") as read_file:
        dados = json.load(read_file)

    for post in reddit.subreddit(target[random.randint(0, len(target) - 1)]).hot(limit=10):
        url = (post.url)

        if(url[-1] == 'g'):
        #print(url)

            r = requests.get(url)
            file_name = url.split("/")

        #print(file_name)

            completeName = os.path.join(save_path, file_name[-1])   

            with open(completeName,"wb") as f:
        
                f.write(r.content)

            f.close()

            dados[file_name[-1]] = {"send": False, "data": str(datetime.datetime.now()), "tag": "meme"}

        
            print(dados)

            with open("database.json", "w") as write_file:
                json.dump(dados, write_file)

    time.sleep(10000)
    
