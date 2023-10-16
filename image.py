import os
import requests
from PIL import Image, ImageDraw, ImageFont
import textwrap


def retrieve_image() -> os.path:
    """
    Retrieves the image either from online, or a generated color matrix.
    :return:
    """
    img_width = 1000
    img_height = 1000
    img_url = f"https://random.imagecdn.app/{img_width}/{img_height}"  # some api i found online
    img_path = 'image_temp.jpg'

    response = requests.get(img_url, stream=True)

    if response.status_code == 200:
        # Save the image to a file
        with open(img_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
    else:
        # handle api failure by manually creating image
        print('Failed to get image:', response.status_code)
        Image.new('RGB', (img_width, img_height)).save(img_path)

    assert img_path in os.listdir(os.getcwd())
    return img_path


def build_image(image_path: os.path, text_content: str, sender_name: str) -> os.path:
    """
    Put text onto the image, and then make a new image in the directory.
    Delete image_path after done.
    :param image_path: path of image
    :param text_content: returned from get_message()
    :param sender_name: returned from get_message()
    :return: path of the new image with the text.
    """
    text_content = textwrap.fill(text_content, width=38)
    text_content = f"{text_content}\n-{sender_name}"
    img = Image.open(image_path)
    font = ImageFont.truetype(os.path.join(os.getcwd(), "roboto.ttf"), size=45)
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

    box = draw.multiline_textbbox(
        (text_anchor[0], text_anchor[1]),
        text_content,
        font,
        "ms"
    )

    text_anchor = center_box(text_anchor)

    draw.multiline_text(
        (text_anchor[0], text_anchor[1]),
        text_content,
        font=font,
        anchor="ms",
    )

    box = draw.multiline_textbbox(
        (text_anchor[0], text_anchor[1]),
        text_content,
        font,
        "ms"
    )

    # Save the modified image
    modified_path = 'modified_image.jpg'
    img.save(modified_path)

    return modified_path
