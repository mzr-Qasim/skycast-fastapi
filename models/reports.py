from pydantic import BaseModel
from models.location import Location
from typing import Optional
import datetime

class Report(BaseModel):
    description: str
    location : Location
    created_date: Optional[datetime.datetime]