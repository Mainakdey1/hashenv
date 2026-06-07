from typing import Dict
from services.local_environment_parsing_and_write_service import local_env_parsing_and_write_service


def env_parsing_service(local_env_data: Dict[str, str], recieved_env_data: Dict[str, str]):
    differ = False
    for key, value in recieved_env_data.items():
        if key not in local_env_data or local_env_data[key] != value:
            differ = True

    if differ:
        print('The environment variables in the backend differ from you local .env file.')
        print('Would you like to update your local .env file with the backend environment variables? (y/n)')
        choice = input().lower()
        if choice == 'y':
            local_env_parsing_and_write_service(env_data=recieved_env_data)
        else:
            print('Keeping local .env file unchanged.')
    else:
        print('The environment variables in the backend are the same as your local .env file. No changes needed.')
                                                