import os

def repo_searcher():
    repos = []

    for root, dirs, files in os.walk("/Users/chestor"):
        if ".git" in dirs:
            repos.append(root)
            dirs.remove(".git")
    return repos
        
