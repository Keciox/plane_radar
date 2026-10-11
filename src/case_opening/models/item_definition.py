from datetime import datetime

from sqlalchemy import BigInteger, CheckConstraint, DateTime, String, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column

from case_opening.database import Base


class ItemDefinition(Base):
    __tablename__ = "item_definitions"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    rarity: Mapped[str] = mapped_column(String(50), nullable=False)
    weapon_type: Mapped[str] = mapped_column(String(50), nullable=False)
    weapon: Mapped[str] = mapped_column(String(50), nullable=False)
    skin: Mapped[str] = mapped_column(String(50), nullable=False)
    value: Mapped[int] = mapped_column(BigInteger, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )

    __table_args__ = (
        CheckConstraint(
            "rarity IN ('common', 'uncommon', 'rare', 'epic', 'legendary')", name="rarity_valid"
        ),
        CheckConstraint("value >= 0", name="value_non_negative"),
        CheckConstraint(
            "weapon_type IN ('assault', 'sniper', 'shotgun', 'pistol','knife')",
            name="weapon_type_valid",
        ),
        UniqueConstraint("weapon", "skin"),
    )
