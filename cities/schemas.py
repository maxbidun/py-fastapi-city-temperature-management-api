from pydantic import BaseModel, ConfigDict

class CityBase(BaseModel):
    name: str
    additional_info: str

class CityCreate(CityBase):
    pass

class CityUpdate(CityBase):
    nama: str | None = None
    additional_info: str | None = None

class City(CityBase):
    model_config = ConfigDict(from_attributes=True)

    id: int