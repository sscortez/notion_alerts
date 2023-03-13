from os import environ

if environ.get("FLASK_DEBUG") == '1':
  import environments.development
else:
  import environments.production

SECRET_KEY = environ.get("SECRET_KEY")
API_KEY = environ.get("API_KEY")
INTERNAL_INTEGRATION_TOKEN = environ.get("INTERNAL_INTEGRATION_TOKEN")
