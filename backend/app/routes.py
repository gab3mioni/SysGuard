from flask import Blueprint
from .controllers import StatusController, MetricsController

def register_routes(app):

    bp = Blueprint('api', __name__, url_prefix='/api')

    bp.add_url_rule('/status', 'status', StatusController.get_status, methods=['GET'])
    bp.add_url_rule('/metrics', 'metrics', MetricsController.get_metrics, methods=['GET'])

    app.register_blueprint(bp)