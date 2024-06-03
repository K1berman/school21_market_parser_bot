import os
from dotenv import load_dotenv
import json


load_dotenv()

URL = os.getenv("URL")
COOKIES = json.loads(os.getenv("COOKIES"))
TOKEN = os.getenv("TOKEN")