import instagrapi
from instagrapi.mixins.challenge import ChallengeChoice
import image
import ai
import google_sheets
import mailverify
import dotenv
from os import environ as env

dotenv.load_dotenv('.env')

names, messages = google_sheets.get_new_messages()
if names is None and messages is None:
    print("main: no tasks to run, end script")
    quit()


def custom_challenge_code_handler(username, choice):
    if choice == ChallengeChoice.SMS:
        return None
    elif choice == ChallengeChoice.EMAIL:
        return mailverify.retrieve_gmail_message()
    return False


try:
    cl = instagrapi.Client()
    cl.challenge_code_handler = custom_challenge_code_handler
    cl.login(env["USERNAME"], env["PASSWORD"])
except Exception as e:
    print(f"Exception {e}. Check auth. Terminating program.")
    raise Exception(f"Exception occurred: {e}")
print(f"{__name__}: Login succeeded")


def main_loop():
    for name, message in zip(names,messages):
        if ai.is_content_offensive(message):
            continue
        context = ai.generate_image_context(message)
        content = image.build_image(message, name, context)
        print(f"message: {message}")
        print(f"sender: {name}")
        cl.photo_upload(content,message)


main_loop()