import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr
from sqlmodel import Field, SQLModel,Column,String,Boolean,Enum,Integer,ForeignKey

from record_service.main import RecordService
from schemas.attendance import UserKycStatus

class RemitUserBase(SQLModel):
    # id: Column(Integer,primary_key=True,index=True)
    username :str=''# Column(String(60),unique=True,nullable=False)
    email :str
    phone:str=Field(sa_column=Column(String(16),nullable=True))
    photo :str=''
    phone_verified:bool=False
    hashed_password: str
    is_active: bool=False
    verified:bool=False
    kyc_status:UserKycStatus=UserKycStatus.UNVERIFIED#=Field(sa_column=Column(Enum(UserKycStatus),nullable=True)) #Column(Enum(UserKycStatus),default=UserKycStatus.UNVERIFIED)
    kyc_verified:str=False
    # full_kyc=Column(Boolean,default=False)
    is_superuser: bool=False
    is_staff:bool=False
    role:str=''
    # document:int=Field(sa_column=Column(Integer,ForeignKey("Documents.id"),nullable=True))
    # kycType:int=Field(sa_column=Column(Integer,ForeignKey("Kyc.id"),nullable=True))
    # limit on transaction
    total_limit:int=Field(sa_column=Column(Integer,default=0))
    per_day_limit:int=Field(sa_column=Column(Integer,default=0))
    per_month_limit:int=Field(sa_column=Column(Integer,default=0))
    per_year_limit:int=Field(sa_column=Column(Integer,default=0))
    # limit on amount
    per_day_amount:int=Field(sa_column=Column(Integer,default=0))
    per_month_amount:int=Field(sa_column=Column(Integer,default=0))
    per_year_amount:int=Field(sa_column=Column(Integer,default=0))
    @property
    def email_verified(self):
        return self.verified
class RemitUserCreate(BaseModel):
    email: EmailStr 
    password : str

class RemitUserRead(RemitUserBase):
    id:Optional[int] = Field(default=None, primary_key=True) 

class RemitUserUpdate(RemitUserBase):
    pass

 
class RemitUser(RemitUserBase, RecordService, table=True):
    id:Optional[int] = Field(default=None, primary_key=True) 