import os
from dotenv import load_dotenv
import json


load_dotenv()

if (URL := os.getenv("URL")) is None: print("URL - Not Found!")
# COOKIES = json.loads(data_cookies) if (data_cookies := os.getenv("COOKIES")) is not None else print("COOKIES - Not Found!")
if (TOKEN := os.getenv("TOKEN")) is None: print("TOKEN - Not Found!")
if (HEADER := os.getenv("HEADER")) is None: print("TOKEN - Not Found!")
