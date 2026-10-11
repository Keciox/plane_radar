from datetime import datetime

from sqlalchemy import CheckConstraint, DateTime, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column

from flyradar.database import Base


class UserItem(Base):
    __tablename__ = "user_items"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True
    )
    item_definition_id: Mapped[int] = mapped_column(
        ForeignKey("item_definitions.id"), nullable=False
    )
    float_value: Mapped[float] = mapped_column(nullable=False)
    acquired_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    source_case_id: Mapped[int | None] = mapped_column(
        ForeignKey("cases.id", ondelete="SET NULL"),
    )

    __table_args__ = (
        CheckConstraint("float_value >= 0.0 AND float_value <= 1.0", name="float_value_range"),
    )
