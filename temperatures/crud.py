from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from temperatures import shemas, models


async def get_temperatures(db: AsyncSession, city_id: int) -> list[shemas.Temperature]:
    if city_id:
        return await db.scalars(select(models.Temperature).where(models.Temperature.city_id == city_id))
    else:
        return await db.scalars(select(models.Temperature))
