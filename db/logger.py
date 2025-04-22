from datetime import datetime
from db.database import get_connection

def log_sensor_data(temperature, humidity, light):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO sensor_logs (timestamp, temperature, humidity, light)
        VALUES (?, ?, ?, ?)
    """, (datetime.now().isoformat(), temperature, humidity, light))
    conn.commit()
    conn.close()

def log_action(device, action):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO action_logs (timestamp, device, action)
        VALUES (?, ?, ?)
    """, (datetime.now().isoformat(), device, action))
    conn.commit()
    conn.close()

def get_action_logs():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM action_logs ORDER BY timestamp DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows