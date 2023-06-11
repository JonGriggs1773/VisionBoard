from flask_app import app
#! Import controllers as needed
from flask_app.controllers import users

if __name__ == "__main__":
    app.run(debug = True)