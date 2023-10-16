# the main script needs to instantiate the Selenium webdriver
import json
import instagrapi
from collections import namedtuple
import image
import google_sheets as gs


with open('env.json', 'r') as f:
    _env = json.load(f)
Env = namedtuple('Env', _env.keys())
env = Env(**_env)

confession = "oh yeah yeah. test etst tewst eteitehwtiewhou thweoit hwoi t ge4 gee"
sender = "-pseudonym"
img_path = image.build_image(image.retrieve_image(), confession, sender)



# cl = instagrapi.Client()
# cl.login(env.USERNAME, env.PASSWORD)
#
# cl.photo_upload(image_path,"test upload!")