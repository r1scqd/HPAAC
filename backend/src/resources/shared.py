from typing import Any

from dependency_injector.wiring import inject, Provide
from flask_restful import abort
from sqlalchemy.orm import Session

from ..container import AppContainer
from ..db.base import Database, Base


@inject
def abort_if_obj_not_found(model: type[Base], pk: int | Any, db: Database = Provide[AppContainer.db]):
    session: Session
    with db.session() as session:
        obj = session.get(model, pk)
    if not obj:
        abort(404, message=f"{model.__tablename__} {pk} not found")
