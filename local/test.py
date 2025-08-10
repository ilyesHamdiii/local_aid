from dotenv import load_dotenv
load_dotenv()

import os

print(os.getenv('USER'))  # This will print the username from the .env file
print(os.getenv('PASSWORD'))  # This will print the password from the .env file
print(os.getenv('HOST'))      # This will print the host from the .env file
