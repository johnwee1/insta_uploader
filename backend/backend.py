import ai
import image
import dotenv, os


def build_image_pipeline(sender_name, prompt: str):
    res = ai.prompt_model(prompt)
    if res["offensive"] == 1:
        return None
    else:
        path = image.build_image(prompt, sender_name, res["desc"])
    return path
