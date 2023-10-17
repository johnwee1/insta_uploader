import g4f


# from g4f.Provider import Bing


def is_content_offensive(message: str) -> bool:
    """
    Attempts to run content moderation with a given model
    :param message: Message to check
    :return: True if message offensive, False if not offensive or something broke
    """
    with open('prompt.txt', 'r') as f:
        preamble = f.read()

    prompt = preamble + message

    print(f"Prompt: {prompt}")
    try:
        #     response = g4f.ChatCompletion.create(
        #         model = 'gpt-4',
        #         prompt = prompt,
        #         provider=Bing,
        #         messages=[{"role": "user", "content": prompt}],
        #     )

        response = g4f.ChatCompletion.create(
            model=g4f.models.gpt_35_turbo,
            messages=[{"role": "user", "content": prompt}],
        )

        print(response)
        if response[0] == '0':
            return True
    except ValueError:
        print("Requires Authentication")
    except Exception as e:
        print(f"Unknown exception {e} occurred!")
    return False


# def test_function():
#     with open('prompt.txt', 'r') as f:
#         preamble = f.read()
#
#     prompt = preamble + "I like amos because he's handsome."
#     response = g4f.ChatCompletion.create(
#         model=g4f.models.gpt_35_turbo,
#         messages=[{"role": "user", "content": prompt}],
#     )
#
#     print(response)
#     return
#
#
# test_function()
