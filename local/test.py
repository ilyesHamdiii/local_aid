from dotenv import load_dotenv
load_dotenv()

import os

print(os.getenv('username'))  # This will print the username from the .env file
print(os.getenv('password'))  # This will print the password from the .env file
print(os.getenv('host'))      # This will print the host from the .env file
