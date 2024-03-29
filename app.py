from flask import Flask
from .src import get_iss_location
import sys

sys.path.append(r'src/')


app = Flask(__name__)


@app.route("/")
def main():
    iss_location = get_iss_location.get_iss_location()
    return iss_location


if __name__ == "__main__":
    app.run()
