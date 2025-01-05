from flask import Blueprint, request, jsonify, send_file
from ..core.backtest import get_metrics
from ..database.db import create_connection
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

@api_routes.route('/api/login', methods=['POST'])
def login():

    connection = create_connection()
    cursor = connection.cursor()
    data = request.get_json()

    username = data['username']
    password = data['password']

    try:
        query = 'SELECT * FROM Users WHERE Username = ?'

        cursor.execute(query, username)
        result = cursor.fetchone()

        if result:
            db_uid, db_username, db_passcode = result

            if(password == db_passcode):
                return {"response":"USER AUTH SUCCESS", "status_code":200}
            else:
                return {"response":"AUTH FAILED", "status_code":400}
        
        else:
            return {"response":'USER NOT FOUND', "status_code":400}

    finally:
        cursor.close()
        connection.close()