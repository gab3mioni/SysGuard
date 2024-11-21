import psutil

def get_system_metrics():
    """Retorna métricas de CPU e memória."""

    metrics = {
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory_percent": psutil.virtual_memory().percent,
        "memory_total": psutil.virtual_memory().total,
        "memory_used": psutil.virtual_memory().used,
        "memory_free": psutil.virtual_memory().free,
        "disk_percent": psutil.disk_usage('/').percent,
    }

    return metrics