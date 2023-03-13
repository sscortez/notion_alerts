from os import path
from dotenv import load_dotenv

if path.exists(".env.development.local"):
    load_dotenv(".env.development.local")
else:
    load_dotenv(".env.development")
