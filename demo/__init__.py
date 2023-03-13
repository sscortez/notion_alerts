from os import environ
from flask import Flask
from pyngrok import ngrok

def init_webhooks(base_url):
    # Update inbound traffic via APIs to use the public-facing ngrok URL
    pass

def create_app():
    app = Flask(__name__)
    
    app.config.from_pyfile('settings.py')

    app.config.from_mapping(
        BASE_URL="http://localhost:5000",
        USE_NGROK=environ.get("USE_NGROK", "False") == "True" and environ.get(
            "WERKZEUG_RUN_MAIN") != "true"
    )

    if (environ.get("FLASK_DEBUG") == '1') and app.config["USE_NGROK"]:
        from os import sys
        
        # Get the dev server port (defaults to 5000 for Flask, can be overridden with `--port`
        # when starting the server
        port = sys.argv[sys.argv.index("--port") + 1] if "--port" in sys.argv else 5000

        # Open a ngrok tunnel to the dev server
        public_url = ngrok.connect(port).public_url
        print(" * ngrok tunnel \"{}\" -> \"http://127.0.0.1:{}\"".format(public_url, port))

        # Update any base URLs or webhooks to use the public ngrok URL
        app.config["BASE_URL"] = public_url
        init_webhooks(public_url)
        
        # Prevent calling ngrok again
        app.config["USE_NGROK"] = "False"

    @app.route('/')
    def index():
        return f"This is an API KEY: { app.config.get('API_KEY') }"

    return app
