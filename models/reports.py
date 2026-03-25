from pydantic import BaseModel
from models.location import Location
from typing import Optional
import datetime
import uuid

class ReportSubmittal(BaseModel):
    description: str
    location : Location



class Report(ReportSubmittal):
    id: str
    created_date: Optional[datetime.datetime]