import firebase_admin
import flask
import requests
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
    try:
        time_stamp = request_json['timestamp']
        user = request_json['user']  # user to associate snapshot with
        delta_absolute_1 = request_json['delta_absolute_1']
        delta_absolute_2 = request_json['delta_absolute_2']
        delta_absolute_3 = request_json['delta_absolute_3']
        delta_absolute_4 = request_json['delta_absolute_4']
        theta_absolute_1 = request_json['theta_absolute_1']
        theta_absolute_2 = request_json['theta_absolute_2']
        theta_absolute_3 = request_json['theta_absolute_3']
        theta_absolute_4 = request_json['theta_absolute_4']
        alpha_absolute_1 = request_json['alpha_absolute_1']
        alpha_absolute_2 = request_json['alpha_absolute_2']
        alpha_absolute_3 = request_json['alpha_absolute_3']
        alpha_absolute_4 = request_json['alpha_absolute_4']
        beta_absolute_1 = request_json['beta_absolute_1']
        beta_absolute_2 = request_json['beta_absolute_2']
        beta_absolute_3 = request_json['beta_absolute_3']
        beta_absolute_4 = request_json['beta_absolute_4']
        gamma_absolute_1 = request_json['gamma_absolute_1']
        gamma_absolute_2 = request_json['gamma_absolute_2']
        gamma_absolute_3 = request_json['gamma_absolute_3']
        gamma_absolute_4 = request_json['gamma_absolute_4']
        delta_relative_1 = request_json['delta_relative_1']
        delta_relative_2 = request_json['delta_relative_2']
        delta_relative_3 = request_json['delta_relative_3']
        delta_relative_4 = request_json['delta_relative_4']
        theta_relative_1 = request_json['theta_relative_1']
        theta_relative_2 = request_json['theta_relative_2']
        theta_relative_3 = request_json['theta_relative_3']
        theta_relative_4 = request_json['theta_relative_4']
        alpha_relative_1 = request_json['alpha_relative_1']
        alpha_relative_2 = request_json['alpha_relative_2']
        alpha_relative_3 = request_json['alpha_relative_3']
        alpha_relative_4 = request_json['alpha_relative_4']
        beta_relative_1 = request_json['beta_relative_1']
        beta_relative_2 = request_json['beta_relative_2']
        beta_relative_3 = request_json['beta_relative_3']
        beta_relative_4 = request_json['beta_relative_4']
        gamma_relative_1 = request_json['gamma_relative_1']
        gamma_relative_2 = request_json['gamma_relative_2']
        gamma_relative_3 = request_json['gamma_relative_3']
        gamma_relative_4 = request_json['gamma_relative_4']
        delta_session_score_1 = request_json['delta_session_score_1']
        delta_session_score_2 = request_json['delta_session_score_2']
        delta_session_score_3 = request_json['delta_session_score_3']
        delta_session_score_4 = request_json['delta_session_score_4']
        theta_session_score_1 = request_json['theta_session_score_1']
        theta_session_score_2 = request_json['theta_session_score_2']
        theta_session_score_3 = request_json['theta_session_score_3']
        theta_session_score_4 = request_json['theta_session_score_4']
        alpha_session_score_1 = request_json['alpha_session_score_1']
        alpha_session_score_2 = request_json['alpha_session_score_2']
        alpha_session_score_3 = request_json['alpha_session_score_3']
        alpha_session_score_4 = request_json['alpha_session_score_4']
        beta_session_score_1 = request_json['beta_session_score_1']
        beta_session_score_2 = request_json['beta_session_score_2']
        beta_session_score_3 = request_json['beta_session_score_3']
        beta_session_score_4 = request_json['beta_session_score_4']
        gamma_session_score_1 = request_json['gamma_session_score_1']
        gamma_session_score_2 = request_json['gamma_session_score_2']
        gamma_session_score_3 = request_json['gamma_session_score_3']
        gamma_session_score_4 = request_json['gamma_session_score_4']

        db_payload = {"timestamps": time_stamp,
                      "delta_absolute_1": delta_absolute_1,
                      "delta_absolute_2": delta_absolute_2,
                      "delta_absolute_3": delta_absolute_3,
                      "delta_absolute_4": delta_absolute_4,
                      "theta_absolute_1": theta_absolute_1,
                      "theta_absolute_2": theta_absolute_2,
                      "theta_absolute_3": theta_absolute_3,
                      "theta_absolute_4": theta_absolute_4,
                      "alpha_absolute_1": alpha_absolute_1,
                      "alpha_absolute_2": alpha_absolute_2,
                      "alpha_absolute_3": alpha_absolute_3,
                      "alpha_absolute_4": alpha_absolute_4,
                      "beta_absolute_1": beta_absolute_1,
                      "beta_absolute_2": beta_absolute_2,
                      "beta_absolute_3": beta_absolute_3,
                      "beta_absolute_4": beta_absolute_4,
                      "gamma_absolute_1": gamma_absolute_1,
                      "gamma_absolute_2": gamma_absolute_2,
                      "gamma_absolute_3": gamma_absolute_3,
                      "gamma_absolute_4": gamma_absolute_4,
                      "delta_relative_1": delta_relative_1,
                      "delta_relative_2": delta_relative_2,
                      "delta_relative_3": delta_relative_3,
                      "delta_relative_4": delta_relative_4,
                      "theta_relative_1": theta_relative_1,
                      "theta_relative_2": theta_relative_2,
                      "theta_relative_3": theta_relative_3,
                      "theta_relative_4": theta_relative_4,
                      "alpha_relative_1": alpha_relative_1,
                      "alpha_relative_2": alpha_relative_2,
                      "alpha_relative_3": alpha_relative_3,
                      "alpha_relative_4": alpha_relative_4,
                      "beta_relative_1": beta_relative_1,
                      "beta_relative_2": beta_relative_2,
                      "beta_relative_3": beta_relative_3,
                      "beta_relative_4": beta_relative_4,
                      "gamma_relative_1": gamma_relative_1,
                      "gamma_relative_2": gamma_relative_2,
                      "gamma_relative_3": gamma_relative_3,
                      "gamma_relative_4": gamma_relative_4,
                      "delta_session_score_1": delta_session_score_1,
                      "delta_session_score_2": delta_session_score_2,
                      "delta_session_score_3": delta_session_score_3,
                      "delta_session_score_4": delta_session_score_4,
                      "theta_session_score_1": theta_session_score_1,
                      "theta_session_score_2": theta_session_score_2,
                      "theta_session_score_3": theta_session_score_3,
                      "theta_session_score_4": theta_session_score_4,
                      "alpha_session_score_1": alpha_session_score_1,
                      "alpha_session_score_2": alpha_session_score_2,
                      "alpha_session_score_3": alpha_session_score_3,
                      "alpha_session_score_4": alpha_session_score_4,
                      "beta_session_score_1": beta_session_score_1,
                      "beta_session_score_2": beta_session_score_2,
                      "beta_session_score_3": beta_session_score_3,
                      "beta_session_score_4": beta_session_score_4,
                      "gamma_session_score_1": gamma_session_score_1,
                      "gamma_session_score_2": gamma_session_score_2,
                      "gamma_session_score_3": gamma_session_score_3,
                      "gamma_session_score_4": gamma_session_score_4}

        watson_payload = db_payload.values()
        watson_data = get_watson_prediction(watson_payload)
        users.child(user).push(db_payload)  # push payload associated with a timestamp

        return watson_data
    except KeyError as e:
        print("Missing critical key")
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
    return requests.get(watson_endpoint, params=request_params)


def verify_user(user):
    snapshots = users.child(user).get()
    if not snapshots:
        return None
    else:
        return snapshots


if __name__ == '__main__':
    app.run()
