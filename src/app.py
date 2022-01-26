# flask_web/app.py

from flask import Flask, jsonify, request, Response
from flask_api import status
from UERanSim import UERanSim
from pyroute2 import IPRoute
import datetime
import os
import time


# globals - must return 428 if not configured
#trafficgen = TrafficGen()
ue = UERanSim("/etc/ueransim/open5gs-ue.yaml")
app = Flask(__name__)
datanet=os.environ["DATANET"]
tuniface=os.environ["UESIMIFACE"]

@app.route('/')
def hello_world():
    ts = int(datetime.datetime.now().timestamp())
    return jsonify(timestamp=ts), status.HTTP_200_OK

@app.route('/run', methods=['POST'])
def post_run():

    global ue

    if ue.get_conf() is None:
        jsonify(message='Missing configuration'), status.HTTP_400_BAD_REQUEST

    ue.apply_conf()
    try:
        ret = ue.run()
    except:
        return jsonify(message='Cannot run UE simulator.'), status.HTTP_400_BAD_REQUEST

    try:
        time.sleep(2)
        ipr = IPRoute()
        idx=ipr.link_lookup(ifname=tuniface)[0]
        ipr.route("add",dst=datanet,oif=idx)
    except:
        return jsonify(message="OK - Cannot add route - Maybe already in place."), status.HTTP_200_OK

    return jsonify(message="OK"), status.HTTP_200_OK

@app.route('/stop', methods=['POST'])
def post_stop():

    global ue

    try:
        ipr = IPRoute()
        ipr.route("del",dst=datanet)
    except:
        pass

    try:
        ret = ue.stop()
    except:
        return jsonify(message='Cannot stop UE simulator.'), status.HTTP_400_BAD_REQUEST


    return jsonify(message="OK"), status.HTTP_200_OK

@app.route('/poll', methods=['GET'])
def get_poll():

    global ue

    try:
        ret = ue.poll()
    except:
        return jsonify(message='Cannot poll UE simulator.'), status.HTTP_400_BAD_REQUEST

    return jsonify(message=ret), status.HTTP_200_OK

@app.route('/status', methods=['GET'])
def get_status():

    global ue

    try:
        ret = ue.status()
    except:
        return jsonify(message='Cannot poll UE simulator.'), status.HTTP_400_BAD_REQUEST

    return jsonify(message=ret), status.HTTP_200_OK

@app.route('/configuration', methods=['POST'])
def post_configuration():

    global ue

    configuration=request.get_json()
    if ue.update_conf(configuration) is not None:
        return Response(ue.to_json(), mimetype = 'application/json')
    else:
        return jsonify(message='invalid configuration'), status.HTTP_400_BAD_REQUEST

@app.route('/configuration', methods=['GET'])
def get_configuration():

    global ue

    return Response(ue.to_json(), mimetype = 'application/json')

@app.route('/configuration', methods=['DELETE'])
def delete_configuration():

    return jsonify(message="Not implemented"), status.HTTP_400_BAD_REQUEST

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=WEB_MGMT_PORT)
