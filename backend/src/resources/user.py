# todo переделать
import flask
from dependency_injector.wiring import inject, Provide
from flask_restful import Resource, abort, reqparse
from loguru import logger
from sqlalchemy.orm import Session

from ..container import AppContainer
from ..db.base import Database
from ..db.models import UserModel, OrganizationModel, TariffModel

parser = reqparse.RequestParser()
for k in ('qwety', 'qwer'):
    parser.add_argument(k, required=True)


class UserResource(Resource):
    db: Database = Provide[AppContainer.db]

    def get(self, user_id: int):
        # abort_if_user_not_found(user_id)
        session: Session
        with self.db.session() as session:
            tariff = TariffModel(
                name='comm',
                price=0,
                description='default tariff'
            )
            session.commit()
            logger.info(f'{tariff}')
            org = OrganizationModel(
                phone='7952351',
                email="ema@gm",
                ITN='213421412dsf',
                name='oweq',
                address='addrsname',
                tariff_id=tariff.id
            )
            logger.info(f'{org}')
            session.commit()
        print(flask.request.data)
        return user_id

    def post(self):
        print(flask.request.data)

    def delete(self, user_id: int):
        abort_if_user_not_found(user_id)
        # with self.db.session() as session:
        #     session.
        # user =
