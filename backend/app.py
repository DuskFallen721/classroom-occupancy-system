import os
from flask import Flask
from routes import main

basedir = os.path.abspath(os.path.dirname(__file__))
frontend_dir = os.path.abspath(os.path.join(basedir, '..', 'frontend'))

app = Flask(__name__, static_folder=frontend_dir, static_url_path='')
app.register_blueprint(main)

# Application entry point
if __name__ == "__main__":
    app.run(debug=True)
