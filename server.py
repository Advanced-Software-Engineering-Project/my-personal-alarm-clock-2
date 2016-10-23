#!flask/bin/python
from flask import Flask, jsonify, request, Response
import redis

# Crossdomain imports
from datetime import timedelta
from flask import make_response, request, current_app
from functools import update_wrapper



r = redis.StrictRedis(host='localhost', port=6379, db=0)

app = Flask(__name__)




# Retrieve a user's alarm time
@app.route('/alarms/<username>', methods=['GET', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type')
def get_alarm(username=None):
    time = r.get(username)
    return jsonify({'time': time})


# Save a user's alarm time
@app.route('/alarms', methods=['POST', 'OPTIONS'])
@crossdomain(origin='*', headers='Content-Type')
def save_alarm():
    data = request.data.split('&')
    username = data[0].split('=')[1]
    time = data[1].split('=')[1]
    r.set(username, time)
    return Response('success')




# Temporary local development solution for CORS
@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
  return response


  
  

if __name__ == '__main__':
    app.run(debug=True)
