from abc import ABC
from typing import Any

from dependency_injector.wiring import inject, Provide
from flask import jsonify
from flask_restful import abort, Resource, reqparse
from loguru import logger
from sqlalchemy import select
from sqlalchemy.orm import Session

from ..container import AppContainer
from ..db.base import Database, Base


@inject
def abort_if_obj_not_found(model: type[Base], pk: int | Any, db: Database = Provide[AppContainer.db]):
    session: Session
    with db.session() as session:
        obj = session.get(model, pk)
    if not obj:
        abort(404, message=f"{model.__tablename__.replace('_table', '')} {pk} not found")


# todo recursive jsonify
class ManyObjCrudResource(Resource):
    db: Database = Provide[AppContainer.db]
    model: type[Base]
    returnable_fields: tuple[str] = ()
    returnable_name: str
    rules: tuple[str] = ()

    id_needit = True

    def __init__(self):
        if self.id_needit and self.returnable_fields:
            p = list(self.returnable_fields)
            p.append('id')
            self.returnable_fields = tuple(p)

    def get(self):
        session: Session
        with self.db.session() as session:
            objs = session.scalars(select(self.model)).all()
            logger.info(objs)
            return jsonify({self.returnable_name: [
                it.to_dict(only=self.returnable_fields, rules=self.rules) for it in objs]})


class OneObjCrudResource(Resource):
    db: Database = Provide[AppContainer.db]
    model: type[Base]
    returnable_fields: tuple[str] = ()
    returnable_name: str

    required_post_fields: tuple[str] = ()
    unrequired_post_fields: tuple[str] = ()

    id_needit = True

    def __init__(self):
        if self.id_needit and self.returnable_fields:
            p = list(self.returnable_fields)
            p.append('id')
            self.returnable_fields = tuple(p)
        self.p = reqparse.RequestParser()
        for field in self.required_post_fields:
            self.p.add_argument(field, required=True)
        for field in self.unrequired_post_fields:
            self.p.add_argument(field, required=False)

    def get(self, id: int):
        abort_if_obj_not_found(self.model, id)
        session: Session
        with self.db.session() as session:
            obj = session.get(self.model, id)
            return jsonify({self.returnable_name: obj.to_dict(only=self.returnable_fields)})

    def post(self):
        args = self.p.parse_args()
        session: Session
        with self.db.session() as session:
            obj = self.model(**args)
            session.add(obj)
        return jsonify({'success': 'ok'})

    def delete(self, id: int):
        abort_if_obj_not_found(self.model, id)
        session: Session
        with self.db.session() as session:
            obj = session.get(self.model, id)
            session.delete(obj)
        return jsonify({'success': 'ok'})
