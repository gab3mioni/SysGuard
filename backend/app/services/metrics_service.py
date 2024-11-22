import os
import pandas as pd
from ..models.system_log import SystemLog
from ..database import db
from ..utils import get_system_metrics

class MetricsService:
    @staticmethod
    def collect_metrics():
        metrics = get_system_metrics()
        log = SystemLog(**metrics)
        db.session.add(log)
        db.session.commit()
        return metrics

    @staticmethod
    def format_metrics(metrics):
        formatted_metrics = {
            "Utilização da CPU": f"{metrics['cpu_percent']:.2f}%",
            "Utilização do disco": f"{metrics['disk_percent']:.2f}%",
            "Memória total": f"{metrics['memory_total'] / 1024 ** 3:.2f} GB",
            "Memória livre": f"{metrics['memory_free'] / 1024 ** 3:.2f} GB",
            "Memória utilizada": f"{metrics['memory_used'] / 1024 ** 3:.2f} GB ({metrics['memory_percent']:.2f}%)",
        }

        return formatted_metrics

    @staticmethod
    def export_to_csv():
        csv_dir = 'csv'

        if not os.path.exists(csv_dir):
            os.makedirs(csv_dir)

        system_log_path = os.path.join(csv_dir, 'system_metrics_data.csv')

        if os.path.exists(system_log_path):
            os.remove(system_log_path)

        system_log_query = db.session.query(SystemLog).order_by(SystemLog.timestamp.desc()).limit(50).all()
        system_log_df = pd.DataFrame([{
            'id': log.id,
            'cpu_percent': log.cpu_percent,
            'memory_percent': log.memory_percent,
            'memory_total': log.memory_total,
            'memory_used': log.memory_used,
            'memory_free': log.memory_free,
            'disk_percent': log.disk_percent,
            'timestamp': log.timestamp
        } for log in system_log_query])

        system_log_df.to_csv(system_log_path, index=False)