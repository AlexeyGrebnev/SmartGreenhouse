from sensors import read_all
from gpio import controller

THRESHOLDS = {
    "temperature": 28,
    "humidity": 40,
    "light": 100
}

def auto_control():
    data = read_all()

    # Температура
    if data["temperature"] > THRESHOLDS["temperature"]:
        controller.control_device("fan", "on")
    else:
        controller.control_device("fan", "off")

    # Влажность
    if data["humidity"] < THRESHOLDS["humidity"]:
        controller.control_device("pump", "on")
    else:
        controller.control_device("pump", "off")

    # Освещенность
    if data["light"] < THRESHOLDS["light"]:
        controller.control_device("lamp", "on")
    else:
        controller.control_device("lamp", "off")