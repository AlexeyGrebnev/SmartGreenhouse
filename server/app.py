from flask import Flask, request, jsonify
import sensors
import devices

# ✅ импорт автоматической логики
from gpio.auto_logic import auto_control

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

# ✅ Новый endpoint: автоматическое управление
@app.route("/auto", methods=["POST"])
def run_auto_mode():
    auto_control()
    return jsonify({"status": "auto mode executed"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)