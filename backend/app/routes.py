from flask import Blueprint, jsonify
from flask_cors import CORS
from .utils import get_system_metrics

bp = Blueprint('api', __name__, url_prefix='/api')
CORS(bp, resources={r"/api/*": {"origins": "http://localhost:3001"}})

@bp.route('/status', methods=['GET'])
def status():
    """Endpoint para verificar o status do backend."""
    return jsonify({"status": "Back online!"})

@bp.route('/metrics', methods=['GET'])
def metrics():
    """Retorna métricas do sistema"""
    metrics = get_system_metrics()
    return jsonify(metrics)