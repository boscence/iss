from flask import Flask
from .src import get_iss_location, get_location_data
import sys
import json

sys.path.append(r'src/')


app = Flask(__name__)


@app.route("/")
def main():
    iss_location = get_iss_location.get_iss_location()
    iss_location['location'] = get_location_data.get_location_data(iss_location['iss_position']['latitude'], 
                                                                       iss_location['iss_position']['longitude'])

    #iss_location['location'] = get_location_data.get_location_data(31.503104, 
    #                                                              121.930806)                           
    return json.dumps(iss_location)


if __name__ == "__main__":
    app.run(debug=True)
