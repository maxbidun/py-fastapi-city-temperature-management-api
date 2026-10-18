from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.annotation import Annotated

from dependencies import get_db
from temperatures import shemas, crud

router = APIRouter()



@router.get("/temperatures", response_model=list[shemas.Temperature])
async def get_temperature(db:Annotated[AsyncSession, Depends(get_db)], city_id:int) -> shemas.Temperature:

    return await crud.get_temperatures(db)


