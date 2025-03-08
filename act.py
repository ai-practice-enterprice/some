from flask import Flask
import requests


app = Flask(__name__)


# URL port for camera application and robots
HUMAN_DETECTION_URL = "http://localhost:5002"
ROBOT_CONTROL_URL = "http://localhost:5003"

# Receives signal from worker's application
@app.route("/",methods=["GET"])
def home():
    try:
        response = requests.get(HUMAN_DETECTION_URL)
        if response.status_code == 200:
            try :
                requests.post(ROBOT_CONTROL_URL, json={"area": response.text})
                if response.status_code == 200:
                    return({"Human has finished unloading. A robot has been instructed to move to": response.text})
            except requests.exceptions.RequestException as e:
                return ("Could not communicate to the robot.")
        else:
            return ("Camera server is not responding.")
    except requests.exceptions.RequestException as e:
        return ("Human hasn't answered if unloading is done.")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5004, debug=True)
