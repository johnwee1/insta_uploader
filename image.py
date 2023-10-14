import os


def retrieve_image() -> os.path:
    """
    Retrieves the image either from online, or a generated color matrix.
    :return:
    """
    path = os.getcwd()
    return path


def build_image(image_path: os.path, content: tuple[str, str]) -> os.path:
    """
    Put text onto the image, and then make a new image in the directory.
    Delete image_path after done.
    :param image_path: path of image
    :param content: returned from get_message()
    :return: path of the new image with the text.
    """
    text_image_path = os.getcwd()
    return text_image_path
