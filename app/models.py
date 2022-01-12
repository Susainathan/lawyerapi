from sqlalchemy import Column, Integer, String
from app.database import Base

class Law_Firm(Base):
    __tablename__ = "Law_Firm"

    id = Column(Integer, primary_key=True, nullable=False)
    Law_Firm_Name = Column(String, nullable=False)
    Law_Firm_Email_Address = Column(String, nullable=False)
    Load_Range = Column(Integer, nullable=False)
    Legal_Fee = Column(Integer, nullable=False)
    Law_Firm_Priority = Column(String, nullable=False)
    Remarks = Column(String, nullable=False)
    Law_Firm_Status = Column(String, nullable=False)
    Display_Hierarchy = Column(Integer, nullable=False)
