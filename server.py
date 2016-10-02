#!flask/bin/python
from flask import Flask, jsonify, request, Response
import redis


r = redis.StrictRedis(host='localhost', port=6379, db=0)

app = Flask(__name__)


# Retrieve a user's alarm time
@app.route('/alarms/<username>', methods=['GET'])
def get_alarm(username=None):
    time = r.get(username)
    return jsonify({'time': time})

# Save a user's alarm time
@app.route('/alarms', methods=['POST'])
def save_alarm():
    data = request.data.split('&')
    username = data[0].split('=')[1]
    time = data[1].split('=')[1]
    r.set(username, time)
    return Response('success')


if __name__ == '__main__':
    app.run(debug=True)

