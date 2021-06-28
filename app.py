from flask import Flask
from routes.setup_routes import setup_routes
app = Flask(__name__)

if __name__ == "__main__":
    setup_routes(app)
    app.run(debug=True)