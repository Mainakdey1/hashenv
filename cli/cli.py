import typer
import requests
import os


app = typer.Typer()

BASE_URL = "http://localhost:8000"

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

if __name__ == "__main__":
    app()

