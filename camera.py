from flask import Flask
import random

app = Flask(__name__)


offloadarea = ['A-inbound ', 'B-inbound ', 'C-inbound ', 'D-inbound ', 'E-inbound ', 'F-inbound ']

@app.route('/')
def random_value():
    # Return a random value from the list
    return random.choice(offloadarea)

if __name__ == '__main__':
    # Run the app on port 5002
    app.run(host='0.0.0.0',port=5002,debug=True)