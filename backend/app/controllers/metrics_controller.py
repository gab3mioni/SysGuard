from flask import jsonify
from ..services.metrics_service import MetricsService

class MetricsController:
    @staticmethod
    def get_metrics():
        try:
            metrics = MetricsService.collect_metrics()
            formatted_metrics = MetricsService.format_metrics(metrics)

            return jsonify(formatted_metrics)

        except Exception as e:
            return jsonify({'message': str(e)}), 500