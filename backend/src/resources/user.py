# todo переделать
import flask
from dependency_injector.wiring import inject, Provide
from flask_restful import Resource, abort, reqparse
from loguru import logger
from sqlalchemy.orm import Session

from .shared import abort_if_obj_not_found
from ..container import AppContainer
from ..db.base import Database
from ..db.models import UserModel, OrganizationModel, TariffModel

parser = reqparse.RequestParser()
for k in ('qwety', 'qwer'):
    parser.add_argument(k, required=True)


class UserResource(Resource):
    db: Database = Provide[AppContainer.db]

    def get(self, user_id: int):
        abort_if_obj_not_found(UserModel, user_id)
        session: Session
        with self.db.session() as session:
            user = session.get(UserModel, user_id)
            return {'user': user.to_dict(
                only=('first_name', 'last_name', 'middle_name', 'status', 'job_title', 'login', 'role'))}

    def post(self):
        ...

    def delete(self, user_id: int):
        abort_if_obj_not_found(UserModel, user_id)
        session: Session
        with self.db.session() as session:
            obj = session.get(UserModel, user_id)
            session.delete(obj)
