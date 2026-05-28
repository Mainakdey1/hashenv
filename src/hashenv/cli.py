import typer

from helpers.get_repo_list import get_repo_list
from helpers.env_recieve import env_recieve
from helpers.ping_backend_server import ping_backend_server
from helpers.get_env_from_backend import get_env_from_backend
app = typer.Typer()



@app.command()
def login(token: str):
    with open(".env", "w") as f:
        f.write(token)
    print('Logged in!')

@app.command()
def ping():
    print('status: working!')


@app.command()
def show_repository(all: bool = typer.Option(False, "--all"), r: bool = typer.Option(False, "--r")):
    if all:
        res = get_repo_list()
        print(res)
    elif r:
        print('Showing repository for --r flag')
    else:
        print('Nothing passed as parameter, returning nothing')

@app.command()
def install(r: bool = typer.Option(False, "--r")):
    if r:
        print('do something here')
    else:
        env_recieve("org-unique")


#test commands can and will usually go here
@app.command()
def ping_server():
    ping_backend_server()
    env_data = get_env_from_backend('backend-api')
    print(env_data)



if __name__ == "__main__":
    app()

