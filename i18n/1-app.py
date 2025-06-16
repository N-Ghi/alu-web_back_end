from flask import Flask, request
from flask_babel import Babel


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Instantiate Flask app
app = Flask(__name__)

# Apply configuration from the Config class
app.config.from_object(Config)

# Instantiate Babel and bind it to the app
babel = Babel(app)

# Optional: Define a function to select locale dynamically based on request headers
@babel.localeselector
def get_locale():
    # Return best match from the client request
    return request.accept_languages.best_match(app.config['LANGUAGES'])


