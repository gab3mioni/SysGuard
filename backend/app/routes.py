from flask import Blueprint, jsonify
from flask_cors import CORS
from .utils import get_system_metrics

bp = Blueprint('api', __name__, url_prefix='/api')
CORS(bp, resources={r"/api/*": {"origins": "http://localhost:3001"}})

@bp.route('/status', methods=['GET'])
def status():
    """
    Endpoint para verificar o status do backend.

    Retorna:
        json: Um objeto JSON com a mensagem indicando que o backend está online.
        Exemplo de resposta:
        {
            "status": "Back online!"
        }
    """
    return jsonify({"status": "Back online!"})

@bp.route('/metrics', methods=['GET'])
def metrics():
    """
    Endpoint para obter as métricas do sistema

    Utiliza a função get_system_metrics() para coletar informações de desempenho
    e recursos do sistema, como uso de CPU, memória e disco.

    Retorna:
        json: Um objeto JSON contendo as métricas do sistema.
        Exemplo de resposta:
        {
            "cpu_percent": 0.0,
            "memory_percent": 1.6,
            "disk_percent": 17.2,
        }
    """
    metrics = get_system_metrics()
    return jsonify(metrics)