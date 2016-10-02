#!flask/bin/python
from flask import Flask, jsonify, request
import redis


r = redis.StrictRedis(host='localhost', port=6379, db=0)

app = Flask(__name__)


# Retrieve a user's alarm time
@app.route('/alarms/<username>', methods=['GET'])
def get_alarm(username=None):
    time = r.get('username')
    return jsonify({'time': time})

# Save a user's alarm time
@app.route('/alarms', methods=['POST'])
def save_alarm():
    print(request.data)
    username = request.data['username']
    time = request.data['time']
    r.set(username, time)


if __name__ == '__main__':
    app.run(debug=True)

{hour: int, minute: int}