from helpers.local_env_parsing_helpers.check_local_env_for_content import check_local_env_for_content
from helpers.env_recieve import env_recieve

def local_env_parsing_and_write_service(env_data: dict):
    local_env_has_content = check_local_env_for_content()
    if local_env_has_content:
        print("Local .env file has content, do you wish to overwrite this content? (y/n)")
        choice = input().lower()
        if choice == 'y':
            print("Overwriting local .env file with environment variables from backend...")
            env_recieve(env_data=env_data)
            print("local .env file has been updated with environment variables from backend.")
        else:
            print("Keeping existing local .env file content. No changes made.")
    else:
        print("Local .env file is empty, writing environment variables from backend.. ")
        env_recieve(env_data=env_data)



