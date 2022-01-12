from pydantic import BaseModel
from pydantic import EmailStr
from typing import Optional


class Add_Firm(BaseModel):
    Law_Firm_Name: str
    Law_Firm_Email_Address: EmailStr
    Load_Range: int
    Legal_Fee: int
    Law_Firm_Priority: str
    Remarks: str
    Law_Firm_Status: str = "Active"
    Display_Hierarchy: int

class Update_Firm(Add_Firm):
    pass

class UpdateHierarchy(BaseModel):
    Display_Hierarchy: int