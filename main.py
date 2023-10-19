import instagrapi
import image
import ai
import google_sheets
import mailverify
import dotenv
from os import environ as env

dotenv.load_dotenv('.env')

try:
    cl = instagrapi.Client()
    cl.login(env["USERNAME"], env["PASSWORD"], verification_code=mailverify.retrieve_gmail_message())
except Exception as e:
    print(f"Exception {e}. Check auth. Terminating program.")
    quit()


def main_loop():
    names, messages = google_sheets.get_new_messages()
    for name, message in zip(names,messages):
        if ai.is_content_offensive(message):
            continue
        context = ai.generate_image_context(message)
        content = image.build_image(message, name, context)
        print(f"message: {message}")
        print(f"sender: {name}")
        cl.photo_upload(content,message)


main_loop()