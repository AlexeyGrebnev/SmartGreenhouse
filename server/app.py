from flask import Flask, request, jsonify
import sensors
import devices
from flask import render_template

# ✅ импорт автоматической логики
from gpio.auto_logic import auto_control

app = Flask(__name__)

@app.route("/sensors", methods=["GET"])
def get_sensor_data():
    data = sensors.read_all()
    return jsonify(data)

@app.route('/control', methods=['POST'])
def control_device():
    data = request.get_json()
    if not data or 'device' not in data or 'action' not in data:
        return jsonify({"error": "Missing 'device' or 'action' in request"}), 400

    device = data['device']
    action = data['action']

    if device not in ['water', 'light', 'fan']:
        return jsonify({"error": "Invalid device type"}), 400
    if action not in ['on', 'off']:
        return jsonify({"error": "Invalid action"}), 400

    return jsonify({"status": f"{device} turned {action}"}), 200

# ✅ Новый endpoint: автоматическое управление
@app.route("/auto", methods=["POST"])
def run_auto_mode():
    auto_control()
    return jsonify({"status": "auto mode executed"}), 200

@app.route("/logs", methods=["GET"])
def get_logs():
    logs = get_action_logs()
    return jsonify(logs)

@app.route("/sensors", methods=["GET"])
def get_sensor_data():
    data = sensors.read_all()
    # ✅ логирование
    log_sensor_data(data["temperature"], data["humidity"], data["light"])
    return jsonify(data)

@app.route("/control", methods=["POST"])
def control_device():
    payload = request.get_json()
    device = payload.get("device")
    action = payload.get("action")
    success = devices.control(device, action)
    # ✅ логирование
    if success:
        log_action(device, action)
    return jsonify({"status": "ok" if success else "fail"})

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


