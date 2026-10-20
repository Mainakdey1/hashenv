import requests
import keyring
import typer
from core.config import settings
from rich.console import Console

from ..authentication.qr_code import get_device_id

SERVICE = "hashenv"
USERNAME = "default"


console = Console()

SERVER_URL = settings.SERVER_URL
LOCAL_SERVER_URL = settings.LOCAL_SERVER_URL
def log_in(token : int):   
    try: 
        response = requests.post(f"{SERVER_URL}/auth", json={"token": token})
        if response.status_code == 200:
            keyring.set_password(SERVICE, USERNAME, token)
            console.print("[green]Logged in successfully!")
            return response.json()
        else:
            logout_redirect()
            console.print("[red]Not authorized, wrong token passed")
    except requests.exceptions.RequestException as e:
        print(f'Error connecting to server: {e}')

def get_token() -> str:
    token = keyring.get_password(SERVICE, USERNAME)

    if token is None:
        typer.echo(
            "Not logged in. Run `hashenv login`"
        )
        raise typer.Exit(1)

    return token

def authenticated() -> bool:
    token = keyring.get_password(SERVICE, USERNAME)

    if token is None:
        console.print("[red]Not logged in, run `hashenv login`")
        return False
    return True

def mobile_authenticated() -> bool:
    device_token_id = get_device_id()
    try: 
        response = requests.get(f"{SERVER_URL}/device/isregistered/{device_token_id}")
        if response.status_code == 200:
            return True
        else:
            console.print("[red]Authorization expired!")
            return False
    except requests.exceptions.RequestException as e:
        print(f'Error connecting to server: {e}')
    return

def logout_redirect():
    token = keyring.get_password(SERVICE, USERNAME)

    if token is None:
        return
    keyring.delete_password(SERVICE, USERNAME)



    