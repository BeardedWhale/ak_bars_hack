import os
from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.config['CORS_HEADERS'] = 'Content-Type'

    from . import loan_estimator
    app.register_blueprint(loan_estimator.bp)
    CORS(app) 
        # allow_headers=["Content-Type", "Authorization", "Access-Control-Allow-Credentials"],
        # supports_credentials=True)
    # app.config.from_mapping(
    #     SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev_key'
    # )

    return app