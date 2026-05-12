from .repo_searcher import repo_searcher


def get_repo_list():
    repo_list = repo_searcher()
    return repo_list


