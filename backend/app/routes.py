from flask import Blueprint, jsonify
from flask_cors import CORS
from .utils import get_system_metrics
from .models import db, SystemLog, export_to_csv

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
    try:

        metrics = get_system_metrics()

        cpu_percent = metrics.get("cpu_percent")
        memory_percent = metrics.get("memory_percent")
        memory_total = metrics.get("memory_total")
        memory_used = metrics.get("memory_used")
        memory_free = metrics.get("memory_free")
        disk_percent = metrics.get("disk_percent")

        new_metrics = SystemLog(
            cpu_percent=cpu_percent,
            memory_percent=memory_percent,
            memory_total=memory_total,
            memory_used=memory_used,
            memory_free=memory_free,
            disk_percent=disk_percent,
        )

        formatted_metrics = {
            "Utilização da CPU": f"{cpu_percent:.2f}%",
            "Utilização do disco": f"{disk_percent:.2f}%",
            "Memória total": f"{memory_total /1024**3:.2f} GB",
            "Memória livre": f"{memory_free /1024**3:.2f} GB",
            "Memória utilizada": f"{memory_used / 1024**3:.2f} GB ({memory_percent:.2f}%)",
        }

        db.session.add(new_metrics)
        db.session.commit()
        export_to_csv()

        return jsonify(formatted_metrics)

    except Exception as e:
        return jsonify({"error": f"Erro ao processar as métricas: {str(e)}"}), 500