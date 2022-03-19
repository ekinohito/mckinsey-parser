from typing import Optional
from pydantic import BaseModel

class Contacts(BaseModel):
    phone: Optional[str]
    email: Optional[str]
