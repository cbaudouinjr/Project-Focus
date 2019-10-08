import firebase_admin
import flask
import requests
import logging
from flask import Flask
from flask import Response
from firebase_admin import db

app = Flask(__name__)

firebase_admin.initialize_app(options={
    'databaseURL': 'https://projectfocus.firebaseio.com'
})

users = db.reference('users')  # reference to sub users document
watson_endpoint = 'https://us-south.ml.cloud.ibm.com/v4/deployments/f0a19534-40b3-4db2-a7ca-dce0a5a68f33/predictions'


@app.route('/snapshot', methods=['POST'])
def create_snapshot():
    request_json = flask.request.json
    submission_data = request_json['submission_data']
    snapshot_data = request_json['snapshot_data']

    try:
        user = submission_data['user']
        watson_payload = list(snapshot_data.values())
        watson_data = get_watson_prediction(watson_payload)
        users.child(user).push(submission_data)  # push payload associated with a timestamp

        return flask.jsonify(watson_data)
    except KeyError as e:
        logging.error("Missing critical key")
        return Response("Missing critical key/value", status=400)


@app.route('/retrieve_snapshots/<user>')
def retrieve_snapshots(user):
    snapshots = verify_user(user)
    if snapshots is not None:
        return flask.jsonify(snapshots)
    else:
        return Response(status=404)


def get_watson_prediction(payload):
    request_params = {"input_data": [{"fields": payload, "values": ["focused"]}]}
    print(request_params)
    return requests.get(watson_endpoint, params=request_params)


def verify_user(user):
    snapshots = users.child(user).get()
    if not snapshots:
        return None
    else:
        return snapshots


if __name__ == '__main__':
    app.run()
