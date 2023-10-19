from os import environ as env
import dotenv
import pytest

def check_environment_variable(variable_name):
    if variable_name in env:
        return True
    return False


@pytest.mark.parametrize("secret", ["USERNAME", "PASSWORD", "PEXELS_API_KEY", "SHEETS_JSON", "GMAIL_JSON"])
def test_loaded_secrets(secret):
    dotenv.load_dotenv('../.env')
    assert check_environment_variable(secret), f"{secret} is not loaded as an environment variable!"