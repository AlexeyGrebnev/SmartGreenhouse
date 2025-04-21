from flask import Flask, request, jsonify
import sensors
import devices

app = Flask(__name__)

@app.route("/sensors", methods=["GET"])
def get_sensor_data():
    data = sensors.read_all()
    return jsonify(data)

@app.route("/control", methods=["POST"])
def control_device():
    payload = request.get_json()
    device = payload.get("device")
    action = payload.get("action")
    success = devices.control(device, action)
    return jsonify({"status": "ok" if success else "fail"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
