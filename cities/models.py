from sqlalchemy import Column, String
from sqlalchemy.orm import Mapped
from sqlalchemy.testing.schema import mapped_column

from database import Base


class City(Base):
    __tablename__ = 'cities'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    additional_info: Mapped[str] = mapped_column(String(511), nullable=False)