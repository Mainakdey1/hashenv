import typer


from helpers.get_repo_list import get_repo_list
from helpers.env_recieve import env_recieve

app = typer.Typer()



@app.command()
def login(token: str):
    with open(".env", "w") as f:
        f.write(token)
    print('Logged in!')

@app.command()
def hello():
    print('Hello, this cli tool is working!')

@app.command()
def ping():
    print('status: working!')


@app.command()
def show_repository(all: bool = typer.Option(False, "--all")):
    if all:
        res = get_repo_list()
        print(res)
    else:
        print('Nothing passed as parameter, returning nothing')

@app.command()
def install():
    env_recieve("org-unique")

if __name__ == "__main__":
    app()

