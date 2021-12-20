import os 
from dotenv import load_dotenv

load_dotenv()
 
def hello(): 
    username = os.getenv("username") if os.getenv("username") else "Default"
    return f"hello {username}"