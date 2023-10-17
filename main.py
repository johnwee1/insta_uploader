import json
import instagrapi
from collections import namedtuple
import image
import ai
import google_sheets


with open('env.json', 'r') as f:
    _env = json.load(f)
Env = namedtuple('Env', _env.keys())
env = Env(**_env)

try:
    cl = instagrapi.Client()
    cl.login(env.USERNAME, env.PASSWORD)
except Exception as e:
    print(f"Exception {e}. Check auth. Terminating program.")
    quit()


def main_loop():
    names, messages = google_sheets.get_new_messages()
    for name, message in zip(names,messages):
        if ai.is_content_offensive(message):
            continue
        content = image.build_image(message, name)
        print(f"message: {message}")
        print(f"sender: {name}")
        cl.photo_upload(content,message)


main_loop()