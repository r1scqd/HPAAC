# всё в одном файле ради того чтобы не было проблем с рекурсивном импортом и типизацией
import datetime
from enum import IntEnum
from typing import Optional

from sqlalchemy import ForeignKey, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

# many to many refs
access_education_material_table = Table(
    'access_education_material_table',
    Base.metadata,
    Column('user_id', ForeignKey('user_table.id'), primary_key=True),
    Column('material_id', ForeignKey('education_material_table.id'), primary_key=True),
)
access_test_table = Table(
    'access_test_table',
    Base.metadata,
    Column('user_id', ForeignKey('user_table.id'), primary_key=True),
    Column('test_id', ForeignKey('test_table.id'), primary_key=True),
)


class BaseWithId(Base):
    __abstract__ = True
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, init=False)


# models

class MessageModel(BaseWithId):
    __tablename__ = "message_table"
    user_id: Mapped[int] = mapped_column(ForeignKey('user_table.id'))
    date: Mapped[datetime.datetime]
    text: Mapped[str]
    user: Mapped['UserModel'] = relationship(init=False)


class UserModel(BaseWithId):
    __tablename__ = "user_table"
    first_name: Mapped[str]
    last_name: Mapped[str]
    middle_name: Mapped[str]
    organization_id: Mapped[int] = mapped_column(ForeignKey('organization_table.id'))
    status: Mapped[str]
    # должность
    job_title: Mapped[str]
    login: Mapped[str]
    hash_password: Mapped[str]
    # role_id: Mapped[int] = mapped_column(ForeignKey('role_table.id'))
    # лишние джоины не нужны
    role: Mapped[str]
    token: Mapped[str | None] = mapped_column(default=None)
    organization: Mapped['OrganizationModel'] = relationship(init=False)

    # external refs
    education_materials: Mapped[list['EducationMaterialModel']] = relationship(
        secondary=access_education_material_table, back_populates='access_users', init=False
    )
    test_sessions: Mapped[list['TestSessionModel']] = relationship(init=False)
    access_tests: Mapped[list['TestModel']] = relationship(
        secondary=access_test_table, back_populates='access_users', init=False
    )


class OrganizationModel(BaseWithId):
    __tablename__ = "organization_table"
    phone: Mapped[str]
    email: Mapped[str]
    # ITN - Individual Taxpayer Number (ИНН)
    ITN: Mapped[str]
    name: Mapped[str]
    address: Mapped[str]
    tariff_id: Mapped[int] = mapped_column(ForeignKey('tariff_table.id'))
    tariff: Mapped['TariffModel'] = relationship(init=False)


class TariffModel(BaseWithId):
    __tablename__ = "tariff_table"
    name: Mapped[str]
    price: Mapped[int]
    description: Mapped[str]


class EducationMaterialModel(BaseWithId):
    __tablename__ = "education_material_table"
    name: Mapped[str]
    text: Mapped[str]
    # todo owner?
    user_id: Mapped[int] = mapped_column(ForeignKey('user_table.id'))
    user: Mapped['UserModel'] = relationship(init=False)

    access_users: Mapped[list['UserModel']] = relationship(
        secondary=access_education_material_table, back_populates='education_materials', init=False
    )


class TestSessionModel(BaseWithId):
    __tablename__ = "test_session_table"
    user_id: Mapped[int] = mapped_column(ForeignKey('user_table.id'))
    date: Mapped[datetime.datetime]
    # todo result?
    result: Mapped[str]
    # todo resolve test
    vr_id: Mapped[Optional[int]] = mapped_column(ForeignKey('vr_table.id'), nullable=True)
    test_id: Mapped[Optional[int]] = mapped_column(ForeignKey('test_table.id'), nullable=True)
    # enum need it
    test_type: Mapped[int]
    user: Mapped['UserModel'] = relationship(back_populates='test_sessions', init=False)
    vr: Mapped[Optional['VRModel']] = relationship(init=False)
    test: Mapped[Optional['TestModel']] = relationship(init=False)


class TestType(IntEnum):
    common = 1
    vr = 2
    ...


class TestModel(BaseWithId):
    __tablename__ = "test_table"
    name: Mapped[str]
    # todo json
    text: Mapped[str]

    # external refs
    access_users: Mapped[list['UserModel']] = relationship(
        secondary=access_test_table, back_populates='access_tests', init=False
    )


class VRModel(BaseWithId):
    __tablename__ = "vr_table"
    name: Mapped[str]
    link: Mapped[str]
