from flask import Flask
from flask_ngrok import run_with_ngrok

def create_app():
    app = Flask(__name__)
    run_with_ngrok(app)
    
    app.config.from_pyfile('settings.py')
    
    @app.route('/')
    def index():
        return f"This is an API KEY: { app.config.get('API_KEY') }"

    return app
