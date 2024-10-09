import os, dotenv
import json
from groq import Groq

dotenv.load_dotenv()
promptfile = "prompt.txt"


def prompt_model(message: str) -> dict:
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

    with open(promptfile, "r") as f:
        preamble = f.read()

    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": preamble},
            {"role": "user", "content": message},
        ],
        response_format={"type": "json_object"},
    )

    print(f"{__name__}: Response: {response}")
    try:
        data = json.loads(response.choices[0].message.content)
    except json.JSONDecodeError:
        data = {"offensive": 1, "reason": "JSON DECODE ERROR", "desc": "Black"}
    return data
