from pydantic import BaseModel
from types_.inn import Inn
from types_.ogrn import OGRN

class Supplier(BaseModel):
    inn: Inn
    ogrn: OGRN
    name: str
    rating: str
    financeTotal: str
    financeStatus: str
    financeEfficiency: str
    financeCondition: str
    juridicalTotal: str
    juridicalTaxBehaviour: str
    juridicalHonesty: str
    juridicalDirector: str
    juridicalCourts: str
    experienceTotal: str
    experienceSize: str
    experienceStability: str
    experienceSustainability: str
    experienceSupplier: str