from ..database import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func
from datetime import datetime

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