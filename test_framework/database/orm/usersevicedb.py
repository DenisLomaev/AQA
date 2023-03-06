from sqlalchemy import Boolean, Column, Integer, String

from test_framework.database.base import BaseModel


class Client(BaseModel):
    __tablename__ = "db_client"

    id = Column(String, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    sur_name = Column(String)
    country_of_residence = Column(String)
    client_status = Column(String)


class Contacts(BaseModel):
    __tablename__ = "db_contacts"

    id = Column(Integer, primary_key=True)
    id_client = Column(String)
    sms_notification = Column(Boolean)
    push_notification = Column(Boolean)
    email = Column(String)
    email_subscription = Column(Boolean)
    mobile_phone = Column(String)


class Fingerprint(BaseModel):
    __tablename__ = "db_fingerprint"

    id = Column(Integer, primary_key=True)
    id_client = Column(String)
    fingerprint = Column(String)


class PassportData(BaseModel):
    __tablename__ = "db_passport_data"

    id = Column(Integer, primary_key=True)
    id_client = Column(String)
    identification_passport_number = Column(String)


class UserProfile(BaseModel):
    __tablename__ = "db_user_profile"

    id = Column(Integer, primary_key=True)
    id_client = Column(String)
    security_question = Column(String)
    security_answer = Column(String)


class Verification(BaseModel):
    __tablename__ = "db_verification"

    id = Column(Integer, primary_key=True)
    id_contact = Column(String)
    sms_verification_code = Column(String)
