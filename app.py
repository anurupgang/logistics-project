from flask import Flask, jsonify
import sys
import time

app = Flask(__name__)
start_time = time.time()

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "status": "online",
        "service": "Smart Logistics & Shipment Tracking API",
        "domain": "Supply Chain & Logistics",
        "uptime_seconds": round(time.time() - start_time, 2)
    }), 200

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy", "database": "connected"}), 200

@app.route('/track/<tracking_id>', methods=['GET'])
def track_shipment(tracking_id):
    return jsonify({
        "tracking_id": tracking_id,
        "status": "In Transit",
        "estimated_delivery": "2 days",
        "location": "Central Distribution Hub"
    }), 200

# Failure Simulation Endpoint for CloudWatch & TTR Testing
@app.route('/crash', methods=['GET'])
def crash():
    print("CRITICAL: Crash endpoint triggered! Terminating process...")
    sys.exit(1)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
