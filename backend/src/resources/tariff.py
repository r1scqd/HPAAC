import dataclasses

from dependency_injector.wiring import Provide
from flask import jsonify
from flask_restful import Resource, reqparse
from loguru import logger
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.container import AppContainer
from src.db.base import Database
from src.db.models import TariffModel
from src.resources.shared import abort_if_obj_not_found

parser = reqparse.RequestParser()

for item in ('name', 'price', 'description'):
    parser.add_argument(item)


class TariffsResource(Resource):
    db: Database = Provide[AppContainer.db]

    def get(self):
        session: Session
        with self.db.session() as session:
            its = session.scalars(select(TariffModel)).all()
            return jsonify({'tariffs': [dataclasses.asdict(it) for it in its]})


class TariffResource(Resource):
    db: Database = Provide[AppContainer.db]

    def get(self, tariff_id: int):
        abort_if_obj_not_found(TariffModel, tariff_id)
        session: Session
        with self.db.session() as session:
            tariff = session.get(TariffModel, tariff_id)
            return jsonify({'tariff': tariff.to_dict()})

    def post(self):
        args = parser.parse_args()
        session: Session
        with self.db.session() as session:
            obj = TariffModel(
                name=args['name'],
                price=int(args['price']),
                description=args['description']
            )
            logger.info(obj)
            session.add(obj)

        return 200

    def delete(self, tariff_id: int):
        abort_if_obj_not_found(TariffModel, tariff_id)
        session: Session
        with self.db.session() as session:
            tariff = session.get(TariffModel, tariff_id)
            session.delete(tariff)
