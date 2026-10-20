import typer
import uuid
from rich.spinner import Spinner
from rich.console import Console
from importlib.metadata import version, PackageNotFoundError


from services.repository_processing_and_query_service import process_repository_service
from helpers.get_repo_list import get_repo_list
from services.authentication.auth import log_in, get_token, authenticated, mobile_authenticated
from helpers.env_recieve import env_recieve
from helpers.ping_backend_server import ping_backend_server
from helpers.get_env_from_backend import get_env_from_backend
from services.authentication.qr_code import display_qr_code, get_device_id


app = typer.Typer()
console = Console()


@app.command(help="Login using QR Code")
def pair():
    device_token_id = get_device_id()

    console.status("[bold green] Scan this QR code with your mobile app")
    display_qr_code(device_token_id=device_token_id)

    # will add a check if device code is registered in devicetoken id tables, if not then
    # reject requests


@app.command(help="Login with your token.")
def login():
    token = str(input("Enter your API token: "))
    log_in(token=token)
    # console.print("[bold blue]Feature still in development. Coming soon!!")
    # with open(".env", "w") as f:
    #     f.write(token)
    # print('Logged in!')

@app.command(help="Ping server health.")
def ping():
    res = authenticated() or mobile_authenticated()
    if res:
        ping_backend_server()
    else:
        console.print("[red]Not logged in, run `hashenv login or hashenv pair`")

def version_callback(value: bool):
    if value:
        try:
            current_version = version("hashenv")
        except PackageNotFoundError:
            current_version = "unknown"

        print(f"Hashenv CLI version: {current_version}")
        raise typer.Exit()

@app.callback()
def main(
    version_flag: bool = typer.Option(
        False,
        "--version",
        callback=version_callback,
        is_eager=True,
        help="Show the installed CLI version."
    )
):
    pass
@app.command(help="Display all your repositories.")
def show_repository(all: bool = typer.Option(False, "--all"), r: bool = typer.Option(False, "--r")):
    if all:
        with console.status(status="[bold green]Loading..."):
            res = get_repo_list()
            print(res)
    elif r:
        print('Showing repository for --r flag')
    else:
        print('Nothing passed as parameter, returning nothing')

@app.command(help="Install env files for your repository.")
def install(r: bool = typer.Option(False, "--r")):
    res = authenticated() or mobile_authenticated()
    if res:
        if r:
            try:
                process_repository_service()
            except Exception.__traceback__ as e:
                print(f"An error occurred: {e}")
        else:
            console.log('No arguments passed, returning nothing!')


#test commands can and will usually go here
# @app.command()
# def ping_server():
#     ping_backend_server()




if __name__ == "__main__":
    app()

