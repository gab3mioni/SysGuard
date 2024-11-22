import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func
from datetime import datetime
import pandas as pd

db = SQLAlchemy()

class ContainerLog(db.Model):
    __tablename__ = 'container_log'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    container_name: Mapped[str] = mapped_column(nullable=False)
    action: Mapped[str] = mapped_column(nullable=False)
    timestamp: Mapped[datetime] = mapped_column(nullable=False, default=func.now())

class SystemLog(db.Model):
    __tablename__ = "system_metrics"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    cpu_percent: Mapped[float] = mapped_column(nullable=False)
    memory_percent: Mapped[float] = mapped_column(nullable=False)
    memory_total: Mapped[float] = mapped_column(nullable=False, default=0)
    memory_used: Mapped[float] = mapped_column(nullable=False)
    memory_free: Mapped[float] = mapped_column(nullable=False)
    disk_percent: Mapped[float] = mapped_column(nullable=False)
    timestamp: Mapped[datetime] = mapped_column(nullable=False, default=func.now())

def export_to_csv():

    conn = db.create_engine('sqlite:///app.db')

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