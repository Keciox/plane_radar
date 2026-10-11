from sqlalchemy import CheckConstraint, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from flyradar.database import Base


class CaseItem(Base):
    __tablename__ = "case_items"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    case_id: Mapped[int] = mapped_column(ForeignKey("cases.id", ondelete="CASCADE"), nullable=False)
    item_definition_id: Mapped[int] = mapped_column(
        ForeignKey("item_definitions.id"), nullable=False
    )
    weight: Mapped[int] = mapped_column(nullable=False)

    __table_args__ = (
        CheckConstraint("weight > 0", name="weight_minimum"),
        CheckConstraint("weight <= 100000", name="weight_maximum"),
        UniqueConstraint("case_id", "item_definition_id"),
    )
