import psutil

def get_system_metrics():
    """Retorna métricas de CPU e memória."""

    metrics = {
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory_percent": psutil.virtual_memory().percent,
        "disk_percent": psutil.disk_usage('/').percent,
    }

    return metrics