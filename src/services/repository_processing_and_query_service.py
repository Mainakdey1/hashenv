from helpers.get_repo_details_from_git import get_repo_details_from_git
from helpers.get_env_from_backend import get_env_from_backend
from helpers.env_recieve import env_recieve
from helpers.push_env_to_backend import push_env_to_backend
from helpers.environment_processors.get_env_variables_from_local import get_env_variables_from_local
from helpers.environment_processors.ping_db_for_repository_check import ping_db_for_repository_check
from services.env_parsing_service import env_parsing_service

#This service handles the processing of git environment, processing current repository details and querying the backend for 
#for details about current repository. If it doesn't find details, it will ask the user to create a new 
#new .env file and the cli will provide the option to add the current repository to the db

def process_repository_service():
    DATABASE_KEY = get_repo_details_from_git()
    if DATABASE_KEY is not None:
        repository_exists = ping_db_for_repository_check(DATABASE_KEY)
        if repository_exists:
            print('Repository found in backend, receiving environment variables...')
            env_data = get_env_from_backend(DATABASE_KEY)
            env_parsing_service(get_env_variables_from_local(), env_data)

            

        else:
            print('This repository is not registered in the backend.')
            print('Would you like to add it? (y/n)')
            choice = input().lower()
            if choice == 'y':
                local_env_data = get_env_variables_from_local()
                push_env_to_backend(repository=DATABASE_KEY, payload=local_env_data)

            




        

