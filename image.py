import os
from os import environ as env
import requests
from PIL import Image, ImageDraw, ImageFont
import textwrap
import json
from types import SimpleNamespace

FONT_SIZE = 50
OPACITY = 0.5
RECT_RAD = 50
img_path = "image_temp.jpg"


def retrieve_context_img(query: str) -> os.path:
    json.loads(env["SHEETS_JSON"])
    headers = {
        "Authorization": env["PEXELS_API_KEY"]
    }
    size = "small"
    locale = "en-US"
    per_page = "1"
    url = f"https://api.pexels.com/v1/search?query={query}&size={size}&locale={locale}&per_page={per_page}"
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(__name__ + "Request failed with status code:", response.status_code)
        # Fallback to random image
        return retrieve_image()
    data = json.loads(response.text, object_hook=lambda x: SimpleNamespace(**x))
    img = requests.get(data.photos[0].src.landscape, stream=True)
    if img.status_code == 200:
        with open(img_path, 'wb') as f:
            for chunk in img.iter_content(chunk_size=8192):
                f.write(chunk)
    else:
        return retrieve_image()
    assert img_path in os.listdir(os.getcwd())
    return img_path

def retrieve_image() -> os.path:
    """
    Retrieves the image either from online, or a generated color matrix.
    :return:
    """
    img_width = 1000
    img_height = 1000
    img_url = f"https://random.imagecdn.app/{img_width}/{img_height}"  # some api i found online

    response = requests.get(img_url, stream=True)

    if response.status_code == 200:
        # Save the image to a file
        with open(img_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
    else:
        # handle api failure by manually creating image
        print(__name__)
        print(': Failed to get image:', response.status_code)
        Image.new('RGB', (img_width, img_height)).save(img_path)

    assert img_path in os.listdir(os.getcwd())
    return img_path


def build_image(text_content: str, sender_name: str, context: str) -> os.path:
    """
    Put text onto the image, and then make a new image in the directory.
    Delete image_path after done.
    :param text_content: returned from get_message()
    :param sender_name: returned from get_message()
    :return: path of the new image with the text.
    """
    image_path = retrieve_context_img(context) # can switch with retrieve_image() if you want

    text_content = textwrap.fill(text_content, width=38)
    text_content = f"{text_content}\n- {sender_name}"
    img = Image.open(image_path).convert("RGBA")
    font = ImageFont.truetype(os.path.join(os.getcwd(), "roboto.ttf"), size=FONT_SIZE)
    draw = ImageDraw.Draw(img)
    text_anchor = (img.size[0] / 2, img.size[1] / 2)

    def center_box(anchor: tuple[float,float]) -> tuple[float,float]:
        """
        vertically centers the image based on multiline box
        :return:
        """
        box = draw.multiline_textbbox(
            anchor,
            text_content,
            font,
            "ms"
        )
        print(box)
        x1, y1, x2, y2 = box[0], box[1], box[2], box[3]
        y_avg = y1*0.5 + y2*0.5
        print(f"y avg: {y_avg}")
        y_offset = y_avg - anchor[1]

        return (anchor[0], anchor[1]-y_offset)

    text_anchor = center_box(text_anchor)


    x1,y1,x2,y2 = draw.multiline_textbbox(
        (text_anchor[0], text_anchor[1]),
        text_content,
        font,
        "ms"
    )

    x1-=RECT_RAD
    y1-=RECT_RAD
    x2+=RECT_RAD
    y2+=RECT_RAD

    black_color = (0,0,0,int(OPACITY*256))

    blank = Image.new('RGBA', img.size, (0,0,0,0))
    draw_blank = ImageDraw.Draw(blank)
    draw_blank.rounded_rectangle((x1,y1,x2,y2), fill=black_color, radius=RECT_RAD/4)

    img = Image.alpha_composite(img, blank).convert("RGB")
    # Save the modified image
    draw = ImageDraw.Draw(img)
    draw.multiline_text(
        (text_anchor[0], text_anchor[1]),
        text_content,
        font=font,
        anchor="ms",
    )
    modified_path = 'modified_image.jpg'
    img.save(modified_path)

    return modified_path
