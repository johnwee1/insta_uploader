import g4f


# from g4f.Provider import Bing


def is_content_offensive(message: str) -> bool:
    """
    Attempts to run content moderation with a given model
    :param message: Message to check
    :return: True if message offensive, False if not offensive or something broke
    """
    try:
        response = _prompt_model("filterprompt.txt", message)
        if response[0] == '0':
            return True
    except ValueError:
        print("Requires Authentication")
    except Exception as e:
        print(f"Unknown exception {e} occurred!")
    return False


def generate_image_context(message: str) -> str | bool:
    try:
        response = _prompt_model("contentprompt.txt", message)
        return response
    except ValueError:
        print("Requires Authentication")
    except Exception as e:
        print(f"Unknown exception {e} occurred!")
    return False


def _prompt_model(preamble_filepath, message):
    with open(preamble_filepath, 'r') as f:
        preamble = f.read()
    prompt = preamble + message
    print(f"{__name__}: Prompt: {prompt}")
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_35_turbo,
        messages=[{"role": "user", "content": prompt}],
    )
    return response
