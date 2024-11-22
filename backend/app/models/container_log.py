from ..database import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func
from datetime import datetime

class ContainerLog(db.Model):
    __tablename__ = 'container_log'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    container_name: Mapped[str] = mapped_column(nullable=False)
    action: Mapped[str] = mapped_column(nullable=False)
    timestamp: Mapped[datetime] = mapped_column(nullable=False, default=func.now())