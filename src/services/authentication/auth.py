import requests
import keyring
import typer
from core.config import settings
from rich.console import Console

SERVICE = "hashenv"
USERNAME = "default"


console = Console()

SERVER_URL = settings.SERVER_URL
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

def logout_redirect():
    token = keyring.get_password(SERVICE, USERNAME)

    if token is None:
        return
    keyring.delete_password(SERVICE, USERNAME)



    