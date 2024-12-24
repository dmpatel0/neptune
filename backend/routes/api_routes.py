from flask import Blueprint, request, jsonify, send_file
from ..core.backtest import get_metrics
import json

api_routes = Blueprint('api_routes', __name__)

@api_routes.route('/api/status', methods=['GET'])
def get_status():
    return jsonify({"status": "Backend connection successful."}), 200

@api_routes.route('/api/run_backtest', methods=['POST'])
def run_backtest():
    data = request.get_json()

    metrics = get_metrics(data['ticker'], data['sDate'], data['eDate'], data['strat'], '1d')
    return {"response":json.loads(metrics.to_json()), "status_code":200}

@api_routes.route('/api/load_graph', methods=['GET'])
def load_graph():
    return send_file('../frontend/templates/graph.html', mimetype='text/html')