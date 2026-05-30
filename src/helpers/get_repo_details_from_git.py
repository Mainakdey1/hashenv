import subprocess


def get_repo_details_from_git():
    try:
        url = subprocess.check_output(
            ["git", "remote", "get-url", "origin"],
            text=True
        ).strip()
        DATABASE_KEY = url.split("/")[-1].replace(".git", "")
        return DATABASE_KEY
    except subprocess.CalledProcessError:
        print('This repository is not connected to a remote origin. Please connect it to a ' \
            'remote repository and try again.')
        return None