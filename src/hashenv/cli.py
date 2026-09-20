import typer

from services.repository_processing_and_query_service import process_repository_service
from helpers.get_repo_list import get_repo_list
from helpers.env_recieve import env_recieve
from helpers.ping_backend_server import ping_backend_server
from helpers.get_env_from_backend import get_env_from_backend
from rich.spinner import Spinner
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command(help="Login with your token.")
def login():
    console.print("[bold blue]Feature still in development. Coming soon!!")
    # with open(".env", "w") as f:
    #     f.write(token)
    # print('Logged in!')

@app.command(help="Ping server health.")
def ping():
    ping_backend_server()

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
    if r:
        try:
            process_repository_service()
        except Exception.__traceback__ as e:
            print(f"An error occurred: {e}")
    else:
        env_recieve("org-unique")


#test commands can and will usually go here
# @app.command()
# def ping_server():
#     ping_backend_server()




if __name__ == "__main__":
    app()

