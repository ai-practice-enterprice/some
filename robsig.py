from flask import Flask, request
app = Flask(__name__)



@app.route("/",methods=["POST"])
def home():
    try:
    # Make a GET request to the Flask server
        data = request.get_json()
        print(f"Robot has been sent to area {data['area']}")
    except Exception as e:
        print(f"Robot not sent {e}")
    return ("Yeah! Phase 1 done")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5003, debug=True)