import json, requests
import random
import time
import os.path

token = ""
userID = ""

url = f'https://api.telegram.org/bot{token}/sendPhoto'

data = {'chat_id': userID,
        'caption': "Look master!"}

messages = ["Look master!", "LOL master hahahaha", "KKKKKKKKKKKKKKKK", "Look this shit LOL", ":D"]

with open("database.json", "r") as read_file:
    database = json.load(read_file)

for x in database:
    if database[x]["send"] == False:

        completeName = os.path.join("files/", x) 

        requests.post(url, {'chat_id': userID,
         "caption": messages[random.randint(0, len(messages) - 1)]}
        , files={'photo': open(completeName, 'rb')})
        
        database[x]["send"] = True

        with open("database.json", "w") as write_file:
                json.dump(database, write_file)

        time.sleep(120)
