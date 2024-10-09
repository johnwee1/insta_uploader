import ai
import image


def build_image_pipeline(sender_name: str, prompt: str):
    res = ai.prompt_model(sender_name, prompt)
    if res["offensive"] == 1 or len(sender_name.split(" "))>4:
        return None
    else:
        path = image.build_image(prompt, sender_name, res["desc"])
    return path
