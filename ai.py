import g4f
from g4f.Provider import Bing


def is_content_offensive(message: str) -> bool:
    with open('prompt.txt', 'r') as f:
        preamble = f.read()

    prompt = preamble + message

    print(f"Prompt: {prompt}")
    try:
        response = g4f.ChatCompletion.create(
            model = 'gpt-4',
            prompt = prompt,
            provider=Bing,
            messages=[{"role": "user", "content": prompt}],
        )
        print(response)
        if (response[0] == '0'):
            return True
    except ValueError:
        print("Requires Authentication")
    except Exception as e:
        print(f"Unknown exception {e} occurred!")
    return False



